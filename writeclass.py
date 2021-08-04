class WriteMethod:
    def _write_script(copied,copy_to, copied_encoding="utf-8", copy_to_encoding="utf_8"):
        with open(copied, "r", encoding=copied_encoding) as A:
            with open(copy_to, "w", encoding=copy_to_encoding) as B:
                for code in A.read():
                    B.write(code)

    def _write_binary(copied, copy_to):
        with open(copied, "rb") as A:
            with open(copy_to, "wb") as B:
                B.write(A.read())
