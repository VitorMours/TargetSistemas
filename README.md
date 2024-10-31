# Entrevista Técnica da Target Sistemas

## Resolução das questões 1, 2 e 3
Essas questões são questões que exigem a execução de código, para a mesma, 
cada questão é um método, dentro da classe `Solution`, que podem ser chamados, e tem 
como retorno, uma string, que possui a resposta. Para executar todas as resoluções com um 
único comando, pode-se ser executado:


```python
if __name__ == "__main__":
    s = Solution()
    s.all()
```


## Resolução das questões 4 e 5
a)9

b)128

c)49

d)100

e)13

f)21


---

Primeiro deixaria todos os interruptores na mesma posição, e desligaria somente os interruptores do meio e da esquerda. Ao entrar na sala veria todas as lâmpadas, e decoraria se estariam ligadas ou desligadas. Ao sair, desligaria o interruptor da direita e ligaria da esquerda. Ao entrar na sala novamente, verificaria que a lâmpada que permaneceu igual é a do interruptor do meio, pois seu estado não mudou do anterior. A lâmpada que agora possui o mesmo estado que a do meio, que foi acionada antes da segunda ida, é a da direita, e a que está diferente, é a da esquerda