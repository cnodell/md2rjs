# md2rjs

md2rjs is a script that quickly and easily creates a node.js presentation from  a markdown file. It does this by creating a reveal.js compatible html file and copying the reveal.js directory. These files are put into a directory named after the original markdown file.

---

## Prerequisites

- python3
- reveal.js

Before using md2rjs you must first download reveal.js. There is no official method for doing this. I just cloned the reveal.js github repository.

---

## Initial Configuration

md2rjs does not know where the reveal.js directory is located on your system or what setting you want reveal.js to use. It doesn't try to guess either. Instead, it will use whatever you specify in "~/.config/md2rjs/md2rjs.conf".

---

### Reveal.js Configuration

This is specified in the 'html_top' and 'html_bottom' sections of the md2rjs.conf file. As md2rjs simply puts your markdown content between the contents of html_top and html_bottom, the resulting html file is the same thing you would get if you had hand crafted it using the reveal.js documentation. Details on how to customize these bits can be found in the reveal.js documentation.

---

#### Themes

Reveal.js comes with a few themes by default. These are located in the reveal.js/css/theme/ directory. To change the theme just change the line ``` <link rel="stylesheet" href="reveal.js/css/theme/black.css" id="theme"> ``` under 'html_top' in md2rjs.conf to specify the desired theme. Once done all presentations will use this new theme.

---

### Sample Config

md2rjs comes with a sample md2rjs.conf file. You should edit it as needed (be sure to verify reveal.js's location) and move it to ~/.config/md2rjs/ (creating the directories if needed).

---

## Separating Slides

md2rjs uses '---' surrounded by empty lines to determine where to separate horizontal slides and '--' surrounded by empty lines to separate vertical slides. This is also configurable by editing the ``` <section data-markdown data-separator="^\n---\n$" data-separator-vertical="^\n--\n$"> ``` line under the 'html_top' section of md2rjs.conf.

I prefer to use just the '---' separator as I seldom need vertical slides and --- is valid markdown (a horizontal rule).

---

### Example of Slide Separation

    ## Slide 1
    
    This slide has slide 2 after it on the right side (--- separator).
    
    ---
    
    ## Slide 2
    
    This slide has Slide 2.2 below it (-- separator), Slide 1 to it's left (before it) and Slide 3 to it's right (after it).
    
    --
    
    ## Slide 2.2
    
    This slide has Slide 2 above it (-- separator), Slide 1 to it's left (before it) and Slide 3 to it's right (after it).
    
    ---
    
    ## Slide 3
    
    This slide has slide 2 to it's left (before it).

---

## Creating a Reveal.js Presentation from a Markdown File

By running:

    $ python md2rjs.py presentation.md

You will get:

    |-sample_presentation
    |---reveal.js
    |---sample.html

---

## Viewing the Presentation

Just open the new html file in your browser of choice.

---

## Quality Warning

This is a quick script with no quality control. It does not try to fail gracefully, verify input or avoid overwriting files.
