

class Solution:
    def fibonacci(self) -> str:
        value = int(input("Digite um valor, e ele vai ser procurado dentro da sequência fibonacci: "))

        if value == 0:
            return f"O valor {value} está presente dentro da sequência fibonacci"    
        elif value == 1:
            return f"O valor {value} está presente dentro da sequência fibonacci"    
        
        actual_term = 0
        plus_value = 1
        while value > actual_term:

            fib_value = actual_term + plus_value
            actual_term = plus_value
            plus_value = fib_value
            
            if fib_value == value:
                return f"O valor {value} está presente dentro da sequência fibonacci"    
        
        return f"O valor {value} não está presente dentro da sequência fibonacci"    

    def count_a(self):
        word = str(input("Digite uma string, para vermos quantas letras \'a\' existem dentro dela: ")).strip()
        count = 0

        for char in word:
            if char == 'a':
                count += 1

        return f"Existem um total de {count} letras 'a' dentro de: '{word}'."

    def soma_value(self) -> str:
        indice = 12
        soma = 0
        k = 1

        while k < indice:
            k += 1
            soma += k
            
        return f"O valor final da soma, é de: {soma}"


    def all(self) -> list[str]:
        fib = self.fibonacci()
        count = self.count_a()
        soma = self.soma_value()
        
        for c in [fib, count, soma]:
            print(c)

if __name__ == "__main__":

    s = Solution()
    s.all()