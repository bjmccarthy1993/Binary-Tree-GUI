from binary_tree import *
import tkinter
from tkinter import *
import sys
import math
import time

"""
gui.py contains the functions for drawing a GUI to show the features of a Binary Search Tree.

@author Benjamin McCarthy, Josef Bode
@Version 1.0

"""

button_pressed = False

intro_text = "Kia ora! Welcome to Ben and Joey's binary search tree GUI.\n\nGet started by inserting some numbers into the tree."
intro_text += "\nIf you need any help understanding an operation, press the corresponding \"?\" button for an explanation of said operation."

#Function to center the window
def center(win):
    win.update_idletasks()
    
    #Tkinter way to find the screen resolutin
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    width = win.winfo_width()
    height = win.winfo_height()

    #size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = screen_width//2 - (width//2)
    y = screen_height//2 - (height//2)

    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.config(bg="dark slate gray")

    
#Function to move all nodes to the appropriate positions
def move_all(node, direction, scale):
    #Stopping case
    if node == None:
        return
    #For the root, paint it but only shift the subtrees
    if node == tree.root:
        node.painted_object_oval = canvas.create_oval(node.x -20, node.y-20, node.x + 20, node.y+20, outline="black")
        node.painted_object_string = canvas.create_text(node.x, node.y, text=str(node.key))
        
        move_all(tree.root.left, "left", scale/2)
        move_all(tree.root.right, "right", scale/2)
        return

    #Move objects left
    if direction == "left":
        node.x = node.parent.x
        node.x += (-30) * scale
    else:#Move objects right
        node.x = node.parent.x
        node.x += (30) * scale
    #Paint the oval and string and line for the node
    node.painted_object_oval = canvas.create_oval(node.x-20, node.y-20, node.x+20, node.y+20, outline="black")
    node.painted_object_string = canvas.create_text(node.x, node.y, text=str(node.key))
    node.painted_object_line = canvas.create_line(node.x, node.y-20, node.parent.x, node.parent.y+20)
    
    move_all(node.left, "left", scale/2)
    move_all(node.right, "right", scale/2)
    return

    
#Clears all labels and reset any coloured nodes
def clear():
    global tempstring, tempoutline, tempwriting
    search_label.config(text="")
    insert_label.config(text="")
    delete_label.config(text="")
    canvas.delete(tempstring)
    canvas.delete(tempoutline)
    canvas.delete(tempwriting)
    tempstring = -1
    tempoutline = -1
    tempwriting = -1
    

#Function to visualize searching the tree for a node
def search():
    global tempstring, tempoutline, tempwriting, button_pressed

    if button_pressed:
        return

    if tree.root is None:
        information_label.config(text="There is no tree to perform search on, try inserting some values first.")
    
    try:
        search_label.config(text="")
        entry = int(search_entry.get())
        node = tree.search(entry)
        if node == None:
            information_label.config(text= "Searching for " +str(entry) + ".\n\n\n" + str(entry) + " does not exist in the tree.")
            tempwriting = canvas.create_text(20, 20, text=str(entry) + " was not found!", fill="blue", font=("Gill Sans", 24), anchor="nw")
            root.update()
            time.sleep(1)
            clear()
           
        else:
            information_label.config(text= "Searching for " +str(entry) + ".\n\n\n" + str(entry) + " exists in the tree.")
            tempstring = canvas.create_text(node.x, node.y, text=str(node.key), fill="green")
            tempoutline = canvas.create_oval(node.x-20, node.y-20, node.x+20, node.y + 20, outline="green", width=3.0)
            tempwriting = canvas.create_text(20, 20, text="Found " + str(entry) + "!", fill="green", font=("Gill Sans", 24), anchor="nw")
            root.update()
            time.sleep(1)
            clear()
            
    except ValueError:
        search_label.config(fg="red")
        search_label.config(text="Enter an Integer!")
        root.update()
        time.sleep(1)
        clear()

    search_entry.delete(0, "end")


#Function to highlight a node green temporarily
def highlight_node_green(node):
    global tempstring, tempoutline, tempwriting, tempnum

    
    tempstring = canvas.create_text(node.x, node.y, text=str(node.key), fill="green")
    tempoutline = canvas.create_oval(node.x-20, node.y-20, node.x+20, node.y + 20, outline="green", width=3.0)

    root.update()
    time.sleep(1)
    canvas.delete(tempstring)
    canvas.delete(tempoutline)
    canvas.delete(tempwriting)
    canvas.delete(tempnum)
    tempstring = -1
    tempoutline = -1
    tempwriting = -1
    tempnum = -1
    
    
