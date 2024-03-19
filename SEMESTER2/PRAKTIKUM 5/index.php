<?php
 class manusia{
    public $nama;
    public $umur;
    // protected
    // private

    public function setNama($nama){
        $this->nama = $nama;
    }
    public function setUmur($umur){
        $this->umur = $umur;
    }
    public function getinfo(){
        return "nama: " . $this ->nama . " umur: ". $this->umur;
    }
}

// membuat objek
$aming = new manusia();
$aming->setNama("Aming");
$aming->setUmur("19");
echo $aming->getinfo();

echo '<br>';

$alek = new manusia();
$alek->setNama("Alek");
$alek->setUmur("90");
echo $alek->getinfo();


?>
