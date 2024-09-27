from application import *

##  Create Application  ##
main = Application()
main.InitializeButtons()

## Label ##
output_var = tkinter.StringVar()
output_var.set("")

output = tkinter.Label(
    main.root, fg="white", bg="black",
    font=("fixedsys", 17), highlightthickness=0, 
    bd=0, width=15, textvariable=output_var
)
output.grid(row=1, column=2, padx=5, pady=5, sticky="NSEW")
main.widgets["Output"] = output_var

main.root.mainloop()