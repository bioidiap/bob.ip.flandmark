==============================
 Python Bindings to flandmark
==============================

This package is a simple Boost.Python wrapper to the (rather quick) open-source
facial landmark detector `flandmark
<http://cmp.felk.cvut.cz/~uricamic/flandmark/index.php>`_. If you use this
package, the author asks you to cite the following paper::

  @InProceedings{Uricar-Franc-Hlavac-VISAPP-2012,
    author =      {U{\\v{r}}i{\\v{c}}{\\'{a}}{\\v{r}}, Michal and Franc, Vojt{\\v{e}}ch and Hlav{\\'{a}}{\\v{c}}, V{\\'{a}}clav},
    title =       {Detector of Facial Landmarks Learned by the Structured Output {SVM}},
    year =        {2012},
    pages =       {547-556},
    booktitle =   {VISAPP '12: Proceedings of the 7th International Conference on Computer Vision Theory and Applications},
    editor =      {Csurka, Gabriela and Braz, Jos{\'{e}}},
    publisher =   {SciTePress --- Science and Technology Publications},
    address =     {Portugal},
    volume =      {1},
    isbn =        {978-989-8565-03-7},
    book_pages =  {747},
    month =       {February},
    day =         {24-26},
    venue =       {Rome, Italy},
    keywords =    {Facial Landmark Detection, Structured Output Classification, Support Vector Machines, Deformable Part Models},
    prestige =    {important},
    authorship =  {50-40-10},
    status =      {published},
    project =     {FP7-ICT-247525 HUMAVIPS, PERG04-GA-2008-239455 SEMISOL, 
      Czech Ministry of Education project 1M0567},
    www = {http://www.visapp.visigrapp.org},
  }

Installation
------------

To install these bindings, you will need the open-source library `Bob
<http://www.idiap.ch/software/bob/>`_ installed somewhere. At least version 1.1
of Bob is required. If you have compiled Bob yourself and installed it on a
non-standard location, you will need to note down the path leading to the root
of that installation.

Just type::

  $ python bootstrap.py
  $ ./bin/buildout

If Bob is installed in a non-standard location, edit the file ``buildout.cfg``
to set the root to Bob's local installation path. Remember to use the **same
python interpreter** that was used to compile Bob, then execute the same steps
as above.

Usage
-----

Pretty simple, just do something like::

  import bob
  import flandmark

  video = bob.io.VideoReader('myvideo.avi')
  localize = flandmark.Localizer()

  for frame in video:
    print localize(frame)
