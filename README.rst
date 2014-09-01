==========================================
IS 210: Software Application Programming I
==========================================
-----------
Homework #2
-----------

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Available: 2014-09-08T09:00:00-0400
:Due-Date: 2014-09-15T09:00:00-0400

Overview
========

The following tasks are all Python-related coding tasks related to variable
assignment, numbers, and strings. Use the link provided in the Lesson 02 Course
Materials to access the repository.

If you need a brief refresher on how to get the starter code and save and
submit your work, see the `Workflow Refresher`_ below or skip straight to the
`Instructions`_.

Workflow Refresher
==================

As a brief reminder, to get access to the starter code, you must first *Fork*
the starter repo on `GitHub` and then clone the newly created repository to
your working machine. The link to the starter repository is found in the
Blackboard Lesson 02 Course Materials.

Once you've done this, start Git Bash on your local development workstation.

Virtual Lab (Only)
------------------

If you are using the Virtual Lab, you will need to remind the machine who you
are. Desktop users can skip this step. Virtual Lab users, run the following
commands:

.. code-block:: console

    $ git config user.name "FIRST LAST"
    $ git config user.email "CUNY_SPS_EMAIL"

Where ``FIRST`` and ``LAST`` are your first and last name, respectively and
``CUNY_SPS_EMAIL`` is your spsmail.cuny.edu e-mail address.

Getting the Starter Code
------------------------

.. code-block:: console

    $ git clone HTTPS_CLONE_URL


Where ``HTTPS_CLONE_URL`` is the HTTPS Clone Url found on your *personal* fork
of the starter repo. Please be cautious and check that you're cloning your
repo and not the parent repository. To check, make sure that your username
is in the Clone URL:

    https://github.com/YOUR-USERNAME/is210_lesson_XX.git


Enter the Newly Created Local Repository
----------------------------------------

Use the ``cd`` command to enter the starter repository directory.

.. code-block:: console

    $ cd is210_lesson_XX

Where XX is the lesson number. This will change with each lesson but is found
in the Clone URL as the part after the last slash (``/``) and before ``.git``.

Use ``ls`` to see the available files:

Example:

.. code-block:: console

    $ ls
    LICENSE new_python.py README.rst

Begin Work
----------

You may now begin work. Use whatever editor your prefer to work on and run
your code. You may also use Git Bash to run python files, eg:

.. code-block:: console

    $ python new_python.py
    Some value


Remember, you can call your program with ``python -i`` to start an interpreter
after the program runs. This will let you investigate the value of variables
which will now be accessible from the python interactive command line. This is
a helpful way to debug your work in progress.

Example ``new_python.py``:

.. code-block:: python

    my_var = 'Some value'
    my_new_var = my_var * 2
    print my_new_var

.. code-block:: console

    $ python -i myprogram.py
    Some valueSome value

.. code-block:: pycon

    >>> print my_var
    Some Value
    >>> print my_new_var
    Some valueSome value

You may also launch the IDLE Python editor, the preferred editor of this
course, from Git Bash.

.. code-block:: console

    $ idle new_python.py

This works the same whether you're accessing an existing Python file or want
to create a new Python file called ``new_python.py``.

Saving your Work
----------------

While you are welcome to use any pattern you wish, I recommend saving your
work after each task by issuing a commit and a push to the upstream repository.
Virtual Lab users, especially, take note of this recommendation as the
Virtual Lab long-term storage options are not-yet available and each Virtual
Lab machine is wiped clean each time you log-off.

To save your work, first check what files have changed in your repository.

.. code-block:: console

    $ git status
    On branch master
    Your branch is ahead of 'origin/master' by 3 commits.
      (use "git push" to publish your local commits)

    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)

            modified:   old_python.py

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

            new_python.py

Now add the files you've recently worked on to staging. The ``add`` command
adds changes, not files, so it must be used to add new and existing files
alike.

.. code-block:: console

    $ git add new_python.py old_python.py

