# Delim
Python code that will search files depending on file type (nc1, pdf, xml, .Xml)
So lets start from the begining, I am a Robotics programmer/ processing equipment programmer ( Plate-table, Beamline, Robotic Coper and Angle Master) 
therefore i receive 1000's of files, ranging from .nc1, .nc, .xml, .Xml, for the programming that i do.
         
We work with a detailing company/companies that create structural steel models using "Tekla Structures"
The project is massive, so it is broken down into phases and mods, so the first package that was sent had 900 files, and each of these files were 
25 characters long, excluding the .nc1..etc

So I tested this import and "Nested" the plate nc1 files (235 plate nc1 files) into a Raw Plate that measured 8 feet by 24 feet, the amount of time it 
would consume marking all 25 chararcters onto each piece mark was 11 hrs, so this was unacceptable, I then started doing some research on how to write code
to modify .nc1 files and stumbled upon "ChatGPT" don't hate me to much for this guys, im still learning and had to get some answers some how lol 

so with the help of Chat Gpt and one of my co-workers, Justyn, we created this code, that i called Delim, because it removes characters from the files
that i chose.

So i ran this Python code and it work! it removed 10 digits from the file name and cut my plate program time in half! 5.5hrs 
