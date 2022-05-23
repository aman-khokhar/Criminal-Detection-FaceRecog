-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 11, 2021 at 12:34 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `criminaldetection`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `a_id` int(11) NOT NULL,
  `a_name` varchar(30) NOT NULL,
  `a_pass` varchar(20) NOT NULL,
  `a_email` varchar(30) NOT NULL,
  `a_contact` int(11) NOT NULL,
  `a_post` varchar(30) NOT NULL,
  `a_recovery_code` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`a_id`, `a_name`, `a_pass`, `a_email`, `a_contact`, `a_post`, `a_recovery_code`) VALUES
(1, 'kuvadiya tushar j.', 'tushar', 'kuvadiyatushar2001@gmail.com', 826482136, '', 826482),
(2, 'khokhar aman', 'aman@123', 'khokharaman123@gmail.com', 989885973, 'head', 0),
(3, 'sarvik', 'sarvik@123', 'sarvik@gmail.com', 2147483647, 'sub officer', 2054492051),
(4, 'chandra parmar', 'chandra@123', 'chandraparmar@gmail.com', 2147483647, 'sub officer', 2053992028);

-- --------------------------------------------------------

--
-- Table structure for table `criminal`
--

CREATE TABLE `criminal` (
  `c_id` int(11) NOT NULL,
  `c_photo` longblob NOT NULL,
  `c_encode_photo` text NOT NULL,
  `c_fname` varchar(20) NOT NULL,
  `c_mname` varchar(20) NOT NULL,
  `c_lname` varchar(20) NOT NULL,
  `c_nickname` varchar(20) NOT NULL,
  `c_home_address` varchar(40) NOT NULL,
  `crime_record` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `criminal`
--

INSERT INTO `criminal` (`c_id`, `c_photo`, `c_encode_photo`, `c_fname`, `c_mname`, `c_lname`, `c_nickname`, `c_home_address`, `crime_record`) VALUES
(1, '', '-0.17656449973583221, 0.09994138777256012, 0.07135594636201859, -0.07312238216400146, -0.06584829092025757, -0.014450689777731895, -0.07555405795574188, 0.02640625648200512, 0.1580771803855896, -0.02752356231212616, 0.17553667724132538, -0.0151483453810215, -0.2196948230266571, -0.1223343014717102, -0.029223697260022163, 0.07661822438240051, -0.13813379406929016, -0.0792190283536911, -0.08312710374593735, -0.0797305554151535, 0.10899758338928223, 0.0758451521396637, 0.0054831961169838905, 0.017250705510377884, -0.17103050649166107, -0.37043946981430054, -0.09482087194919586, -0.05063247308135033, -0.027232155203819275, -0.15466348826885223, -0.00842801108956337, -0.02174198254942894, -0.16507355868816376, -0.0899486169219017, -0.006412755697965622, 0.1361790895462036, 0.04326764494180679, 0.004287464544177055, 0.1224319264292717, -0.0017574746161699295, -0.1213001161813736, 0.0045824418775737286, 0.13298067450523376, 0.27134203910827637, 0.147989884018898, 0.09170748293399811, -0.07266902923583984, 0.01573357731103897, 0.13191059231758118, -0.28954795002937317, 0.13724026083946228, 0.12476690858602524, 0.059341926127672195, 0.05578138306736946, 0.21815532445907593, -0.17086079716682434, -0.04293008893728256, 0.18340221047401428, -0.18330760300159454, 0.06268563121557236, -0.08526244759559631, 0.0013199783861637115, -0.004119078628718853, -0.08400356769561768, 0.18089725077152252, 0.15419329702854156, -0.11682872474193573, -0.15047316253185272, 0.06291307508945465, -0.13696761429309845, 0.004420476034283638, 0.04882857948541641, -0.056492794305086136, -0.11043675988912582, -0.353628545999527, 0.10094448179006577, 0.3501611351966858, 0.09449625760316849, -0.17064596712589264, 0.026432499289512634, -0.0634872168302536, -0.11301127821207047, 0.001361439935863018, -0.03003954328596592, -0.1387939304113388, 0.0771714523434639, -0.11378078162670135, 0.04487107694149017, 0.1161135584115982, 0.07000919431447983, 0.014108114875853062, 0.24706785380840302, -0.012400781735777855, 0.07991799712181091, 0.056709397584199905, 0.042067937552928925, -0.19787165522575378, -0.03285656124353409, -0.1376626342535019, 0.0038903439417481422, 0.08061608672142029, -0.1472669392824173, 0.0022450732067227364, 0.1023394986987114, -0.17865297198295593, 0.04974992573261261, 0.015112328343093395, -0.035862039774656296, -0.058060891926288605, 0.06822697818279266, -0.17596735060214996, -0.05299623683094978, 0.15171366930007935, -0.2820664346218109, 0.16248755156993866, 0.14290107786655426, -0.004463765304535627, 0.16811910271644592, 0.1192229762673378, 0.035243552178144455, 0.0004745572805404663, 0.029386963695287704, -0.044130995869636536, -0.01970563642680645, 0.018046151846647263, -0.05439963564276695, 0.023406799882650375, 0.08015769720077515', 'aditya', 'roy', 'kapur', 'addu', 'mumbai', '377'),
(2, '', '-0.03999021649360657, 0.05655823275446892, 0.03091026283800602, -0.02774970605969429, -0.06659402698278427, -0.08864913135766983, 0.0018639741465449333, -0.10384175926446915, 0.12988890707492828, 0.015636591240763664, 0.1599837988615036, -0.131469264626503, -0.23039838671684265, -0.056342676281929016, -0.09690012782812119, 0.10234709084033966, -0.0712820291519165, -0.013165915384888649, -0.05509928613901138, -0.07580369710922241, 0.021529724821448326, 0.03836187720298767, 0.1675211489200592, 0.03718617185950279, -0.06154419481754303, -0.2760007977485657, -0.09828508645296097, -0.1493562012910843, -0.011687176302075386, -0.08362529426813126, -0.047096941620111465, 0.11627235263586044, -0.24746689200401306, -0.12508057057857513, -0.022765453904867172, 0.018633214756846428, -0.0857977643609047, -0.06889674067497253, 0.2601716220378876, 0.04047926515340805, -0.09859243780374527, 0.024737047031521797, 0.04808231443166733, 0.18653379380702972, 0.15959930419921875, 0.008701426908373833, -0.005878150463104248, -0.03975006192922592, 0.12798407673835754, -0.2038429081439972, 0.0465146042406559, 0.15525610744953156, 0.17345426976680756, 0.0482560433447361, 0.04841069132089615, -0.06300470978021622, 0.06682078540325165, 0.05598556250333786, -0.15893858671188354, 0.013288810849189758, 0.06810871511697769, -0.035403668880462646, -0.01228347234427929, -0.046635229140520096, 0.1672845482826233, 0.10740266740322113, -0.003525207284837961, -0.07639715075492859, 0.15084150433540344, -0.0988677591085434, -0.04892326518893242, 0.05251574516296387, -0.11599946022033691, -0.1270182877779007, -0.24661283195018768, 0.048289574682712555, 0.2941894233226776, 0.13709717988967896, -0.1345730870962143, 0.04065154865384102, -0.15566101670265198, -0.03539927676320076, -0.05690143629908562, -0.033709488809108734, -0.11501353234052658, 0.025263983756303787, -0.10653753578662872, -0.002121114172041416, 0.1433672457933426, -0.1060464009642601, -0.06997144222259521, 0.16165754199028015, 0.0013451837003231049, 0.08331228047609329, 0.03299790620803833, -0.0474252924323082, -0.13733670115470886, -0.006960737053304911, -0.13744403421878815, 0.004109957255423069, 0.039594002068042755, -0.11447563022375107, -0.01876591145992279, 0.09414969384670258, -0.21408742666244507, 0.12172753363847733, -0.04280031472444534, -0.1167527288198471, -0.06397240608930588, 0.006785768084228039, -0.08295340836048126, 0.03488800674676895, 0.10749983042478561, -0.1750534474849701, 0.22903931140899658, 0.07323476672172546, -0.01648901216685772, 0.1309436410665512, 0.06445109844207764, 0.08458659052848816, -0.05603507161140442, 0.021760905161499977, -0.09625691175460815, -0.16811545193195343, 0.12397138774394989, 0.07383548468351364, 0.06466367095708847, 0.06874513626098633', 'apurva', 'asrani', 'm.', 'appu', 'dehlhi', '302'),
(3, '', '-0.09578975290060043, 0.10123670846223831, 0.061638154089450836, -0.01962772198021412, -0.056322500109672546, 0.0023575392551720142, -0.11593121290206909, -0.06583228707313538, 0.11554819345474243, -0.14760400354862213, 0.23875904083251953, 0.032095760107040405, -0.1962912380695343, -0.1639428734779358, -0.014523858204483986, 0.14475665986537933, -0.16279566287994385, -0.16894319653511047, 0.004504917189478874, -0.04203696548938751, 0.11114823818206787, 0.008120537735521793, 0.024279722943902016, 0.006415161304175854, -0.1075056940317154, -0.3744315207004547, -0.08809728175401688, -0.05636577308177948, 0.06630788743495941, -0.10841915011405945, -0.05167613551020622, 0.03694765642285347, -0.1574612855911255, 0.0007083471864461899, 0.02195662260055542, 0.09649287909269333, 0.02928750589489937, -0.06180958449840546, 0.19884321093559265, -0.019639253616333008, -0.22637945413589478, 0.03147648274898529, 0.06150753051042557, 0.2038370817899704, 0.18907956779003143, 0.08049178123474121, -0.0022947657853364944, -0.106541708111763, 0.17125611007213593, -0.13867242634296417, 0.04148104041814804, 0.1586110144853592, 0.15196947753429413, 0.015227414667606354, 0.04896266385912895, -0.17711424827575684, 0.04640559107065201, 0.04464091360569, -0.18969926238059998, -0.028638625517487526, -0.01722034066915512, -0.12982536852359772, 0.030129410326480865, -0.008187358267605305, 0.19755226373672485, 0.0716894119977951, -0.05818118527531624, -0.17644815146923065, 0.1952570676803589, -0.1459999829530716, -0.038533829152584076, 0.10626383125782013, -0.1364189237356186, -0.1595146656036377, -0.28630080819129944, 0.01656913012266159, 0.3609296381473541, 0.14760124683380127, -0.1472564935684204, 0.10024916380643845, 0.012008610181510448, -0.023754697293043137, 0.11171133816242218, 0.14881494641304016, -0.12257419526576996, 0.007059982046484947, -0.12145379185676575, 0.016107996925711632, 0.2109915018081665, 0.008100267499685287, -0.08453965187072754, 0.1497460901737213, 0.016262482851743698, 0.14904294908046722, 0.07731238752603531, -0.008861690759658813, -0.07819253951311111, 0.011260472238063812, -0.1449272334575653, -0.030192676931619644, 0.0010793553665280342, -0.03478133678436279, 0.004711249377578497, 0.1256120204925537, -0.1022888720035553, 0.041103143244981766, -0.024505184963345528, -0.008132596500217915, -0.04224828630685806, 0.051577892154455185, -0.09803295880556107, -0.056104376912117004, 0.048753488808870316, -0.2357155829668045, 0.20423999428749084, 0.16194438934326172, 0.07350451499223709, 0.1565386950969696, 0.1699065864086151, 0.08140236884355545, 0.00534124905243516, -0.08856935799121857, -0.165225550532341, -0.04990215599536896, 0.09608578681945801, -0.0352122001349926, 0.15812522172927856, 0.001840746495872736', 'kuvadiya', 'tushar', 'j.', 'appa', 'bhavnagar', '302,307'),
(4, '', '-0.04208740219473839, 0.06927990913391113, 0.07235392928123474, 0.015454067848622799, -0.12187334895133972, 0.02777465619146824, 0.03305118530988693, -0.1013769656419754, 0.11518057435750961, -0.08826207369565964, 0.12872251868247986, -0.05458323284983635, -0.25120189785957336, -0.03808923065662384, -0.00932603795081377, 0.055582620203495026, -0.049817245453596115, -0.1590280383825302, -0.08764724433422089, -0.02259019948542118, -0.048169419169425964, 0.036006588488817215, 0.022959519177675247, -0.07824859023094177, -0.028256423771381378, -0.39802518486976624, -0.08108795434236526, -0.02069726586341858, -0.032128166407346725, -0.05093545466661453, 0.013198924250900745, 0.12546420097351074, -0.22884084284305573, -0.07178878039121628, 0.014791522175073624, 0.08702845126390457, -0.09715089946985245, -0.024439217522740364, 0.12766128778457642, 0.0057711051777005196, -0.15866877138614655, 0.008668816648423672, 0.024753879755735397, 0.28342118859291077, 0.1080813929438591, 0.018285296857357025, -0.025255009531974792, -0.05549992620944977, 0.02516934648156166, -0.21913957595825195, 0.127052903175354, 0.14758451282978058, 0.103867307305336, 0.0679435059428215, 0.11639313399791718, -0.12874779105186462, 0.023723872378468513, 0.058458756655454636, -0.08044324815273285, 0.034446265548467636, 0.09729151427745819, -0.06803593039512634, -0.008963026106357574, -0.13051225244998932, 0.1699141263961792, 0.0640486553311348, -0.025372445583343506, -0.10074632614850998, 0.08725912123918533, -0.08968581259250641, -0.048399072140455246, -0.001166448462754488, -0.08075122535228729, -0.1328831911087036, -0.26294511556625366, 0.06711281836032867, 0.31570708751678467, 0.14969654381275177, -0.1806708574295044, -0.013155797496438026, -0.10266346484422684, 0.02886735275387764, 0.06125008314847946, -0.01120714284479618, -0.07000727951526642, 0.009849758818745613, -0.11764994263648987, 0.014225994236767292, 0.15942607820034027, -0.028472695499658585, -0.10661179572343826, 0.12908202409744263, -0.04841722920536995, -0.03691789507865906, 0.0612306110560894, -0.02486373484134674, -0.07333625853061676, 0.0017465869896113873, -0.20569828152656555, -0.03877435624599457, 0.04427281394600868, -0.1633996069431305, -0.06568341702222824, 0.11260224878787994, -0.21817165613174438, 0.1452360451221466, 0.011475500650703907, -0.018198898062109947, 0.042261525988578796, -0.030436556786298752, -0.12440541386604309, 0.0282006673514843, 0.14173224568367004, -0.2798752188682556, 0.23406265676021576, 0.11894548684358597, -0.012103389017283916, 0.1874806433916092, 0.07518694549798965, 0.06876739114522934, -0.06600722670555115, -0.04635525122284889, -0.14130011200904846, -0.14454393088817596, 0.05936354398727417, 0.10302699357271194, 0.01440455112606287, 0.08366020023822784', 'mohan', 'lal', 'l.', 'mohu', 'kolkata', '207'),
(5, '', '-0.136112242937088, 0.060876376926898956, 0.061159487813711166, -0.028743712231516838, -0.042680248618125916, -0.05889006704092026, -0.02060016244649887, -0.10207152366638184, 0.10303209722042084, -0.054968900978565216, 0.2544842064380646, 0.027829762548208237, -0.20508453249931335, -0.13662919402122498, -0.04664907604455948, 0.025934716686606407, -0.07567672431468964, -0.13741646707057953, -0.11662552505731583, -0.07431261986494064, -0.004156957380473614, -0.012071453034877777, 0.04769456386566162, 0.05863390862941742, -0.15576082468032837, -0.35594692826271057, -0.10931465774774551, -0.08288952708244324, 0.02715042233467102, -0.12393179535865784, 0.027008093893527985, 0.057301104068756104, -0.19767938554286957, -0.10029201954603195, -0.01441741082817316, 0.05402972921729088, -0.06658119708299637, -0.04194807633757591, 0.20687662065029144, 0.04648596793413162, -0.14298585057258606, 0.0181940458714962, 0.05090077966451645, 0.3654438555240631, 0.1920691728591919, 0.02177603356540203, 0.08021016418933868, -0.12000023573637009, 0.14330606162548065, -0.20582911372184753, 0.10670262575149536, 0.15617972612380981, 0.14113065600395203, 0.043290771543979645, 0.13988102972507477, -0.0916411429643631, 0.03230936452746391, 0.1497829705476761, -0.20788396894931793, 0.11585685610771179, 0.030076663941144943, 0.0034593287855386734, 0.012837143614888191, -0.08117062598466873, 0.18693174421787262, 0.06710117310285568, -0.12356363236904144, -0.1026991456747055, 0.10845950245857239, -0.16289688646793365, 0.006623650901019573, 0.17351678013801575, -0.0776980072259903, -0.2457074224948883, -0.2637231647968292, 0.1301802694797516, 0.4509912133216858, 0.21328549087047577, -0.13796794414520264, 0.020286589860916138, -0.1294906735420227, -0.12300312519073486, 0.07907874137163162, 0.056592199951410294, -0.12719930708408356, 0.015805646777153015, -0.09570374339818954, 0.05244959145784378, 0.20679165422916412, 0.08671341836452484, -0.07223667949438095, 0.2078614979982376, 0.029323730617761612, -0.021757887676358223, 0.06552468240261078, 0.03936241567134857, -0.19646772742271423, 0.03494884818792343, -0.13319993019104004, -0.024720925837755203, -0.017428219318389893, -0.09002074599266052, 0.031878165900707245, 0.016646958887577057, -0.10866221785545349, 0.15850652754306793, 0.011663734912872314, -0.025212958455085754, -0.03237162530422211, -0.030163437128067017, -0.13434453308582306, -0.04888239875435829, 0.10086560249328613, -0.3244892358779907, 0.14091959595680237, 0.10052526742219925, 0.1036243587732315, 0.16256864368915558, 0.12151098996400833, 0.03744757920503616, -0.01026844047009945, -0.03401276841759682, -0.04692220687866211, -0.021610576659440994, 0.07690112292766571, -0.030839454382658005, 0.15107792615890503, -0.02562280371785164', 'nawazuddin', 'siddiqui', 'p.', 'bvm shah', 'gandhi nagar', '302,307'),
(6, '', '-0.0746607854962349, 0.16608107089996338, 0.046709660440683365, -0.16916970908641815, -0.12191687524318695, 0.09088284522294998, 0.0008703302592039108, -0.020329460501670837, 0.09750080108642578, 0.048074185848236084, 0.2003246396780014, 0.040213387459516525, -0.305867999792099, -0.05312056466937065, 0.024554327130317688, 0.12465816736221313, -0.13838425278663635, -0.10311425477266312, -0.17186132073402405, 0.01636575534939766, -0.03856446221470833, 0.04964043200016022, -0.016640273854136467, -0.02356642112135887, -0.0888700932264328, -0.23925060033798218, 0.01222933642566204, -0.10831789672374725, -0.03699416667222977, -0.08981462568044662, 0.09766329079866409, 0.022328468039631844, -0.149491548538208, -0.06162803992629051, 0.010678328573703766, 0.06929974257946014, -0.10583995282649994, -0.08817239850759506, 0.19958719611167908, -0.03743107244372368, -0.15542860329151154, 0.023648696020245552, 0.07285506278276443, 0.24865727126598358, 0.18967370688915253, -0.11969723552465439, 0.1065782904624939, -0.03567247837781906, 0.09057152271270752, -0.3042979836463928, 0.10867775231599808, 0.060995519161224365, 0.1861192286014557, 0.11838601529598236, 0.06244388222694397, -0.21363617479801178, 0.06997331976890564, 0.1982146054506302, -0.2312975376844406, 0.10661319643259048, 0.07544850558042526, -0.08258644491434097, -0.04536626115441322, -0.02417166158556938, 0.20511312782764435, 0.11376599967479706, -0.1191607341170311, -0.19076602160930634, 0.11447285860776901, -0.06252525001764297, -0.049894779920578, 0.07554919272661209, -0.12852773070335388, -0.1298043131828308, -0.2864565849304199, 0.08932842314243317, 0.3115524649620056, 0.11311381310224533, -0.265214204788208, -0.029791202396154404, -0.12832678854465485, 0.0032228361815214157, -0.016557704657316208, 0.0044106729328632355, -0.060937896370887756, -0.07163210958242416, -0.10363658517599106, -0.004976075142621994, 0.19311508536338806, -0.055526088923215866, -0.04527892544865608, 0.21393577754497528, 0.09983894228935242, -0.10036806762218475, 0.061170149594545364, 0.03563028201460838, -0.029667595401406288, -0.02594056911766529, -0.10106772929430008, 0.037054404616355896, -0.019069546833634377, -0.22981539368629456, -0.007429792080074549, 0.09331133961677551, -0.19283495843410492, 0.18102969229221344, 0.020417002961039543, 0.021866071969270706, 0.002210121601819992, -0.01335855945944786, -0.05281546711921692, -0.055542752146720886, 0.24377451837062836, -0.24477873742580414, 0.2175600379705429, 0.15769802033901215, 0.014868238009512424, 0.12303466349840164, 0.07322113960981369, 0.1260722130537033, -0.005212097428739071, 0.043561555445194244, -0.09882274270057678, -0.05860678106546402, 0.027057748287916183, 0.036629900336265564, 0.03303119167685509, 0.12917150557041168', 'pruthvi', 'show', 'q.', 'FF heros', 'America', '477'),
(7, '', '-0.0698254331946373, 0.07618961483240128, 0.17458456754684448, 0.04434213787317276, -0.01960751973092556, -0.08623138070106506, 0.003412787802517414, -0.08979631960391998, 0.11899136006832123, -0.03865104168653488, 0.21822910010814667, -0.06920289248228073, -0.23499399423599243, 0.07302430272102356, -0.08862566947937012, 0.1007973924279213, -0.07776842266321182, -0.08677119016647339, -0.14252007007598877, -0.031094659119844437, -0.028407873585820198, 0.006295238621532917, 0.03389272838830948, -0.02725980617105961, -0.10773452371358871, -0.37026408314704895, -0.11919236183166504, -0.07785084843635559, 0.027879012748599052, -0.06957480311393738, 0.000899224542081356, 0.057684388011693954, -0.10405605286359787, -0.0530058816075325, 0.00036414340138435364, 0.022515952587127686, -0.07418125867843628, -0.08175570517778397, 0.2353137731552124, 0.07498925924301147, -0.18059830367565155, 0.05949750915169716, 0.06598129868507385, 0.34905192255973816, 0.1797567754983902, 0.05234142765402794, 0.059592776000499725, -0.08375893533229828, 0.07006802409887314, -0.2777140140533447, 0.109805628657341, 0.09370990842580795, 0.1135212704539299, 0.12093976140022278, 0.15592041611671448, -0.19533449411392212, 0.015158111229538918, 0.15901726484298706, -0.20887364447116852, 0.1730867326259613, 0.059728220105171204, 0.002255180850625038, 0.03170143812894821, -0.05546841025352478, 0.1955176293849945, 0.1523461788892746, -0.14503765106201172, -0.021976836025714874, 0.1156257688999176, -0.14717121422290802, 0.0137199517339468, 0.05144660174846649, -0.09452714771032333, -0.18932735919952393, -0.3019585609436035, 0.042901113629341125, 0.3998014032840729, 0.14061591029167175, -0.16442357003688812, -0.07177382707595825, -0.06102417781949043, -0.05052701383829117, 0.05471282824873924, 0.055543452501297, -0.15110783278942108, -0.02685462310910225, -0.07295454293489456, -0.018763931468129158, 0.18132856488227844, 0.06616664677858353, -0.07759994268417358, 0.20976348221302032, -0.04829252511262894, -0.04640167951583862, -0.005708729848265648, 0.07564172893762589, -0.18532902002334595, -0.05145880952477455, -0.15448077023029327, -0.06165225803852081, -0.0014567794278264046, -0.12661732733249664, -0.020682724192738533, 0.08871566504240036, -0.23422513902187347, 0.1518360674381256, -0.0020521932747215033, -0.015507304109632969, 0.008554356172680855, 0.024120094254612923, -0.08864831924438477, 0.055212631821632385, 0.19740936160087585, -0.2614405155181885, 0.17304688692092896, 0.18455545604228973, 0.04344379901885986, 0.10978694260120392, 0.07761456072330475, -0.016846267506480217, -0.030272001400589943, 0.010096268728375435, -0.12376809120178223, -0.05151955410838127, -0.0130050303414464, -0.008791055530309677, 0.05962768942117691, 0.07143069803714752', 'tonny', 'stark', 'u', 'tony bhai', 'brazil', '456'),
(8, '', '-0.14850474894046783, 0.05217205360531807, -0.0015846611931920052, -0.05820300802588463, -0.09946891665458679, -0.05756914243102074, 0.021085046231746674, 0.035964950919151306, 0.1316705197095871, -0.10385887324810028, 0.12742352485656738, -0.014178010635077953, -0.23908638954162598, 0.012903347611427307, 0.029849305748939514, 0.0967329666018486, -0.1771421730518341, -0.10052519291639328, -0.04705752432346344, -0.11510064452886581, 0.11437486112117767, 0.062324319034814835, -0.055634330958127975, 0.06841837614774704, -0.11738988757133484, -0.32145723700523376, -0.07575300335884094, -0.06595242768526077, 0.00621234904974699, -0.10482211410999298, 0.060817159712314606, 0.07232233136892319, -0.10261908173561096, -0.0017407238483428955, 0.036702144891023636, 0.11318843066692352, -0.0554204136133194, -0.05440352484583855, 0.18754266202449799, 0.010062308982014656, -0.09988431632518768, -0.06867370754480362, 0.05282873660326004, 0.34572717547416687, 0.1156705692410469, 0.08387383073568344, 0.0017833039164543152, 0.0005259746685624123, 0.09991663694381714, -0.2609401047229767, 0.07551079988479614, 0.13149896264076233, 0.04739223048090935, 0.08928477764129639, 0.11650155484676361, -0.13163496553897858, 0.06576241552829742, 0.0868966206908226, -0.20196124911308289, 0.07429508119821548, 0.033819567412137985, -0.14781369268894196, -0.03935735672712326, -0.07380267232656479, 0.22176823019981384, 0.08015824109315872, -0.09824434667825699, -0.12087210267782211, 0.09143960475921631, -0.21477271616458893, -0.11996612697839737, 0.037414852529764175, -0.09233563393354416, -0.13689519464969635, -0.27389732003211975, 0.019313182681798935, 0.3244372606277466, 0.1856645792722702, -0.0977935642004013, 0.045067958533763885, 0.01469301525503397, -0.020305395126342773, 0.17030543088912964, 0.08086463063955307, -0.10122057795524597, -0.019458536058664322, -0.10850919038057327, 0.09146381914615631, 0.17350345849990845, -5.9213489294052124e-05, -0.09565353393554688, 0.16303566098213196, 0.01612001284956932, 0.008111519739031792, 0.030944153666496277, -0.010434171184897423, -0.06432624161243439, -0.023854082450270653, -0.06955642998218536, -0.013965996913611889, 0.13654853403568268, -0.1144731417298317, -0.010518023744225502, 0.11032311618328094, -0.17292094230651855, 0.10440181940793991, -0.03158142790198326, 0.0025045964866876602, -0.021182775497436523, 0.026998231187462807, -0.2152717560529709, -0.012021717615425587, 0.12323840707540512, -0.2541176974773407, 0.17161963880062103, 0.20129206776618958, -0.029114874079823494, 0.140120729804039, 0.040682390332221985, 0.04228662699460983, -0.016692178323864937, -0.049393557012081146, -0.1656489372253418, -0.06002607196569443, 0.06951408088207245, 0.07958656549453735, 0.07712450623512268, 0.011258536949753761', 'Khokhar', 'Aman', 'n', 'gamer', 'bhavnagar', '302,307');

-- --------------------------------------------------------

--
-- Table structure for table `system record`
--

CREATE TABLE `system record` (
  `c_id` int(11) NOT NULL,
  `record_time` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `u_id` int(11) NOT NULL,
  `u_name` varchar(40) NOT NULL,
  `u_pass` varchar(20) NOT NULL,
  `u_email` varchar(30) NOT NULL,
  `u_contact` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`u_id`, `u_name`, `u_pass`, `u_email`, `u_contact`) VALUES
(1, 'ravirajbhai gandhi', 'raviraj@123', 'ravirajgandhi@gmail.com', 707990834),
(2, 'kuldeep jani', 'kuldeep@123', 'janikuldeep@gmail.com', 982536546),
(3, 'dangashiya ram', 'ram@123', 'dagashiyaram@gmail.com', 2147483647);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`a_id`);

--
-- Indexes for table `criminal`
--
ALTER TABLE `criminal`
  ADD PRIMARY KEY (`c_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`u_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `a_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `criminal`
--
ALTER TABLE `criminal`
  MODIFY `c_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `u_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;