Run ``git status`` again to check that the files have been added.

.. code-block:: console

    $ git status
    On branch master
    Your branch is ahead of 'origin/master' by 3 commits.
      (use "git push" to publish your local commits)

    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

            modified:   new_python.py
            modified:   old_python.py

Everything looks good, so commit your changes.

.. code-block:: console

    $ git commit -m "Here's my commit message about what I did."

This saves your work locally. Now lets push it to our remote repository.

.. code-block:: console

    $ git push origin

You may repeat these steps as many times as you need or want.


Instructions
============

The following tasks will either have you interacting with existing files in
the starter repo or creating new ones on the fly. Don't forget to add your
interpreter directive, utf-8 encoding, and a short docstring with any new files
that you create!

.. important::

    In these exercises you may, on occasion, come across a task that requres
    you to research or use a function or method not directly covered by the
    course text. Since Python is such a large language it would be impossible
    for the author to have included descriptions of each and every available
    function which would largely duplicate the offical Python documentation.

    A *vital* skill to successful programming is being comfortable searching
    for and using official language documentation sources like the
    `Python String Documentation`_ page. Throughout our coursework we will be
    practicing both the use of the langugae in practice and the search skills
    necessary to become functional programmers.

Task 01: Reassignment
---------------------

In the reading we learned that strings are immutable, meaning they cannot be
changed. Is the same true for the variables that hold them?

#.  Open ``reassign.py``

#.  After line 8, add another line and try to assign a new value of
    ``Nevermore!`` to the ``RAVEN`` variable.

Task 02: Integer Math
---------------------

Python has an order of operations that respects parentheses. Create a
single-line math statement.

#.  Create a new file ``integer_math.py``

#.  Create a variable called ``WEEKS`` and, in a single statement

    #.  Calculate the remainder of ``19`` divided by ``10``

    #.  Add that to 100

    #.  Add that to 2^8 (do the exponentiation in Python!)

    #.  Divide all of the above by 7

Task 03: String Slicing
-----------------------

Strings are just sequences that can be sliced or repeated with simple
operators.

#.  Open ``lost_in_space .py``

#.  Use the *slice* operator to slice the first 7 characters from the
    ``WILL_ROBINSON`` variable and assign the result into a new variable named
    ``KLAXON``.

#.  Repeat the value of the ``KLAXON`` variable 5 times using the repetition
    operator and save the value *back into* the ``KLAXON`` variable.

Task 04: Split a String
-----------------------

The ``.split()`` method can be used to split a string up according to a
delimiter. By default, this splits a string up on spaces but the delimiter can
be changed to another string.

#.  Open ``artists.py``

#.   After the last line of the file, use the ``.split()`` method to split the
     ``THE_GREAT_QUESTION`` variable on a period+space (``. ``) and assign it
     to a new variable named ``STATEMENTS``.

.. note::

    Notice how ``THE_GREAT_QUESTION`` is assigned? The parentheses tell Python
    this is a multi-line statement. This has the added benefit of automatically
    concatenating our strings. Since the linter would complain if I had a
    single line longer than 80 characters, this is the best way to construct a
    multi-line string in code, though we try to avoid such long strings when
    possible.

Task 05: Slicing a List
-----------------------

Strings and lists are both types of *sequences* which mean they share many
common behaviors. One such behavior is slicing.

#.  With ``artists.py`` still open, slice the new ``STATEMENTS`` returning only
    the first four members into a new variable called ``ARTISTS``


Food for thought: When you slice a list, what object type is returned?

Task 06: Calculating Length
---------------------------

The ``len()`` function is another type of function that has a similar
implication for both strings and lists. Since both are sequences, ``len()``
should count the members.

#.  With ``artists.py`` still open, use ``len()` to determine the length of the
    ``ARTISTS`` list and store the result in a new variable, ``NUM_ARTISTS``.

