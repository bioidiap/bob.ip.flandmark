/**
 * @author Andre Anjos <andre.anjos@idiap.ch>
 * @date Fri 25 Oct 16:54:55 2013
 *
 * @brief Bindings to bob::ap
 */

#ifdef NO_IMPORT_ARRAY
#undef NO_IMPORT_ARRAY
#endif
#include <xbob.blitz/capi.h>
#include <xbob.blitz/cleanup.h>
#include <xbob.io.base/api.h>
#include <xbob.extension/documentation.h>

extern PyTypeObject PyBobIpFlandmark_Type;

static auto s_setter = xbob::extension::FunctionDoc(
    "__set_default_model__",
    "Internal function to set the default model for the Flandmark class"
    )
    .add_prototype("path", "")
    .add_parameter("path", "str", "The path to the new model file")
    ;

PyObject* set_flandmark_model(PyObject*, PyObject* o) {

  int ok = PyDict_SetItemString(PyBobIpFlandmark_Type.tp_dict,
      "__default_model__", o);

  if (ok == -1) return 0;

  Py_RETURN_NONE;

}

static PyMethodDef module_methods[] = {
  {
    s_setter.name(),
    (PyCFunction)set_flandmark_model,
    METH_O,
    s_setter.doc()
  },
  {0}  /* Sentinel */
};

PyDoc_STRVAR(module_docstr, "Flandmark keypoint localization library");

#if PY_VERSION_HEX >= 0x03000000
static PyModuleDef module_definition = {
  PyModuleDef_HEAD_INIT,
  XBOB_EXT_MODULE_NAME,
  module_docstr,
  -1,
  module_methods,
  0, 0, 0, 0
};
#endif

static PyObject* create_module (void) {

  //makes sure that PyBobIpFlandmark_Type has a dictionary on tp_dict
  PyBobIpFlandmark_Type.tp_dict = PyDict_New();
  if (!PyBobIpFlandmark_Type.tp_dict) return 0;

  PyBobIpFlandmark_Type.tp_new = PyType_GenericNew;
  if (PyType_Ready(&PyBobIpFlandmark_Type) < 0) return 0;

# if PY_VERSION_HEX >= 0x03000000
  PyObject* m = PyModule_Create(&module_definition);
# else
  PyObject* m = Py_InitModule3(XBOB_EXT_MODULE_NAME, module_methods, module_docstr);
# endif
  if (!m) return 0;
  auto m_ = make_safe(m); ///< protects against early returns

  if (PyModule_AddStringConstant(m, "__version__", XBOB_EXT_MODULE_VERSION) < 0)
    return 0;

  /* register the types to python */
  Py_INCREF(&PyBobIpFlandmark_Type);
  if (PyModule_AddObject(m, "Flandmark", (PyObject *)&PyBobIpFlandmark_Type) < 0) return 0;

  /* imports dependencies */
  if (import_xbob_blitz() < 0) {
    PyErr_Print();
    PyErr_Format(PyExc_ImportError, "cannot import `%s'", XBOB_EXT_MODULE_NAME);
    return 0;
  }

  if (import_xbob_io_base() < 0) {
    PyErr_Print();
    PyErr_Format(PyExc_ImportError, "cannot import `%s'", XBOB_EXT_MODULE_NAME);
    return 0;
  }

  Py_INCREF(m);
  return m;

}

PyMODINIT_FUNC XBOB_EXT_ENTRY_NAME (void) {
# if PY_VERSION_HEX >= 0x03000000
  return
# endif
    create_module();
}