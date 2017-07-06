<?php
function is_Power($x, $y)  
{  
    $final = $x; 
    while ($x % $y == 0){  
       $x = $x / $y;  
    }  
         
    if($x == 1){  
        print "$final is power of $y";  
    }  
    else{  
        print "$final is not power of $y";  
    }      
}  
is_Power(16,2);
?>
