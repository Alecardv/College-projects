# -*- coding: utf-8 -*-

import StringIO
data = StringIO.StringIO()
numberSpace = 0
Cantidad = 0
Store = 0
numberlabel = 1


class pila():

    def __init__(self, s=None):
        self.l = []
        self.ant = s

    def push(self, obj):
        self.l.append(obj)
        return "%l" + str(len(self.l) - 1)

    def pop(self):
        self.l.pop()
        return "%l" + str(len(self.l))

    def len(self):
        return len(self.l)

    def empty(self):
        return len(self.l) == 0


p = pila()


def push(obj, out):
    global p
    global Cantidad
    global Store
    if p.len() > 7:
        print >>out, "st  %l" + str(Store) + ",  [%fp -" + str(Cantidad) + "]   ! spill %" + str(Store) + " (" + str(Store + 1) + ")"
        Store += 1
        Cantidad += 4
        p = pila(p)
    return p.push(obj)


def pop(out):
    global p
    global Cantidad
    global Store
    temp = p.pop()
    if p.empty() and p.ant:
        p = p.ant
    if not p.ant and (Store - 1) == len(p.l):
        Store -= 1
        Cantidad -= 4
        print >>out, "ld  %l" + str(Store) + ",  [%fp -", (Cantidad), "]   ! recover " + str(Store + 1)
    return temp


def generate(out, top):
    print >>out, "! Creado por mpascal.py"
    print >>out, "! J. Alejandro Cardona Valdes, IS744 (2016-1)"
    print >>out, "\n      .section \".text\""
    print >>data, "      .section \".rodata\""
    emit_program(out, top)
    print >>out, data.getvalue()


def new_label():
    global numberlabel
    label = ".L" + str(numberlabel)
    numberlabel = numberlabel + 1
    return label


def alocate_locals(Arglist):
    if Arglist.__class__.__name__ == 'ParametersList':
        expr = Arglist.param_decl
    elif Arglist.__class__.__name__ == 'VariableList':
        expr = Arglist.var_decl
    else:
        expr = Arglist.expr
    i = 0
    for e in expr:
        if e.__class__.__name__ == 'Parameter':
            if e.typename.__class__.__name__ == 'TypeIndexed':
                i = i + 4 * int(e.typename.intliteral.value)
            else:
                i = i + 4
        else:
            i = i + 4
    i = i + 64
    while (i % 8 != 0):
        i = i + 1
    return i


def emit_program(out, top):
    print >>out, "\n! program"
    for f in top.funlist:
        emit_function(out, f)


def emit_function(out, fun):
    global Cantidad
    print >>out, "\n! function: %s (start)" % fun.id
    print >>out, fun.id, ":"
    if not fun.varlist.__class__.__name__ == "Empty":
        Cantidad = alocate_locals(fun.varlist)
        print >>out, "      save %sp, -", Cantidad, ", %sp "
    else:
        print >>out, "      save %sp, -128, %sp"
    emit_vardecl(out, fun.varlist)
    emit_statements(out, fun.statements)
    test_label = new_label()
    print >>out, "%s:" % (test_label)
    if fun.id == 'main':
        print >>out, "     mov  0, %o0"
        print >>out, "     call _exit"
        print >>out, "     nop"
    print >>out, "     ret"
    print >>out, "     restore"
    print >>out, "\n! function: %s (end)" % fun.id


def emit_statements(out, statements):
    for s in statements.statements:
        emit_statement(out, s)


def emit_statement(out, s):
    if s.__class__.__name__ == 'AssignmentStatement':
        emit_assignment(out, s)
    elif s.__class__.__name__ == 'PrintStatement':
        emit_print(out, s)
    elif s.__class__.__name__ == 'ReadStatement':
        emit_read(out, s)
    elif s.__class__.__name__ == 'WhileStatement':
        emit_while(out, s)
    elif s.__class__.__name__ == 'BeginStatement':
        emit_begin(out, s)
    elif s.__class__.__name__ == 'WriteStatement':
        emit_write(out, s)
    elif s.__class__.__name__ == 'ReturnStatement':
        emit_return(out, s)
    elif s.__class__.__name__ == 'IfStatement':
        emit_if(out, s)
    elif s.__class__.__name__ == 'IfElseStatement':
        emit_ifelse(out, s)
    elif s.__class__.__name__ == 'BreakStatement':
        emit_break(out, s)
    elif s.__class__.__name__ == 'SkipStatement':
        emit_skip(out, s)
    elif s.__class__.__name__ == 'Empty':
        pass


def emit_assignment(out, s):
    print >>out, "\n! assignment (start)"
    eval_expression(out, s.expr)
    print >>out, "!     %s := pop" % s.location.id
    print >>out, "! assignment (end)"


