from wink import flash_led

def initialize():
    from microcontroller import nvm
    if nvm[:5] == bytes(5):
        from keystore import KS_CTAP2, KS_PIN, KS_U2F, Counter
        for k in [KS_CTAP2(), KS_PIN(), KS_U2F()]:
            k.gen_new_keys()
            k.save_keystore()
        Counter(0).reset()
        Counter(4).reset()


def loop():
    import hid
    from ctap2 import ctap2
    from ctap_errors import CTAP2_ERR_KEEPALIVE_CANCEL
    print('loop')
    h = hid.hid()

    ret = None
    print(ret)
    while True:
        ret = h.receive()
        print(ret)
        if ret is not None:
            flash_led(4)
            cmd, data = ret
            if cmd in (hid.CTAPHID_MSG, hid.CTAPHID_CBOR):
                if cmd == hid.CTAPHID_MSG:
                   print("CTAPHID_MSG")
                else:
                    print("CTAPHID_CBOR")
                    resp = ctap2(data, h)
                    if h.is_cancelled():
                        h.send(cmd, CTAP2_ERR_KEEPALIVE_CANCEL)
                    else:
                        h.send(cmd, resp)


# initialize()
try:
    # flash_led(1)
    loop()
except:
    while True:
        pass  # needs a power recycle