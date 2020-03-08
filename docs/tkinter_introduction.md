# Tkinter

* The **tkinter** package is a thin object-oriented layer on top of Tcl/Tk.

* set of wrappers that implement the **Tk widgets** as Python classes

```Python
import tkinter as tk

# creates a toplevel widget of Tk which usually is
# the main window of an application
top_level_window = tk.Tk()
```

* To program using **tkinter** we might often have to refer to the [**tk documentation**](https://tkdocs.com/)

## Configuring widgets

* Widget can be configured while creation using keyword arguments

```Python
import tkinter as tk

root = tk.Tk()
submit_button = tk.Button(root, text = "Submit", bg = "green" )
```

* Widget can be configured through dictionary like index

```Python
submit_button["text"] = "Submit"
```

* Widget can also be configured using the `config()` method on the widget itself.

```Python
submit_button.config(text = "Submit", bg = "green")
```

---

## References

* [Python3 tkInter](https://docs.python.org/3/library/tk.html)
