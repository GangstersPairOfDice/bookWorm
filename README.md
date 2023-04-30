# bookWorm

This project aims at finding new and innovative ways to read books.

The main idea is to help reduce eye-stress from reading by creating a system which allows a more natural flow for receiving information from text.

The first idea being developed is to make a sort of space-filling curve from text, so that one may continue reading without having to restart from a new line.

Example:

This is my very own custom                              >───────────\
example sentence that is meant          ->         >───────────\
to be read "normally".                                         >───────────

<br />

This is my very own custom                              >───────────┐\
meant is that sentence example           ->          ┌──────────┘\
to be read in a "new" way.                                   └───────────

<br />

Hence the name bookWorm.

<br />

**Usage:**

Program has one function with two parameters, *text* and *n*:
>bookWorm(text, n)

The *text* parameter is where you enter your string.
The *n* parameter is used to specify how many columns (using the amount of spaces between words in your text) you want before it switches to the next row.

**toDo:**
 - Add support for punctuation
 - Implement user-friendly react website
 - Host
