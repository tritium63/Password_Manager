def Encod_Decode():
    import base64
    Encoded=base64.b64encode(b'Passw@^%$*ord_2132')
    print(Encoded)
    Decoded=base64.b64decode(Encoded)
    print(Decoded)