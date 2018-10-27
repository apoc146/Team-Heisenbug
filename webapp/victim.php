<?php
if(isset($_POST["submit"])){
    $check = getimagesize($_FILES["myimage"]["name"]);
    if($check !== false){
        $image = $_FILES['myimage']['name'];
       // echo file_get_contents($image);
        $imgContent = addslashes(file_get_contents($image));

        /*
         * Insert image data into database
         */
        
        //DB details
        $dbHost     = 'localhost';
        $dbUsername = 'root';
        $dbPassword = '';
        $dbName     = 'codefundo';
        
        //Create connection and select DB
        $db = new mysqli($dbHost, $dbUsername, $dbPassword, $dbName);
        
        // Check connection
        if($db->connect_error){
            die("Connection failed: " . $db->connect_error);
        }
        
        //$dataTime = date("Y-m-d H:i:s");
        
        //Insert image content into database
        $insert = $db->query("INSERT into table (Name,Blood Group,Medical History,Identification Mark,Emergency Contact,Allergies,Image) VALUES ('".$_POST["name"]."','".$_POST["bg"]."','".$_POST["medhis"]."','".$_POST["identmark"]."','".$_POST["emercont"]."','".$_POST["aller"]."','$imgContent')");
        
        if($insert){
            echo "File uploaded successfully.";
        }else{
            echo "File upload failed, please try again.";
        } 
    }
    else{
        echo "Please select an image file to upload.";
    }
}
?>