<?php
function coin_flipper(){
    $h = 0;
    $t = 0;

    for($i=0; $i<10000; $i++){
        $rand_num = rand(0,99);

        if($rand_num >= 50){
            $t++;
        }else{
            $h++;
        }
    }
    $string = "Tails " . $t . " Heads " . $h;

    return $string;
}
echo coin_flipper();
?>