#.  Now try using ``len()`` to determine the length of the original variable,
    ``THE_GREAT_QUESTION`` and assign it into a new variable, ``CHARACTERS``.

Task 07: Testing Membership
---------------------------

The ``in`` operator is an incredibly useful tool that tests for the membership
of one object in another. It's also usable between both strings and lists.

#.  With ``artists.py`` still open, use the ``in`` operator to test for the
    existence of the string ``Creators`` in the ``THE_GREAT_QUESTION`` variable
    and store the result in a variable named ``HAS_CREATORS``.

#.  Use the ``in`` operator to test for the existence of the ``Splinter``
    string in the ``ARTISTS`` variable. Store the result in a new variable
    named ``HAS_SPLINTER``.

Task 08: Stripping Characters
-----------------------------

The trio of functions ``.lstrip()``, ``.rstrip()``, and ``.strip()`` can be
used to strip unwanted characters from a string. By default they remove
whitespace which includes newlines but they can also strip other character
sequences.

#.  Open ``stripped.py``

#.  Using ``.strip()`` remove the whitespace from both sides of the
    ``NERVOUS_AS`` variable and store the value into the ``NERVOUS_AS``
    variable.

#.  Using ``.rstrip()`` and ``.lstrip()``, remove the commas (``,``) and
    forward slashes (``/``) from the ``NERVOUS_AS`` variable and store the
    value back in the ``NERVOUS_AS`` variable. Do this in a one-line
    statement.

.. note::

    Depending on what a function returns it is often possible to chain together
    multiple function calls as a form of shorthand. This is possible because
    these functions return either the original object or an object of the exact
    same type (eg, a string) so subsequent ``.function()`` calls are operating
    on the return (the object) of prior calls.

Task 09: Multi-line Strings
---------------------------