#Traversal methods
def preorder():
    global tempwriting, tempnum, button_pressed
    
    if tree.root == None:
        information_label.config(text="There is no tree to perform preorder traversal on, try inserting some values first.")
        return

    if button_pressed:
        return

    button_pressed = True
    node_list = tree.preorder_node(tree.root)

    node_list_keys = ""
    for node in node_list:
        node_list_keys += str(node.key) + ", "
    temp_traversal_text = canvas.create_text(20, 590, text="Preorder Walk: " + node_list_keys[:-2], fill="blue", font=("PT Sans", 15), anchor="nw")
    information_label.config(text="Preorder traversal works as follows:\n\t1. Visit the root\n\t2. Traverse the left subtree\n\t3. Traverse the right subtree")
    for node in node_list:
        tempwriting = canvas.create_text(20,20, text="Preorder Walk: ", fill="green", font=("PT Sans", 24), anchor="nw")
        tempnum = canvas.create_text(50,50, text=str(node.key), fill="green", font=("PT Sans", 28), anchor="nw")
        highlight_node_green(node)
    canvas.delete(temp_traversal_text)
    clear()
    button_pressed = False
        
def postorder():
    global tempwriting, tempnum, button_pressed
    
    if tree.root == None:
        information_label.config(text="There is no tree to perform postorder traversal on, try inserting some values first.")
        return

    if button_pressed:
        return

    button_pressed = True
    node_list = tree.postorder_node(tree.root)

    node_list_keys = ""
    for node in node_list:
        node_list_keys += str(node.key) + ", "
    temp_traversal_text = canvas.create_text(20, 590, text="Postorder Walk: " + node_list_keys[:-2], fill="blue", font=("PT Sans", 15), anchor="nw")
    information_label.config(text="Postorder traversal works as follows:\n\t1. Traverse the left subtree\n\t2. Traverse the right subtree\n\t3. Visit the root")
    for node in node_list:
        tempwriting = canvas.create_text(20,20, text="Postorder Walk: ", fill="green", font=("Gill Sans", 24), anchor="nw")
        tempnum = canvas.create_text(50,50, text=str(node.key), fill="green", font=("Gill Sans", 28), anchor="nw")
        highlight_node_green(node)
    canvas.delete(temp_traversal_text)

    button_pressed = False

def inorder():
    global tempwriting, tempnum, button_pressed
    
    if tree.root == None:
        information_label.config(text="There is no tree to perform inorder traversal on, try inserting some values first.")
        return

    if button_pressed:
        return

    button_pressed = True
    node_list = tree.inorder_node(tree.root)

    node_list_keys = ""
    for node in node_list:
        node_list_keys += str(node.key) + ", "
    temp_traversal_text = canvas.create_text(20, 590, text="Inorder Walk: " + node_list_keys[:-2], fill="blue", font=("PT Sans", 15), anchor="nw")
    information_label.config(text="Inorder traversal works as follows:\n\t1. Traverse the left subtree\n\t2. Visit the root\n\t3. Traverse the right subtree")
    for node in node_list:
        tempwriting = canvas.create_text(20,20, text="Inorder Walk: ", fill="green", font=("Gill Sans", 24), anchor="nw")
        tempnum = canvas.create_text(50,50, text=str(node.key), fill="green", font=("Gill Sans", 28), anchor="nw")
        highlight_node_green(node)
    canvas.delete(temp_traversal_text)
    button_pressed = False    
    
    

