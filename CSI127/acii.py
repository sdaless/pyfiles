#Sara D'Alessandro
#My first machine language program that prints "Mihi cura furturi."

# Store 'Hello world!' at the top of the stack
ADDI $sp, $sp, -13
ADDI $t0, $zero, 77 # M
SB $t0, 0($sp)
ADDI $t0, $zero, 105 # i
SB $t0, 1($sp)
ADDI $t0, $zero, 104 # h
SB $t0, 2($sp)
ADDI $t0, $zero, 105 # i
SB $t0, 3($sp)
ADDI $t0, $zero, 32 # (space)
SB $t0, 4($sp)
ADDI $t0, $zero, 99 # c
SB $t0, 5($sp)
ADDI $t0, $zero, 117 # u
SB $t0, 6($sp)
ADDI $t0, $zero, 114 # r
SB $t0, 7($sp)
ADDI $t0, $zero, 97 # a
SB $t0, 8($sp)
ADDI $t0, $zero, 32 # (space)
SB $t0, 9($sp)
ADDI $t0, $zero, 102 # f
SB $t0, 10($sp)
ADDI $t0, $zero, 117 # u
SB $t0, 11($sp)
ADDI $t0, $zero, 116 # t
SB $t0, 12($sp)
ADDI $t0, $zero, 117 # u
SB $t0, 13($sp)
ADDI $t0, $zero, 114 # r
SB $t0, 14($sp)
ADDI $t0, $zero, 105 # i
SB $t0, 15($sp)
ADDI $t0, $zero, 0 # (null)
SB $t0, 16($sp)

ADDI $v0, $zero, 4 # 4 is for print string
ADDI $a0, $sp, 0
syscall 			# print to the log