def emit_print(out, s):
    label = new_label()
    value = s.string_literal
    print >>out, "! print (start)"
    print >>data, "%s:  .asciz  %s" % (label, value)
    print >>out, "      sethi %hi(",label,"), %o0"
    print >>out, "      or    %o0, %lo(",label, "), %o0"
    print >>out, "      call hlprint"
    print >>out, "      nop" 
    print >>out, "! print (end)"


def emit_read(out, s):
    print >>out, "\n! read (start)"
    print >>out, "      call hlread"
    print >>out, "      nop"
    print >>out, "      st %o0, result"
    print >>out, "! read (end)"


def emit_while(out, s):
    print >>out, "\n! while (start)"
    print >>out, "! test:"

    test_label = new_label()
    done_label = new_label()
    print >>out, "%s:" % test_label

    eval_relation(out, s.condition)
    print >> out, "! EvalueRelop"
    l = pop(out)
    print >>out, "cmp %s" % str(l), " %g0 !", " %s contiene resultado del relop" % str(l)
    print >> out, "be .%s  ! == 0, false, goto else" % test_label
    print >> out, "nop"
    print >>out, "!   Relop:= pop"
    print >>out, "!   if not Relop: go to done"

    emit_statement(out, s.body)
    print >>out, " ba %s" % test_label
    print >>out, " nop"
    print >>out, "!   goto test"
    print >>out, "!   done:"
    print >>out, "! goto %s" % test_label
    print >>out, "%s:" % done_label
    print >>out, "! While (end) "


def emit_vardecl(out, varlist):
    pass


def emit_begin(out, s):
    emit_statements(out, s.statements)


def emit_write(out, s):
    print >>out, "\n! write (start)"
    eval_expression(out, s.expr)
    print >>out, "!     expr := pop"
    print >>out, "!     write(expr)"
    print >>out, "          mov  %lm, %o0"
    print >>out, "          call flwritei"
    print >>out, "          nop"
    print >>out, "! write (end)"


def emit_return(out, s):
    print >>out, "\n! return (start)"
    eval_expression(out, s.expr)
    print >>out ,"! return := pop "
    print >>out, "! return (end)"


def emit_if(out, s):
    print >>out, "\n! if (start)"
    print >>out, "! test:"
    test_label= new_label()
    done_label= new_label()
    print >>out, "%s:" %test_label
    eval_relation(out, s.condition)
    l=pop(out)
    print >>out , "cmp %s"% str(l) ," %g0 !", " %s contiene resultado del relop" % str(l)
    print >> out , "be .%s  ! == 0, false, goto else" % test_label
    print >> out , "nop"
    print >>out, "!  relop:= pop"
    print >>out, "!  if not relop: goto %s" %done_label
    emit_statements(out, s.then)
    print >>out ," ba %s" % test_label
    print >>out ," nop"
    print >>out , "!   goto test"
    print >>out , "!   done:"
    print >>out, "\n! goto %s" %test_label
    print >>out, "%s:" %done_label
    print >>out, "! if (end)"


def emit_ifelse(out, s):
    print >>out, "\n! ifelse (start)"
    print >>out, "! test:"
    test_label= new_label()
    done_label= new_label()
    print >>out, "%s:" %test_label

    eval_relation(out, s.condition)
    l = pop(out)
    print >> out, "cmp %s,"% str(l) ," %g0" , "!%s contiene resultado de Relop" % str(l)
    print >> out, "be %s  ! == 0, false, goto else" % test_label
    print >> out, "nop"
    if not s.then == None:
        print >>out, "!  if false go to else"
        print >>out, "!   Statements fot true"
        emit_statement(out, s.then)
        print >>out, " ba %s" % test_label
        print >>out, " nop"
        print >>out, "!   go to next"
        print >>out, "!   else:"
        print >>out, "!   statemnts for false"
        emit_statement(out, s._else)
        print >>out, "!  next:"
    else:
        print >> out, "!  if false: goto done"
        print >> out, "!  statements"
        print >> out, "!  next:"
    print >>out, "\n! goto %s" %done_label
    print >>out, "%s:" %done_label
    print >>out, "! ifelse (end)"


def emit_break(out, s):
    print >>out, "\n! break (start)"
    print >>out, "! break (end)"


def emit_skip(out, s):
    print >>out, "\n! print (start)"
    print >>out, "! print (end)"


