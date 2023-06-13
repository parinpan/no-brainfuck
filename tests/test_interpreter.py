import unittest
from interpreter import brainfuck_reader


class InterpreterTest(unittest.TestCase):
    def test(self):
        self.assertEqual(brainfuck_reader(''), '')
        self.assertEqual(brainfuck_reader('[]'), '')
        self.assertEqual(brainfuck_reader('+[-]'), '')
        self.assertEqual(brainfuck_reader('>+[+[<]>>+<+]------[>....<-]'), 'A' * 1000)
        self.assertEqual(brainfuck_reader('>+[+[<]>>+<+]>>------[<....>-]'), 'A' * 1000)

        self.assertEqual(brainfuck_reader("""
            ++++++++++[>+>+++>+++++++>++++++++++<<<<-]
            >>>>++.-----.++.+++++.++++++++++.---------
            .+++++.--------.-----.+++++++++++++.<-----
            -.>-------.++++++.------------.++++++++.++
            +.<<++++++++++++++++.>>---------.+++++++++
            +++.--.
        """), 'fachrinfan@gmail.com')

        self.assertEqual(brainfuck_reader("""
            # with some comments here
            ++++++++++[>+>+++>+++++++>++++++++++<<<<-]
            >>>>++.-----.++.+++++.++++++++++.---------
            .+++++.--------.-----.+ #here ++++++++++++.<-----
            -.>-------.++++++.------------.++++++++.++
            +.<<++++++++++++++++.>>------ # and here :p ---.+++++++++
            +++.--.
        """), 'fachrinfan@gmail.com')
