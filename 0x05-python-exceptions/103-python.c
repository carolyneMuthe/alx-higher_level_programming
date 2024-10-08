#include <Python.h>

/* Forward declaration of print_python_bytes */
void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p) {
    // Check if p is a list
    if (!PyList_Check(p)) {
        fprintf(stderr, "Provided object is not a list\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    printf("[");
    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        print_python_bytes(item);  // Call to the function
        if (i < size - 1) {
            printf(", ");
        }
    }
    printf("]\n");
}

void print_python_bytes(PyObject *p) {
    // Check if p is a bytes object
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "Provided object is not bytes\n");
        return;
    }

    // Print byte object details
    Py_ssize_t size = PyBytes_Size(p);
    printf("Bytes object of size %zd: ", size);
    for (Py_ssize_t i = 0; i < size; i++) {
        printf("%02x ", (unsigned char) PyBytes_AsString(p)[i]);
    }
    printf("\n");
}
