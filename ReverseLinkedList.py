def reverse_list(head):
    anterior = None
    atual = head

    while atual: # != None
        next = atual.next
        atual.next = anterior

        anterior = atual
        atual = next
    return anterior


class Solution(object):
    pass