#include <Python.h>

/**
 * print_python_bytes - Prints basic info about Python bytes objects.
 * @p: Pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
    if (!PyBytes_Check(p))
    {
        printf("[.] bytes object info\n[ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyObject_Length(p);
    char *str = PyBytes_AsString(p);
    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str ? str : "None");
    
    printf("  first %zd bytes:", size < 10 ? size : 10);
    for (Py_ssize_t i = 0; i < (size < 10 ? size : 10); i++)
    {
        printf(" %02x", (unsigned char)str[i]);
    }
    printf("\n");
}

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: Pointer to a Python object
 */
void print_python_list(PyObject *p)
{
    if (!PyList_Check(p))
    {
        printf("[.] list object info\n[ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyObject_Length(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
    for (Py_ssize_t i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        const char *type = Py_TYPE(item)->tp_name;
        printf("Element %zd: %s\n", i, type);
        if (strcmp(type, "bytes") == 0)
            print_python_bytes(item);
    }
}
