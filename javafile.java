import java.io.*;  
import java.nio.file.Files;  
public class FileTypeDemo   
{  
    /* Driver Code */  
    public static void main(String ar[])  
    {  
        /* declaring a File instance with path of the File */  
        File f = new File("C:/Users/WIN 8.1/Desktop/demo.txt");  
        /* If file exists */  
        if(f.exists())   
        {  
            String fType = "Undetermined";  
            String fName = f.getName();  
            String extension = "";  
            int i = fName.lastIndexOf('.');  
  
            if (i > 0)   
            {  
                extension = fName.substring(i + 1);  
            }  
            try   
            {  
                fType= Files.probeContentType(f.toPath());  
            }  
            catch (IOException ioException)   
            {  
                System.out.println("Cannot determine type of file "+ f.getName()+ " due to the exception: "+ ioException);  
            }  
  
            /* Print the file extension. */  
            System.out.println("File Extension used is: " + extension + " and is probably " + fType);  
        }  
        else   
        {  
            System.out.println("File does not exist!");  
        }  
    }  
}  