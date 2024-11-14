# Generated from PythonToJava.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PythonToJavaParser import PythonToJavaParser
else:
    from PythonToJavaParser import PythonToJavaParser

# This class defines a complete listener for a parse tree produced by PythonToJavaParser.
class PythonToJavaListener(ParseTreeListener):

    # Enter a parse tree produced by PythonToJavaParser#program.
    def enterProgram(self, ctx:PythonToJavaParser.ProgramContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#program.
    def exitProgram(self, ctx:PythonToJavaParser.ProgramContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#statement.
    def enterStatement(self, ctx:PythonToJavaParser.StatementContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#statement.
    def exitStatement(self, ctx:PythonToJavaParser.StatementContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#function.
    def enterFunction(self, ctx:PythonToJavaParser.FunctionContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#function.
    def exitFunction(self, ctx:PythonToJavaParser.FunctionContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#assignment.
    def enterAssignment(self, ctx:PythonToJavaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#assignment.
    def exitAssignment(self, ctx:PythonToJavaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#printStmt.
    def enterPrintStmt(self, ctx:PythonToJavaParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#printStmt.
    def exitPrintStmt(self, ctx:PythonToJavaParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#returnStmt.
    def enterReturnStmt(self, ctx:PythonToJavaParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#returnStmt.
    def exitReturnStmt(self, ctx:PythonToJavaParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#functionCall.
    def enterFunctionCall(self, ctx:PythonToJavaParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#functionCall.
    def exitFunctionCall(self, ctx:PythonToJavaParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#parameters.
    def enterParameters(self, ctx:PythonToJavaParser.ParametersContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#parameters.
    def exitParameters(self, ctx:PythonToJavaParser.ParametersContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#arguments.
    def enterArguments(self, ctx:PythonToJavaParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#arguments.
    def exitArguments(self, ctx:PythonToJavaParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#expression.
    def enterExpression(self, ctx:PythonToJavaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#expression.
    def exitExpression(self, ctx:PythonToJavaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#atom.
    def enterAtom(self, ctx:PythonToJavaParser.AtomContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#atom.
    def exitAtom(self, ctx:PythonToJavaParser.AtomContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#op.
    def enterOp(self, ctx:PythonToJavaParser.OpContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#op.
    def exitOp(self, ctx:PythonToJavaParser.OpContext):
        pass



del PythonToJavaParser