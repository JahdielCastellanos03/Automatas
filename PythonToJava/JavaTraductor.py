from antlr4 import *
from PythonToJavaLexer import PythonToJavaLexer
from PythonToJavaParser import PythonToJavaParser
from PythonToJavaListener import PythonToJavaListener

class TranslatorListener(PythonToJavaListener):
    def __init__(self):
        self.java_code = ""
        self.functions_code = ""

    def enterProgram(self, ctx: PythonToJavaParser.ProgramContext):
        self.java_code += "public class main {\n"
        self.java_code += "    public static void main(String[] args) {\n"

    def exitProgram(self, ctx: PythonToJavaParser.ProgramContext):
        self.java_code += "    }\n"
        self.java_code += self.functions_code
        self.java_code += "}\n"

    def enterFunction(self, ctx: PythonToJavaParser.FunctionContext):
        func_name = ctx.ID().getText()
        params = ', '.join([f"int {param.getText()}" for param in ctx.parameters().ID()])
        self.functions_code += f"    public static int {func_name}({params}) {{\n"

    def exitFunction(self, ctx: PythonToJavaParser.FunctionContext):
        self.functions_code += "    }\n"

    def enterAssignment(self, ctx: PythonToJavaParser.AssignmentContext):
        var_name = ctx.ID().getText()
        expr = ctx.expression().getText()
        self.functions_code += f"        int {var_name} = {expr};\n"

    def enterPrintStmt(self, ctx: PythonToJavaParser.PrintStmtContext):
        expr_text = ctx.expression().getText()
        self.java_code += f"        System.out.println({expr_text});\n"

    def enterReturnStmt(self, ctx: PythonToJavaParser.ReturnStmtContext):
        expr = ctx.expression().getText()
        self.functions_code += f"        return {expr};\n"

def main():
    file_name = input("Nombre del archivo Python (con extensión .txt): ")
    input_stream = FileStream(file_name)

    lexer = PythonToJavaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PythonToJavaParser(stream)
    tree = parser.program()

    translator = TranslatorListener()
    walker = ParseTreeWalker()
    walker.walk(translator, tree)

    with open("main.java", "w") as java_file:
        java_file.write(translator.java_code)

    print("Codigo guardado como: main.java")

if __name__ == "__main__":
    main()