#Function to visualize inserting a node into the tree
def insert():
    global tempstring, tempoutline, tempwriting, button_pressed

    if button_pressed:
        return
    
    try:
        insert_label.config(text="")
        entry = int(insert_entry.get())
        if entry > 999 or entry < -999:
            information_label.config(text="This tree can only handle values between -999 and 999, otherwise the numbers don't fit inside the circles :-(")
            tempwriting = canvas.create_text(20, 20, text="Insert a number between -999 and 999!", fill="blue", font=("Gill Sans", 24), anchor="nw")
            root.update()
            time.sleep(1)
            clear()
            return

        if tree.root is None:
             information_label.config(text="Inserting " + str(entry) + ".\n\n\n"+ str(entry) + " is now the root of the tree.")

        if tree.search_node(tree.root, entry) != None:
            information_label.config(text="Inserting " + str(entry) + ".\n\n\n"+ str(entry) + " is already in the tree - no duplicate values allowed.")
            tempwriting = canvas.create_text(20, 20, text=str(entry) + " is already in the tree!", fill="blue", font=("Gill Sans", 24), anchor="nw")
            root.update()
            time.sleep(1)
            insert_entry.delete(0, "end")
            clear()
            return
        
        node = tree.insert(entry)
        paint_node(node)
        if node.level == 5:
            node = tree.delete(entry)
            deepest_level = tree.search_deepest_level(tree.root)
            fix_up_nodes(tree.root, deepest_level)
            tempwriting = canvas.create_text(20, 20, text="Tree cannot go deeper!", fill="blue", font=("Gill Sans", 24), anchor="nw")
            
            
        else:
            tempwriting = canvas.create_text(20, 20, text="Inserted " + str(entry) + "!", fill="purple", font=("Gill Sans", 24), anchor="nw")
            tempoutline = canvas.create_oval(node.x-20, node.y-20, node.x+20, node.y + 20, outline="purple", width=3.0)
            tempstring = canvas.create_text(node.x, node.y, text=str(entry), fill="purple")
            if node.parent != None:
                side = "right"
                if node == node.parent.left:
                    side = " less than"
                    child_side = " left child "
                if node == node.parent.right:
                    side = " greater than"
                    child_side = " right child "
                information_label.config(text="Inserting " + str(entry) + ".\n\n"+ str(entry) + " is" + side + " it's parent node ( " + str(node.parent.key) +
                                         " )\nThis makes " + str(entry) + " the" + child_side + "of it's parent node.")
                    
        root.update()
        time.sleep(1)
        clear()
    except ValueError:
        information_label.config(text="")
        insert_label.config(fg="red", text="Enter an Integer!")
        root.update()
        time.sleep(1)
        clear()
    insert_entry.delete(0, "end")

#Function to reset the tree to an empty state
def reset():
    global tempoutline, tempstring, tempwriting, y_level, button_pressed

    if button_pressed:
        return

    if tree.root is None:
        information_label.config(text=intro_text)
        return
    
    node_list = tree.preorder_node(tree.root)
    tempwriting = canvas.create_text(20, 20, text="Clearing all!", fill="blue", font=("Gill Sans", 24), anchor="nw")
    for node in node_list:
        canvas.create_text(node.x, node.y, text=str(node.key), fill="red")
        canvas.create_oval(node.x-20, node.y-20, node.x+20, node.y + 20, outline="red", width=3.0)
    
    
    
    if tree.root != None:
        tree.root.left == None
        tree.root.right == None
        tree.root = None

    


    root.update()
    time.sleep(1.5)
    clear()
    canvas.delete("all")
    y_level = 0
    information_label.config(text=intro_text)
    


#Function to delete a node from the tree
def delete():
    global tempstring, tempoutline, tempwriting, button_pressed

    case1 = False
    case2_left = False
    case2_right = False
    case3 = False

    if button_pressed:
        return

    if tree.root is None:
        information_label.config(text="There is no tree to perform delete on, try inserting some values first.")
    
    try:
        delete_label.config(text="")
        entry = int(delete_entry.get())
        node = tree.search(entry)

        if node == None:
            information_label.config(text="Tried to delete " + str(entry) + ", but this value does not exist in the tree.")
            tempwriting = canvas.create_text(20, 20, text=str(entry) + " doesn't exist!", fill="red", font=("Gill Sans", 24), anchor="nw")
            root.update()
            time.sleep(1)
            clear()
        else:
           
            #Code to determine which deletion case we are in
            if node.left == None and node.right == None:
                case1 = True
            elif node.left == None:
                case2_right = True
                child_node_key = str(node.right.key)
            elif node.right == None:
                case2_left = True
                child_node_key = str(node.left.key)
            else:
                case3 = True
                successor = str(tree.successor(node).key)
                successor_node = tree.successor(node)

            
            case = ""
            if case1 == True:
                case = "Case 1:  '" + str(node.key) + "' has no children.\nSimply remove it from the tree."
            elif case2_right == True:
                case = "Case 2:  '" + str(node.key) + "' has one child on the right.\nSimply replace '" + str(node.key) + "' with '"
                case += child_node_key + "' and everything below it."
            elif case2_left == True:
                case = "Case 2:  '" + str(node.key) + "' has one child on the left.\nSimply replace '" + str(node.key) + "' with '"
                case += child_node_key + "' and everything below it."
            else:
                case = "Case 3:  '" + str(node.key) + "' has two children.\nCopy in the key from it's successor ( " + successor
                case += " ) then recursively delete it's successor's node from the tree."

            #Code to highlight the deleted node red
            information_label.config(text="Deleting " + str(entry) + ".\n\n"+ case)
            #information_label.config(text=case)
            tempstring = canvas.create_text(node.x, node.y, text=str(node.key), fill="red")
            tempoutline = canvas.create_oval(node.x-20, node.y-20, node.x+20, node.y + 20, outline="red", width=3.0)
            tempwriting = canvas.create_text(20, 20, text="Deleting " + str(entry) + "!", fill="red", font=("Gill Sans", 24), anchor="nw")
            if case3 == True:
                tempstring_successor = canvas.create_text(successor_node.x, successor_node.y, text=successor, fill="blue")
                tempoutline_successor = canvas.create_oval(successor_node.x-20, successor_node.y-20, successor_node.x+20, successor_node.y + 20, outline="blue", width=3.0)
           
            
            root.update()
            time.sleep(2)
            canvas.delete(tempstring)
            canvas.delete(tempoutline)
            canvas.delete(tempwriting)
            
            
            tempstring = -1
            tempoutline = -1
            tempwriting = -1
            if case3 == True:
                canvas.delete(tempstring_successor)
                canvas.delete(tempoutline_successor)
                tempstring_successor = -1
                tempoutline_successor = -1
            
            node = tree.delete(entry)
            deepest_level = tree.search_deepest_level(tree.root)
            fix_up_nodes(tree.root, deepest_level)
            root.update()
            time.sleep(1)
            clear()

    except ValueError:
        delete_label.config(text="Enter an Integer!")
        root.update()
        time.sleep(1)
        clear()
    delete_entry.delete(0, "end")

