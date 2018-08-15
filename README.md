# sony-remote-shutter-on-wifi
Piece of python software for camera remote trigger
we are write for sony rx100m2  but I think, it work to other sony cameras.

we examined,sony camera api and ruby applications for remote shutter and we wanted to write a simple code.
By the way, for the first time in github I added something and i think that there are deficiencies.I am delighted
,if you help me fix my mistakes and deficiencies.
It's just trigger the camera.We use it this on linux autopilot terminal (emlid-navio2)
firstly press the menü and  go to Ctrl with smartphone options.
now you connect to the camera from the device you want to control
after run this program and take a picture continiously
do not forget to modify the while() loop

Otopilot içerisinden,multishot kablo bulamadığım için,tetikleme yapmak istediğim için bu program parçasını yazıp kendi otopilotuma entegre ettim 
normalde bu parça mavproxy içerisinde çalışmakta,benim için kendi başına pek bir işe yaramıyor.Sony rx100 m2 kamera için  araştırma yaptığımda bulduğum 
apiden ve örnek bir ruby projesinden faydalandığım bir kod parçası oldu(bulunca ekleyeceğim) Bu arada github a ilk defa bir şey eklediğim için 
ölümcül derece eksikleri olacağını tahmın ediyorum.Hatalarımı ve eksiklerimi düzeltmemde yardımcı olursanız sevinirim.Normalde apiden kendiniz için 
istediğiniz gibi yapıp çalıştırabiliyorsunuz kendi araştırmamda sony rx100m2 için destek olmadığını okudum sonrasında  telefon uygulamasından ulaşınca 
temel komutları yapabildiğini gördüm bende sadece işime yarıyacak parçayı aldım.
kodu çalıştırmadan önce kameradan akıllı telefonla kontrol seceneğine gelip karşınıza çıkan wifi şifresini kontrol etmek istediğiniz makinaya yazıp bağlanın
bağlantı sağlanınca kameraya normal şekilde ulaşamayacaksınız,daha sonra bu program parçasını çalıştırın fotograf makinasi sürekli olarak fotograf 
cekmeye başlayacaktır.

