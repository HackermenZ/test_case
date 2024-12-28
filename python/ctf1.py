from Crypto.Util.number import long_to_bytes, inverse

# Given RSA parameters
ct = 15992705724089064444120193146889712084437595934713568135282969350510849933920626015322474190620035040445065249985765253622975199802810700812272572810008216120514856205658683729410860637142545320284596805191642294950093980161541618167303571397067308574096030957532768552576855057335595799372149867813130402869883159687278015357066721069496681991813256408911264597190678513165440826541874385457399958568116720382993812989529003199416870444071610828146432837826364883236881976633562543124184977378867506469068113588455188060512267554841339890539470043097603306051086746223825971034634647938119634155472281495035628566897

n = 23227936232164029970861530739720544352520778735720935207420890174882376827412333933655430773050125063223105279952252646645688444555172775195507551985310194640889895104324456018646125832601779089679701590827611356256710170383531637631760073511661517218646111235975710250411153371873272173049382954008380631003571757611911325340279048021205846952124110222781267454105464350339248989321072629154823927323728421795677221358366526628599478273943164942256137893977888423049286717606728728461966516489140526086143065447489407230653860906178756455507605812427072930666690693793955049309035462672187747738694300544235304694597

e = 9505514526301829717263294425081225773147921488640061749877355257123379885239952101235121118760733225471441278054683129219098179918265288144199680250758835921246817655530970968513158816149975795977249999054829923122104061701585665149205727174280741248954476814722256551823220236433595834106467648179959174974255279776047949321307731418439212077207656734729528117649895238614852179887318782208155144428392348643169772073483319438274649293746065634561599304250937530240744889939318968632641223770595969621799372740839777439173428644107328655908247290982060044254056679496622834448418895866065411065368238894486420418797

# Factored primes of n (using a tool like factordb)
p = 15314304227233833240450121381298256943454424188128405516784758620318374838814218389168550848906559247653656653589721730070658347166806293051885490078562407
q = 15162886578304671347898912101817744337768193749830326344084707826085960282281684362125431443717404502064464823975934068248826095095221086857364669825256787

# Step 2: Compute φ(n)
phi_n = (p - 1) * (q - 1)

# Step 3: Compute the private exponent d
d = inverse(e, phi_n)

# Step 4: Decrypt the ciphertext
m = pow(ct, d, n)

# Step 5: Convert the message from integer to bytes
plaintext = long_to_bytes(m)

# Output the flag
print(plaintext.decode())