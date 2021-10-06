# LALGCompiler
Compilers course assignment

# First steps
Execute the commands below to install the dependencies:
> python -m venv venv
> venv\Scripts\activate
> pip install antlr4-python3-runtime

# How to use
Execute the command below to execute the application:
> python main.py codes/com.txt

# When the grammar rules are changed, you need to generate the grammar files from the command: 
> java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 LALGGrammar.g4 -visitor -o generated
