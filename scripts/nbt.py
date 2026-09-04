"""極簡 NBT 讀取器，只夠用來讀 level.dat 的 Forge 註冊表快照。"""

import gzip
import struct

TAG_END, TAG_BYTE, TAG_SHORT, TAG_INT, TAG_LONG = 0, 1, 2, 3, 4
TAG_FLOAT, TAG_DOUBLE, TAG_BYTE_ARRAY, TAG_STRING = 5, 6, 7, 8
TAG_LIST, TAG_COMPOUND, TAG_INT_ARRAY, TAG_LONG_ARRAY = 9, 10, 11, 12


class Reader:
    def __init__(self, data):
        self.d = data
        self.i = 0

    def take(self, n):
        chunk = self.d[self.i:self.i + n]
        self.i += n
        return chunk

    def u1(self):
        return self.take(1)[0]

    def i2(self):
        return struct.unpack(">h", self.take(2))[0]

    def u2(self):
        return struct.unpack(">H", self.take(2))[0]

    def i4(self):
        return struct.unpack(">i", self.take(4))[0]

    def i8(self):
        return struct.unpack(">q", self.take(8))[0]

    def f4(self):
        return struct.unpack(">f", self.take(4))[0]

    def f8(self):
        return struct.unpack(">d", self.take(8))[0]

    def string(self):
        return self.take(self.u2()).decode("utf-8", "replace")

    def payload(self, tag):
        if tag == TAG_BYTE:
            return self.u1()
        if tag == TAG_SHORT:
            return self.i2()
        if tag == TAG_INT:
            return self.i4()
        if tag == TAG_LONG:
            return self.i8()
        if tag == TAG_FLOAT:
            return self.f4()
        if tag == TAG_DOUBLE:
            return self.f8()
        if tag == TAG_BYTE_ARRAY:
            return self.take(self.i4())
        if tag == TAG_STRING:
            return self.string()
        if tag == TAG_LIST:
            item_tag = self.u1()
            return [self.payload(item_tag) for _ in range(max(0, self.i4()))]
        if tag == TAG_COMPOUND:
            out = {}
            while True:
                t = self.u1()
                if t == TAG_END:
                    return out
                # 名稱必須在 payload 之前讀取；不可寫成 out[self.string()] = self.payload(t)
                name = self.string()
                out[name] = self.payload(t)
        if tag == TAG_INT_ARRAY:
            return [self.i4() for _ in range(self.i4())]
        if tag == TAG_LONG_ARRAY:
            return [self.i8() for _ in range(self.i4())]
        raise ValueError(f"未知的 NBT tag: {tag}")


def load(path):
    with open(path, "rb") as fh:
        head = fh.read(2)
    data = gzip.open(path, "rb").read() if head == b"\x1f\x8b" else open(path, "rb").read()
    r = Reader(data)
    tag = r.u1()
    r.string()  # root name
    return r.payload(tag)
