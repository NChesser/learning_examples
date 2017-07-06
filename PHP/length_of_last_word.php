<?php
function length_of_last_word($sentence){
  
  $words = explode(' ', $sentence);
  
  return strlen(substr($sentence, strrpos($sentence, ' ') + 1));
}

print_r(length_of_last_word("My Name is Nick"));
?>