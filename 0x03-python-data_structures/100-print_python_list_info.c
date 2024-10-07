#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: PyObject pointer to a Python list object
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, alloc, i;
    PyObject *item;

    /* Check if the object is a list */
    if (!PyList_Check(p))
        return;

    /* Get the size of the list */
    size = PyList_Size(p);
    /* Get the allocated memory for the list */
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", alloc);

    /* Iterate over the list and print element types */
    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);  /* Get the element at index i */
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
