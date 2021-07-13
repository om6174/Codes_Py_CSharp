using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using WebApplication2.Models;

namespace WebApplication2.Controllers
{
    public class StudentController : Controller
    {
        public IActionResult Index()
        {

            List<StudentModel> students = new List<StudentModel>();
            JSONReadWrite readWrite = new JSONReadWrite();
            try
            {
                students = JsonConvert.DeserializeObject<List<StudentModel>>(readWrite.Read("students.json", "data"));
            }
            catch
            {
                ModelState.AddModelError("Error", "Something went wrong while reading the json file!!");

            }
            return View(students);


        }



        [HttpPost]
        public IActionResult Index(StudentModel studentModel)
        {
            List<StudentModel> students = new List<StudentModel>();
            JSONReadWrite readWrite = new JSONReadWrite();
            students = JsonConvert.DeserializeObject<List<StudentModel>>(readWrite.Read("students.json", "data"));
            if (studentModel.RollNumber <= 0)
            {
                ModelState.AddModelError("Error", "Roll Number should be a number greater than 0");
            }
            else if(studentModel.Age <= 0)
            {
                ModelState.AddModelError("Error", "Age should be a number greater than 0");
            }
            else if(String.IsNullOrWhiteSpace(studentModel.Name))
            {
                ModelState.AddModelError("Error", "Name should not be blank");
            }
            else if(String.IsNullOrWhiteSpace(studentModel.Gender))
            {
                ModelState.AddModelError("Error", "Gender should not be blank");
            }
            else
            {
                StudentModel student = students.FirstOrDefault(x => x.RollNumber == studentModel.RollNumber);
                if (student == null)
                {
                    students.Add(studentModel);
                }
                else
                {
                    int index = students.FindIndex(x => x.RollNumber == studentModel.RollNumber);
                    students[index] = studentModel;
                }
                string jSONString = JsonConvert.SerializeObject(students);
                readWrite.Write("students.json", "data", jSONString);
            }
            return View(students);
        }

        [HttpPost]
        public ActionResult SearchAct(int numToFind, string nameToFind)
        {
            //List<StudentModel> students = new List<StudentModel>();
            JSONReadWrite readWrite = new JSONReadWrite();
            List<StudentModel> students = JsonConvert.DeserializeObject<List<StudentModel>>(readWrite.Read("students.json", "data"));

            ViewBag.SearchKey = numToFind;
            ViewBag.SearchName = nameToFind;
            return View("Index",students);
        }

        [HttpPost]
        public IActionResult Delete(int RollNumber)
        {

            List<StudentModel> students = new List<StudentModel>();
            JSONReadWrite readWrite = new JSONReadWrite();
            try 
            {
                students = JsonConvert.DeserializeObject<List<StudentModel>>(readWrite.Read("students.json", "data"));
                int index = students.FindIndex(x => x.RollNumber == RollNumber);
                if (index != -1)
                {
                    students.RemoveAt(index);
                    string jSONString = JsonConvert.SerializeObject(students);
                    readWrite.Write("students.json", "data", jSONString);
                    ModelState.AddModelError("Delete", "Data deleted successfully!!");
                }
                else
                    ModelState.AddModelError("Delete", "Roll number not found!");
            }
            catch
            {
                ModelState.AddModelError("Error", "Something went wrong");
            }
            

            return View("Index", students);
        }




    }



    public class JSONReadWrite
    {
        public JSONReadWrite() { }

        public string Read(string fileName, string location)
        {
            string root = "wwwroot";
            var path = Path.Combine(
            Directory.GetCurrentDirectory(),
            root,
            location,
            fileName);

            string jsonResult;

            using (StreamReader streamReader = new StreamReader(path))
            {
                jsonResult = streamReader.ReadToEnd();
            }
            return jsonResult;
        }

        public void Write(string fileName, string location, string jSONString)
        {
            string root = "wwwroot";
            var path = Path.Combine(
            Directory.GetCurrentDirectory(),
            root,
            location,
            fileName);

            using (var streamWriter = File.CreateText(path))
            {
                streamWriter.Write(jSONString);
            }
        }
    }


}
