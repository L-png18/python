from django.db import models

class Perfil(models.Model):
    telefone = models.CharField(max_length=25, null=True, blank=True)
    rua = models.CharField(max_length=50, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_lenght=50, null=True, blank=True)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=50, null=True, blank=True)
    cliente = models.OneToOneField(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.data

    class Venda(models.Model):
        data = models.DateField(auto_now_add=True)
        cliente = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.telefone

class Produto(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    preco = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    qtde = models.IntegerField(null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)

    def __str__(self):
        return self.nome
    
class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

