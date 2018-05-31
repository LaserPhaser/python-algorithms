
#include <Python.h>

long long
_fib(long long n) {
    if (n < 2)
        return n;
    else
        return _fib(n - 1) + _fib(n - 2);
}

static PyObject *
fib(PyObject *self, PyObject *args) {
    long long n;
    if (!PyArg_ParseTuple(args, "L", &n))
        return NULL;
    return Py_BuildValue("L", _fib(n));

}

static PyMethodDef fib_methods[] = {
        {
                "fib_fast", fib,  METH_VARARGS, "Calcs fib."
        },
        {       NULL,       NULL, 0,            NULL}
};

static struct PyModuleDef fib_def =
        {
                PyModuleDef_HEAD_INIT,
                "algorithms.arithmetic.fib", /* name of module */
                "",          /* module documentation, may be NULL */
                -1,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
                fib_methods
        };

PyMODINIT_FUNC PyInit_fib(void) {
    Py_Initialize();
    return PyModule_Create(&fib_def);
}