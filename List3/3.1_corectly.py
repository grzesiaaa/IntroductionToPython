def histogram(t):

    s = dict()

    for i in t:
        if i != " ":
            if i not in s:
                s[i] = 1
            else:
                s[i] += 1

    y = sorted(s, key = s.get, reverse = True)

    for k in y[0:10]:
        print(k +': '+'*'*(int(s[k]/10)))
        
t = t = '''The strange history of this book/
In January 1999 I was preparing to teach an introductory programming class in Java. I had/
taught it three times and I was getting frustrated. The failure rate in the class was too high/
and, even for students who succeeded, the overall level of achievement was too low.
One of the problems I saw was the books. They were too big, with too much unnecessary
detail about Java, and not enough high-level guidance about how to program. And they all
suffered from the trap door effect: they would start out easy, proceed gradually, and then
somewhere around Chapter 5 the bottom would fall out. The students would get too much
new material, too fast, and I would spend the rest of the semester picking up the pieces.
Two weeks before the first day of classes, I decided to write my own book. My goals were:
• Keep it short. It is better for students to read 10 pages than not read 50 pages.
• Be careful with vocabulary. I tried to minimize the jargon and define each term at
first use.
• Build gradually. To avoid trap doors, I took the most difficult topics and split them
into a series of small steps.
• Focus on programming, not the programming language. I included the minimum
useful subset of Java and left out the rest.
I needed a title, so on a whim I chose How to Think Like a Computer Scientist.
My first version was rough, but it worked. Students did the reading, and they understood
enough that I could spend class time on the hard topics, the interesting topics and (most
important) letting the students practice.
I released the book under the GNU Free Documentation License, which allows users to
copy, modify, and distribute the book.
What happened next is the cool part. Jeff Elkner, a high school teacher in Virginia, adopted
my book and translated it into Python. He sent me a copy of his translation, and I had the
unusual experience of learning Python by reading my own book. As Green Tea Press, I
published the first Python version in 2001.
In 2003 I started teaching at Olin College and I got to teach Python for the first time. The
contrast with Java was striking. Students struggled less, learned more, worked on more
interesting projects, and generally had a lot more fun.
vi Chapter 0. Preface
Over the last nine years I continued to develop the book, correcting errors, improving some
of the examples and adding material, especially exercises.
The result is this book, now with the less grandiose title Think Python. Some of the changes
are:
• I added a section about debugging at the end of each chapter. These sections present
general techniques for finding and avoiding bugs, and warnings about Python pitfalls.
• I added more exercises, ranging from short tests of understanding to a few substantial
projects. And I wrote solutions for most of them.
• I added a series of case studies—longer examples with exercises, solutions, and
discussion. Some are based on Swampy, a suite of Python programs I wrote for
use in my classes. Swampy, code examples, and some solutions are available from
http://thinkpython.com.
• I expanded the discussion of program development plans and basic design patterns.
• I added appendices about debugging, analysis of algorithms, and UML diagrams
with Lumpy.
I hope you enjoy working with this book, and that it helps you learn to program and think,
at least a little bit, like a computer scientist.
Allen B. Downey
Needham MA
Allen Downey is a Professor of Computer Science at the Franklin W. Olin College of Engineering.
Acknowledgments
Many thanks to Jeff Elkner, who translated my Java book into Python, which got this
project started and introduced me to what has turned out to be my favorite language.
Thanks also to Chris Meyers, who contributed several sections to How to Think Like a Computer Scientist.
Thanks to the Free Software Foundation for developing the GNU Free Documentation License, which helped make my collaboration with Jeff and Chris possible, and Creative
Commons for the license I am using now.
Thanks to the editors at Lulu who worked on How to Think Like a Computer Scientist.
Thanks to all the students who worked with earlier versions of this book and all the contributors (listed below) who sent in corrections and suggestions.
vii
Contributor List
More than 100 sharp-eyed and thoughtful readers have sent in suggestions and corrections
over the past few years. Their contributions, and enthusiasm for this project, have been a
huge help.
If you have a suggestion or correction, please send email to feedback@thinkpython.com.
If I make a change based on your feedback, I will add you to the contributor list (unless
you ask to be omitted).
If you include at least part of the sentence the error appears in, that makes it easy for me to
search. Page and section numbers are fine, too, but not quite as easy to work with. Thanks!
• Lloyd Hugh Allen sent in a correction to Section 8.4.
• Yvon Boulianne sent in a correction of a semantic error in Chapter 5.
• Fred Bremmer submitted a correction in Section 2.1.
• Jonah Cohen wrote the Perl scripts to convert the LaTeX source for this book into beautiful
HTML.
• Michael Conlon sent in a grammar correction in Chapter 2 and an improvement in style in
Chapter 1, and he initiated discussion on the technical aspects of interpreters.
• Benoit Girard sent in a correction to a humorous mistake in Section 5.6.
• Courtney Gleason and Katherine Smith wrote horsebet.py, which was used as a case study
in an earlier version of the book. Their program can now be found on the website.
• Lee Harr submitted more corrections than we have room to list here, and indeed he should be
listed as one of the principal editors of the text.
• James Kaylin is a student using the text. He has submitted numerous corrections.
• David Kershaw fixed the broken catTwice function in Section 3.10.
• Eddie Lam has sent in numerous corrections to Chapters 1, 2, and 3. He also fixed the Makefile
so that it creates an index the first time it is run and helped us set up a versioning scheme.
• Man-Yong Lee sent in a correction to the example code in Section 2.4.
• David Mayo pointed out that the word “unconsciously" in Chapter 1 needed to be changed to
“subconsciously".
• Chris McAloon sent in several corrections to Sections 3.9 and 3.10.
• Matthew J. Moelter has been a long-time contributor who sent in numerous corrections and
suggestions to the book.
• Simon Dicon Montford reported a missing function definition and several typos in Chapter 3.
He also found errors in the increment function in Chapter 13.
• John Ouzts corrected the definition of “return value" in Chapter 3.
• Kevin Parks sent in valuable comments and suggestions as to how to improve the distribution
of the book.
• David Pool sent in a typo in the glossary of Chapter 1, as well as kind words of encouragement.
• Michael Schmitt sent in a correction to the chapter on files and exceptions.'''
print(histogram(t))            