def eval_expression(out, expr):
    if expr.__class__.__name__ == "Literal":
        print >>out, "mov %s , %s ! push %s" % (expr.value, push(expr.value, out), expr.value)

    elif expr.__class__.__name__ == "Location":
        Push = push(expr.id, out)
        String1 = expr.id
        print >>out, "mov %s , %s ! push %s" % (String1, Push, String1)

    elif expr.__class__.__name__ == "BinaryOp":
        eval_expression(out, expr.left)
        eval_expression(out, expr.right)
        l = pop(out)
        r = pop(out)
        if expr.op == '+':
            Push = push(str(l), out)
            print >>out, "add  %s , %s , %s !  %s + %s -> %s " % (str(l), str(r), Push, str(l), str(r), Push)
        elif expr.op == '-':
            Push = push(str(l), out)
            print >>out, "sub  %s , %s , %s !  %s - %s -> %s " % (str(l), str(r), Push, str(l), str(r), Push)
        elif expr.op == '*':
            Push = push("%o0", out)
            print >>out, " mov %s ,  %%o0 " % (str(l))
            print >>out, " call .mul !  mul"
            print >>out, " mov %s , %%o1 " % str(r)
            print >>out, " mov %%o0 , %s" % Push
        elif expr.op == '/':
            Push = push("%o0", out)
            print >>out, " mov %s ,  %%o0 " % (str(l))
            print >>out, "call .mod !  mod"
            print >>out, " mov %s , %%o1 " % str(r)
            print >>out, " mov %%o0 , %s" % Push

    elif expr.__class__.__name__ == "UnaryOp":
        eval_expression(out,expr.expr)
        l = pop(out)
        Push=push(str(l), out)
        if expr.op == '+':
            print >>out, "add %s , %s! + %s -> %s" % (str(l), Push, str(l), Push)
        elif expr.op == '-':
            print >>out, "sub %s , %s! - %s -> %s" % (str(l), Push, str(l), Push)

    elif expr.__class__.__name__ == "Group":
        eval_expression(out, expr.expr)

    elif expr.__class__.__name__ == "LocationIndexed":
        eval_expression(out, expr.expr)
        print >>out, "!     index := pop"
        print >>out, "!     push a[index]"

    elif expr.__class__.__name__ == "FunCall":
        emit_funcall(out, expr)

    elif expr.__class__.__name__ == "IntCast":
        pass

    elif expr.__class__.__name__ == "FloatCast":
        pass


def emit_exprlist(out, exprlist):
    count = 0
    for e in exprlist.expr:
        eval_expression(out, e)
        count += 1
        print >>out, "!     arg%s := pop" % count


def eval_relation(out, relation):
    if relation.__class__.__name__ == "RelationalOp":
        eval_expression(out, relation.left)
        eval_expression(out, relation.right)
        test_label = new_label()
        l = pop(out)
        r = pop(out)
        op = ''
        if relation.op == '>':
            op = 'gt'
        elif relation.op == '<':
            op = 'lt'
        elif relation.op == '<=':
            op = 'le'
        elif relation.op == '>=':
            op = 'ge'
        elif relation.op == '!=':
            op = 'ne'
        elif relation.op == '==':
            op = 'eq'
        print >>out, "!     %s" % op
        Push = push(str(l), out)
        print >> out ," cmp %s,%s,%s  ! if %s < %s -> %s" % (str(l) , str(r) , Push , str(l) , str(r) , Push)
        print >> out ," bl %s ! rama menor que " % test_label
        print >> out ," mov 1, %s  ! rama retardo (siempre se ejecuta)" % Push
        print >> out ," mov 0 %s " % Push
        print >> out ,"%s" % test_label
    elif relation.__class__.__name__ == "UnaryRelation":
        pass
    elif relation.__class__.__name__ == "RelationGroup":
        pass


def emit_arglist(out, Arglist):
    i = 0
    for e in Arglist.expr:
        eval_expression(out, e)
        i = i + 1
        print >>out, "!  arg" + str(i) + ":= pop"


def emit_paramlist(out, paramlist):
    i = 0
    for e in paramlist.param_decl:
        if e.__class__.__name__ != 'Empty':
            Push = push(e.id, out)
            String1 = e.id
            print >>out, "mov %s , %s ! push %s" % (String1, Push, String1)
            i = i + 1
            print >>out, "!  arg" + str(i) + ":= pop"


def emit_funcall(out, Funcall):
    global Cantidad
    print >>out, str(Funcall.id.id), ":"
    if not Funcall.params.expr.__class__.__name__ == "Empty":
        Cantidad = alocate_locals(Funcall.params)
        print >>out, "  save  %sp , -", Cantidad, ", %sp "
    test_label = new_label()
    emit_arglist(out, Funcall.params)
    print >>out, "%s:" % test_label
    print >>out, "  ret"
    print >>out, "  restore"
    print >>out, "!   push ", Funcall.id.id, "(Arglist)"
