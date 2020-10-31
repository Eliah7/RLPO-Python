# Authored by elia on 31/10/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""

if __name__ == '__main__':
    import os

    try:
        from jnius import autoclass

    except KeyError:
        os.environ['JDK_HOME'] = "/Library/Java/JavaVirtualMachines/jdk-9.0.4.jdk/Contents/Home/lib"
        os.environ['JAVA_HOME'] = "/Library/Java/JavaVirtualMachines/jdk-9.0.4.jdk/Contents/Home/lib"
        from jnius import autoclass

    Stack = autoclass('java.util.Stack')
    stack = Stack()
    stack.push('hello')
    stack.push('world')

    stack.pop()  # --> 'world'
    stack.pop()