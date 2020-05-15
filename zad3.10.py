def zakupy(**rzeczy):
    return len(rzeczy)
produkty = {'nakretki': 'kg','gwozdzie': 'kg','patyki': 'sztuki','kamienie': 'sztuki',}
print(zakupy(**produkty))