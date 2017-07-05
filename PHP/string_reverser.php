<?php
$string = "Nick Chesser is really cool!";

function utf8_reverse($str){
    preg_match_all('/./us', $str, $array);
    return join('',array_reverse($array[0]));
}

print utf8_reverse($string);
?>
