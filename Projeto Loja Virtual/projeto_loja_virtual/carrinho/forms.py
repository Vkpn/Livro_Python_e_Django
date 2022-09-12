from django import forms


OPCOES_QUANTIDADE_PRODUTO = []

for i in range(1,50):
    OPCOES_QUANTIDADE_PRODUTO.append((i, str(i)))


class FormAdicionarProdutoAoCarrinho(forms.Form):
    quantidade = forms.TypedChoiceField(choices=OPCOES_QUANTIDADE_PRODUTO, coerce=int)
    atualizar = forms.BooleanField(required=False, widget=forms.HiddenInput)