#Function to redo all the node paintings upon deletion
def fix_up_nodes(node, deepest_level):
    global y_level
    
    fix_y(node)
    canvas.delete("all")
    y_level = deepest_level
    move_all(tree.root, "Don't move", 2**(deepest_level))

#Function to fix the Y values of all nodes when a node is deleted
def fix_y(node):
    if node != None:
        level = 0
        y = 50
        #Calculate the y depth for this node
        while level != node.level:
            y += 50 * (level + 1)
            level += 1
        node.y = y
        fix_y(node.left)
        fix_y(node.right)
    

#Paint function - to get all nodes at this point in
#time and put them on the canvas
def paint_node(node):
    global y_level, r_paint, l_paint
    
    x1 = 625 - 20
    x2 = 625 + 20
    y1 = 30
    y2 = 70
    y = 50
    
    level = 0
                           
    if node == None:
        return
    elif node.level == 0:
        node.x = 540
        node.y = 50
        node.painted_object_oval = canvas.create_oval(node.x-20, node.y-20, node.x+20, node.y+20, outline="black")
        node.painted_object_string = canvas.create_text(node.x, node.y, text=str(node.key))
    else:
        #Calculate the y depth for this node
        while level != node.level:
            y += 50 * (level + 1)
            level += 1
        #Calculate the node's x position based upon its parents x position     
        if node == node.parent.left:
            node.x = node.parent.x - 30
        else:
            node.x = node.parent.x + 30
            
        node.y = y
                           
        #Check to see if a new y-depth has been met
        if node.level > y_level:
            #Set the new depth
            y_level = node.level
            
        #Add the painted_objects to the nodes
        canvas.delete("all")
        move_all(tree.root, "Don't move", 2**(y_level))
        #node.painted_object_oval = (canvas.create_oval(node.x-20, node.y-20, node.x+20, node.y+20, outline="black"))
        #node.painted_object_string = (canvas.create_text(node.x, node.y, text=str(node.key)))

    return

#These 3 functions below are used with the "help" buttons
def search_help():
    information_label.config(text="Searching through a BST:\n\t1. Start from the root\n\t2. Compare the given element with the root value, if it is less than the root, then recurse for left, else recurse for right\n\t3. If the element to search is found, return true, else return false")

    
def insert_help():
    information_label.config(text="Inserting into a BST:\n\t1. Start from the root\n\t2. Compare the inserting element with the root value, if it is less than the root, then recurse for left, else recurse for right\n\t3. After reaching the end, if the inserting element is less than the current node value, insert at left, else insert at right")

    
def delete_help():
    information_label.config(text="When deleting from a BST, 3 possibilites arise:\n\t1. Node to be deleted is a leaf -- simply remove this node from the tree\n\t2. Node to be deleted has only one child -- link the node's parent to the child and vice-versa, then delete the node\n\t3. Node to be deleted has two children -- find and copy the successor to the node and delete the successor (Note: predecessor can also be used)")
    
    

root = Tk()
root.title("Binary Search Tree")


#Frames
left_frame = Frame(bg="light slate gray", bd=4, relief=RAISED)
left_frame.grid(column=0, row=0, padx=(20,0), pady=10)

draw_frame = Frame(height=610,width=1240, bg="dark slate gray")
draw_frame.grid(column=1,row=0)

info_frame = Frame(bg="snow")
info_frame.grid(columnspan=2)