One way to achieve a multi-line string is to use triple quotes (``"""`` or
``'''``). This is most commonly found in docstrings which are a required part
of every module.

#.  Open ``inquisition.py``

#.  Directly below the coding statement, add a new multi-line docstring that
    describes this module. Traditionally, the first line of a docstring is
    always just one-sentence and usually less than 80 characters. If additional
    documentation is needed, it's followed by an empty line and then more
    descriptions such as listing examples or lists of available attributes.

#.  If you want to test your docstring, make sure you're in the same directory
    as ``inquisition.py`` then try the following commands from the
    Python interactive command line:

    .. code-block:: pycon

        >>> import inquisition  # This loads the module
        >>> help(inquisition)

    Pretty neat, huh? Python's conventions for self-documenting code are one of
    its greatest draws.

.. note::

    While either single-quoted (') or double-quoted (") docstrings are
    acceptable, there is a strong convention towards using double-quoted
    docstrings. Either will pass testing but consistency dictates using one
    type of character for docstrings throughout a project.

    What do the other modules in this repository use in their docstrings?

Task 10: Using Replace
----------------------

``.replace()`` is a helpful, albeit simple, function for replacing parts of a
string. Complex string replacement is best done with the ``re`` module but
``.replace()`` does have a notable edge in speed over the ``re`` module hence
why it still has a role in the greater Python landscape.

#.  Open ``expectation.py``

#.  This file *imports* another module meaning it makes the attributes of
    the imported module available to it. the ``inquisition`` module has a
    constant called ``SPANISH`` which is accessible from the importing module
    as ``inquisition.SPANISH``.

    Use ``.replace()`` to replace all instances of the word ``surprise`` with
    ``haddock`` and assign the result into a new variable called ``FISHY``.

Task 11: Another Way to Replace
-------------------------------

``.replace()`` and ``.re()`` aren't the only way to replace values in a string.
Using a combination of ``.index()``, slicing, ``len()``, and concatenation
you can achieve roughly the same effect.

#.  Copy ``expectation.py`` into a new file, ``flemish.py``.

#.  Open ``flemish.py``

#.  Use a combination of ``.index()``, slicing, ``len()``, simple addition, and
    string concatenation to programmatically replace the first instance of the
    word ``Spanish`` with ``Flemish`` in the ``FISHY`` variable. This will take
    multiple statements and multiple variables. Save the final result string
    into a new variable called ``FLEMISH``

.. hint::

    Start by creating a variable for the string you want to replace
    (``Spanish``), and then calculating its length.

.. hint::

    You can use variables containing integers as values in a slice operation.

.. note::

    While this method may, at first, seem very convoluted there are common
    use-cases for it in functions and loops.

Task 12: Reversing a String
---------------------------

The slice operation has a third parameter known as the *step*, or *stride*. Use
this parameter to reverse a string.

#.  Open ``semordnilap.py``.

#.  Use the third parameter of a slice operation to reverse the order of the
    characters in the ``NAPOLEON`` variable and save the result into a new
    variable named ``REVERSED``.

Task 13: Changing Case
----------------------

Python also has functions to automatically set case. ``.lower()`` and
``.upper()`` are two such examples.

#.  With ``semordnilap.py`` still open, change the case of the ``REVERSED``
    variable to *titlecase* using a single Python string function. Save the
    result in a new variable named ``ENTITLED``.

.. hint::

    Check the official `Python String Documentation`_ page to find the right
    function.

Task 14: Escape Characters
--------------------------

The backslash (``\``) is an escape character. When paired with a following
character, it can be used to create characters not normally allowed in the
string syntax.

#.  Create a new file named ``escapery.py``

#.  Create a variable named ``ESCAPE_STRING`` with the value of
    ``\n'"``

.. note::

    In this case we want the real characters backslash-n, not the escape
    sequence of newline. If you just call the variable by name in the console
    it will print the results without interpreting the characters. Use the
    ``print`` statement to guarantee that the result is properly escaped.

Task 15: Other Numeric Types
----------------------------

Python has several numeric data types in addition to integers.

#.  Create a new file named ``numtypes.py``

#.  Create a float variable named ``FLOATVAR`` and assign it a value of ``0.1``

#.  Create a decimal variable named ``DECIMALVAR`` with its default precision
    and assign it a value of ``0.1``

#.  Create a fraction variable named ``FRACTIONVAR`` and assign it a value of
    one-tenth.

.. hint::

    You'll need to import both the Decimal and Fraction classes from the
    decimal and fractions modules, respectively. Consult the course text or
    official Python documention on how to perform an import.

Food for thought: Do these variables all have the same value?

Task 16: Testing Equality
-------------------------

Just as addition, subtraction, exponentiation are all forms of mathematical
operations and concatenation is a type of string operation, there are a whole
group of operators known as *comparison* operators. Those with prior
programming experience might recognize these operators under a different name
as *tests*.

#.  With ``numtypes.py`` still open, use the equality comparison operator
    (``==``) to test if the ``DECIMALVAR`` variable and ``FRACTIONVAR``
    variable are equal. Store the result in a new variable named
    ``DF_EQUALITY``

#.  Using a single statement, test if the ``DECIMALVAR``, ``FRACTIONVAR``, and
    ``FLOATVAR`` variables are all inequal using the inequality comparison
    operator (``!=``). Store the result in a new variable named
    ``ARE_INEQUAL``.

.. hint::

    If mathematic operators can be chained together as-in Task 03, can you do
    the same with a comparison operator?

Task 17: Other Simple Data Types
--------------------------------

In addition to strings and numbers there are three more major simple data types
that you'll encounter on a regular base, booleans and ``None``. ``None`` is
a very special case that you'll regularly encounter which represents the
absence of data. It's closest equivalent in many other languages is ``Null``.

#.  Create a new file ``simple_types.py``

#.  Create a variable named ``IS_TRUE`` and assign it a value of ``True``

#.  Create a variable named ``IS_FALSE`` and assign it a value of ``False``

#.  Crate a variable named ``IS_NONE`` and assign it a value of ``None``

#.  In a single statement, use the *logical AND* operator (``and``) and the
    equality operator to test if ``IS_TRUE`` is equal to ``1`` and ``IS_FALSE``
    is equal to ``0``. Store the result in a new variable named
    ``INTEGER_EQUIVS``.

Task 18: Data Type Conversion
-----------------------------

The course text mentions that some operations are illegal between objects of
different types. Such operations will raise an error. One of the suggested
illegal operations was attempting to use the addition/concatenation operator to
add an integer to a string. Since that's illegal, how would you combine these
elements?

#.  Open ``conversion.py``

#.  Concatenate the variables ``NOT_THE_QUESTION`` and ``ANSWER`` using the
    string concatenation operator and the ``str()`` function. Store the result
    in a new variable named ``THANKS_FOR_THE_FISH``.

.. note::

    Other languages sometimes call this *casting*. Because Python is an
    implicitly-typed language it's uncommon, though not wholly rare, to see
    this behavior in the wild.

Task 19: Formatting Strings
---------------------------

While concatenation and slicing are certainly acceptable ways to manipulate
strings, the preferred means of injecting data into strings is the
``.format()`` method.

#.  Open ``formatted.py``

#.  Modify the ``NEWS`` variable so that the last formatting string (``{1}``)
    will display its value as a 6 digit number with the appropriate zero
    padding.

#.  Use the ``.format()`` method to format the ``NEWS`` string variable and
    assign the values in the following manner:

    -   ``{friend}`` => ``FNAME``
    -   ``{0}`` => ``NTYPE``
    -   ``{1}`` => ``RNUM``

    Save the result into a new variable named ``EMAIL``.

Task 20: Object Identity
------------------------

Object identity using ``is`` is another form of comparison operation. Unlike
its cousin the equality operator, ``is`` tests if the two things being compared
are the exact same object. In many languages this can be thought of as a strict
comparison operator (``===``). This operator can also be modified by the
``not`` operator to invert the response (eg ``is not``). This is sometimes a
very important distinction as you'll see below.

#.  Open ``identity.py``

#.  Currently, this code is broken. When ``is_empty()`` is passed an empty
    string it throws an error. Because an empty string still has a length
    of zero (0) it should instead report ``True``

#.  Fix the ``is_empty()`` function by changing one operator on one line of
    code so that it only raises an exception only when it's passed a non-sequence
    data type (like an integer) and otherwise correctly reports whether or
    not the passed argument has no length.

.. hint::

    Review Task 17 and the alternate values of booleans

.. hint::

    If you use ``python -i`` to run this code you'll be dropped to an
    interactive command line where you can call ``is_empty()`` and pass it
    any type of data that you want including empty strings (``is_empty('')``), non-empty
    strings (``is_empty('apple')``), and integers (``is_empty(42)``)

.. hint::

    Read the docstrings for both functions to get a sense of what values each
    returns based on a particular set of criteria.

.. important::

    Much of what you see in this file may be new and that's intended. A
    critical skill for programmers of all aptitudes is the ability to
    investigate complex codebases and identify a particular feature or fix that
    is already within the scope of your current skillset. Many codebases are
    so large it is literally impossible for any one person to have a complete
    understanding of the system and in such situations, it is important to have
    the confidence and experience necessary to successfully skim through the
    unnecessary components.

Submission
==========

Code should be submitted to `GitHub`_ by means of opening a pull request.

As-of Lesson 02, each student will have a branch named after his or her
`GitHub`_ username. Pull requests should be made against the branch that
matches your `GitHub`_ username. Pull requests made against other branches will
be closed.  This work flow mimics the steps you took to open a pull request
against the ``pull`` branch in Lesson 01.

For a refresher on how to open a pull request, please see homework instructions
in Lesson 01.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). There will be
automated tests for this assignment to provide early feedback on program code.

When you have completed this assignment, please post the link to your
pull request in the body of the assignment on Blackboard in order to receive
credit.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
