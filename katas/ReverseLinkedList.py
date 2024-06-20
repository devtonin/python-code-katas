def reverse_list(head):
    anterior = None
    atual = head

    while atual:  # != None
        nextt = atual.next
        atual.next = anterior

        anterior = atual
        atual = nextt
    return anterior


class Solution(object):
    pass