#Used this frame to pad the bottom a wee bit
bottom_frame = Frame(bg="dark slate gray",height=15)
bottom_frame.grid(columnspan=2)

#Canvas
canvas = Canvas(draw_frame, height=610, width=1240, bg="snow", highlightbackground="dark slate gray",relief=SUNKEN, bd=6)
canvas.pack(padx=20,pady=(10,20))
canvas.pack_propagate(0)

#Labels, text entry, and buttons
operations_label = Label(left_frame, fg="black", bg ="light slate gray", text="Operations:", font=("PT Sans", 18))
operations_label.grid(row=0, padx=10, pady=(20,0))

search_label = Label(left_frame, fg="red", bg ="light slate gray")
search_label.grid(columnspan=2,row=1, padx=10)
search_entry = Entry(left_frame, width=16,  highlightbackground="light slate gray", justify=CENTER)
search_entry.grid(columnspan=2,row=2, padx=10)
search_button = Button(left_frame, text="Search", fg="black", bg ="light slate gray", command=search, highlightbackground="light slate gray", width=9)
search_button.grid(column=0,row=3, padx=(8,0),pady=(0,10))
search_help_button = Button(left_frame, text="?", fg="black", bg ="light slate gray", highlightbackground="light slate gray", command=search_help)
search_help_button.grid(column=1,row=3, padx=(0,10), pady=(0,10))


insert_label = Label(left_frame, fg="red", bg ="light slate gray")
insert_label.grid(columnspan=2,row=4, padx=10)
insert_entry = Entry(left_frame, width=16, highlightbackground="light slate gray", justify=CENTER)
insert_entry.grid(columnspan=2,row=5, padx=10)
insert_button = Button(left_frame, text="Insert", fg="black", bg ="light slate gray", command=insert, highlightbackground="light slate gray", width=9)
insert_button.grid(column=0,row=6, padx=(8,0),pady=(0,10))
insert_help_button = Button(left_frame, text="?", fg="black", bg ="light slate gray", highlightbackground="light slate gray", command=insert_help)
insert_help_button.grid(column=1,row=6, padx=(0,10), pady=(0,10))


delete_label = Label(left_frame, fg="red", bg ="light slate gray")
delete_label.grid(columnspan=2,row=7, padx=10)
delete_entry = Entry(left_frame, width=16, highlightbackground="light slate gray", justify=CENTER)
delete_entry.grid(columnspan=2,row=8, padx=10)
delete_button = Button(left_frame, text="Delete", fg="black", bg ="light slate gray", command=delete, highlightbackground="light slate gray", width=9)
delete_button.grid(column=0,row=9, padx=(8,0), pady=(0,10))
delete_help_button = Button(left_frame, text="?", fg="black", bg ="light slate gray", highlightbackground="light slate gray", command=delete_help)
delete_help_button.grid(column=1,row=9, padx=(0,10), pady=(0,10))

traversals_label = Label(left_frame, fg="black", bg ="light slate gray", text="Traversals:", font=("PT Sans", 18))
traversals_label.grid(row=10, pady=(40,5))
preorder_button = Button(left_frame, text="Preorder", fg="black", bg ="light slate gray",
                         highlightbackground="light slate gray",command=preorder, width=14)
preorder_button.grid(columnspan=2, row=11, padx=10)
inorder_button = Button(left_frame, text="Inorder", fg="black", bg ="light slate gray",
                        highlightbackground="light slate gray",command=inorder, width=14)
inorder_button.grid(columnspan=2,padx=10, row=12, pady=5)
postorder_button = Button(left_frame, text="Postorder", fg="black", bg ="light slate gray",
                          highlightbackground="light slate gray",command=postorder, width=14)
postorder_button.grid(columnspan=2, row=13, padx=10, pady=(0,60))

clear_button = Button(left_frame, text="Reset", fg="black", bg ="light slate gray", highlightbackground="light slate gray", command=reset, width=12)
clear_button.grid(columnspan=2, row=14, padx=10, pady=(0,20))

information_label = Label(info_frame, bg="snow", relief=RIDGE, bd=4, justify=LEFT, anchor=NW, width=130, height=4,
                          font=("PT Sans Caption", 16), padx=10,pady=10)
information_label.config(text=intro_text)
information_label.pack()
information_label.pack_propagate(0)


#Binary Tree data structure
tree = BST()

#Function to paint
paint_node(tree.root)

#Other needed variables
y_level = 0
tempstring = -1
tempoutline = -1
tempwriting = -1
tempnum = -1
helper_node = None
center(root)

root.resizable(0, 0)

root.mainloop()
