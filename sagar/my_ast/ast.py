from abc import ABC, abstractmethod
from sagar.my_token.token import Token

class Node(ABC):
    @abstractmethod
    def token_literal(self) -> str:
        pass

class Statement(Node):
    @abstractmethod
    def statementNode(self):
        pass

class Expression(Node):
    @abstractmethod
    def expressionNode(self):
        pass

class Program(Node):
    def __init__(self):
        self.statements: list[Statement] = []
    
    def token_literal(self) -> str:
        if len(self.statements):
            return self.statements[0].token_literal()
        else:
            return ''

class Identifier(Expression):
    def __init__(self, token: Token, value: str):
        self.token = token
        self.value = value
    
    def token_literal(self) -> str:
        return self.token.literal

    def expressionNode(self):
        pass


class LetStatement(Statement):
    def __init__(self, token: Token, name: Identifier, value: Expression):
        self.token = token
        self.name = name
        self.value = value
    
    def token_literal(self):
        return self.token.literal
    
    def statementNode(self):
        pass


