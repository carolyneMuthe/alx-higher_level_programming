#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p) {
    Py_ssize_t size = 0; // Initialize size
    PyObject *item;

    // Check if p is a list
    if (!PyList_Check(p)) {
        fprintf(stderr, "Provided object is not a list\n");
        return;
    }

    // Manually calculate the size of the list
    while (PyList_Check(p) && (item = PyList_GetItem(p, size)) != NULL) {
        size++;
    }

    printf("[\n");
    for (Py_ssize_t i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("  ");
        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        } else if (PyFloat_Check(item)) {
            print_python_float(item);
        } else {
            printf("<not a bytes or float object>\n");
        }
    }
    printf("]\n");
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "Provided object is not bytes\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    printf("Bytes object of size %zd: ", size);
    for (Py_ssize_t i = 0; i < size; i++) {
        printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "Provided object is not a float\n");
        return;
    }

    double value = PyFloat_AsDouble(p);
    printf("Float value: %f\n", value);
}
