|     | Faster | Rates          | of Convergence | to Stationary |     | Points | in  |     |     |
| --- | ------ | -------------- | -------------- | ------------- | --- | ------ | --- | --- | --- |
|     |        | Differentially | Private        | Optimization  |     |        |     |     |     |
RamanArora*1 RaefBassily*23 Toma´sGonza´lez*4 Cristo´balGuzma´n*4 MichaelMenart*2 EnayatUllah*1
|     | Abstract |     |     | 1.Introduction |     |     |     |     |     |
| --- | -------- | --- | --- | -------------- | --- | --- | --- | --- | --- |
Protectingusers’datainmachinelearningmodelshasbe-
comeacentralconcerninmultiplecontexts,e.g.thosein-
Westudytheproblemofapproximatingstationary
|     |     |     |     | volvingfinancialorhealthdata. |     |     | Inthisrespect,differential |     |     |
| --- | --- | --- | --- | ----------------------------- | --- | --- | -------------------------- | --- | --- |
pointsofLipschitzandsmoothfunctionsunder
privacy(DP)isthegoldstandardforrigorousprivacypro-
(ε,δ)-differentialprivacy(DP)inboththefinite-
|                           |     |                 |          | tection(Dwork&Roth,2014).                          |     |     | Therefore,recentresearch |     |     |
| ------------------------- | --- | --------------- | -------- | -------------------------------------------------- | --- | --- | ------------------------ | --- | --- |
| sumandstochasticsettings. |     | Apointwiscalled |          |                                                    |     |     |                          |     |     |
|                           |     |                 | (cid:98) | hasfocusedonthelimitsandpossibilitiesofsolvingsome |     |     |                          |     |     |
:Rd →Rif
anα-stationarypointofafunctionF ofthemostwell-establishedmachinelearningproblemsun-
| ∥∇F(w)∥≤α. | Wegiveanewconstructionthat |       |                 |                                                    |     |     |     |     |     |
| ---------- | -------------------------- | ----- | --------------- | -------------------------------------------------- | --- | --- | --- | --- | --- |
|            | (cid:98)                   |       |                 | dertheconstraintofDP.Despiteintensiveresearch,some |     |     |     |     |     |
| improves   | over the existing          | rates | in the stochas- |                                                    |     |     |     |     |     |
fundamentalproblemsremainnotcompletelyunderstood.
ticoptimizationsetting,wherethegoalistofind Oneexampleisnonconvexoptimization;namely,thetask
approximatestationarypointsofthepopulation
ofapproximatingstationarypoints,whichhasbeenheavily
risk given n samples. Our construction finds a studiedinrecentyearsinthenon-privatesetting(Fangetal.,
√
| O˜(cid:0) 1 | + (cid:2) d(cid:3)1/2(cid:1) | -stationarypointofthepop- |     |          |               |        |         |       |            |
| ----------- | ---------------------------- | ------------------------- | --- | -------- | ------------- | ------ | ------- | ----- | ---------- |
|             |                              |                           |     | 2018; Ma | et al., 2018; | Carmon | et al., | 2017; | Nesterov & |
| n1/3        | nε                           |                           |     |          |               |        |         |       |            |
ulationriskintimelinearinn. Wealsoprovide Polyak,2006;Ghadimi&Lan,2013;Arjevanietal.,2019;
√
anefficientalgorithmthatfindsanO˜(cid:0)(cid:2) d(cid:3)2/3(cid:1) Foster etal., 2019). Thisproblem ismotivated bythe in-
-
nε
stationarypointinthefinite-sumsetting. Thisim- tractabilityofnonconvex(global)optimization,aswellas
√
provesonthepreviousbestrateofO˜(cid:0)(cid:2) d(cid:3)1/2(cid:1) byanumberofsettingswherestationarypointshavebeen
.
nε
Furthermore,undertheadditionalassumptionof shown to be global minima (Ge et al., 2016; Sun et al.,
2016).
| convexity, | we completely | characterize | the sam- |     |     |     |     |     |     |
| ---------- | ------------- | ------------ | -------- | --- | --- | --- | --- | --- | --- |
plecomplexityoffindingstationarypointsofthe
1.1.Contributions
populationrisk(uptopolylogfactors)andshow
thattheoptimalrateonpopulationstationarityis
|              | √        |     |     | Inthiswork,wemakeprogresstowardsresolvingthecom- |     |     |     |     |     |
| ------------ | -------- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- |
| Θ˜(cid:0) √1 | d(cid:1) |     |     |                                                  |     |     |     |     |     |
+ . Finally,weshowthatourmethods plexityofapproximatingstationarypointsinoptimization
|        | n nε            |                       |     |     |     |     |     |     |     |
| ------ | --------------- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
| can be | used to provide | dimension-independent |     |     |     |     |     |     |     |
undertheconstraintofdifferentialprivacy,forbothempir-
|     | (cid:0) | (cid:0)(cid:2) √ rank(cid:3)2/3 | (cid:1)(cid:1) |     |     |     |     |     |     |
| --- | ------- | ------------------------------- | -------------- | --- | --- | --- | --- | --- | --- |
ratesofO √1 +min , 1 on ical and population risks. A summary of our new results
|            | n            | nε              | (nε)2/5 |                      |     |                |     |               |     |
| ---------- | ------------ | --------------- | ------- | -------------------- | --- | -------------- | --- | ------------- | --- |
|            |              |                 |         | isavailableinTable1. |     | Inwhatfollows, |     | distheproblem |     |
| population | stationarity | for Generalized | Linear  |                      |     |                |     |               |     |
Models (GLM), where rank is the rank of the dimension,nisthedatasetsize,andε,δaretheapproximate
DPparameters.
designmatrix,whichimprovesupontheprevious
bestknownrate.
Ourfirstsetofresultspertainstothetaskofapproximating
|                    |                                  |     |     | stationary        | points of | the population                  | risk.     | Results                      | for this |
| ------------------ | -------------------------------- | --- | --- | ----------------- | --------- | ------------------------------- | --------- | ---------------------------- | -------- |
|                    |                                  |     |     | problemarescarce. |           | Weprovidethefastestrateuptodate |           |                              |          |
|                    |                                  |     |     |                   |           |                                 | O˜(cid:0) | (cid:2) √ d(cid:3)1/2(cid:1) |          |
|                    |                                  |     |     | for this problem  | under     | DP,                             | of 1      | +                            | , with   |
| *Equalcontribution | 1DepartmentofComputerScience,The |     |     |                   |           |                                 | n1/3      | nε                           |          |
JohnsHopkinsUniversity2DepartmentofComputerScience& analgorithmthatmoreoverhasoraclecomplexity n(i.e.,
Engineering,TheOhioStateUniversity3TranslationalDataAn- is single-pass). This algorithm is a noisy version of the
alyticsInstitute(TDAI),TheOhioStateUniversity4Institutefor
SPIDERalgorithm(Fangetal.,2018),whosegradientesti-
MathematicalandComputationalEngineering,PontificiaUniver- matorsarebuiltusingatree-aggregationdatastructurefor
sidad Cato´lica de Chile. Correspondence to: Michael Menart prefix-sums(Asietal.,2021).
<menart.2@osu.edu>,EnayatUllah<enayat@jhu.edu>.
|     |     |     |     | Next, we | focus | on the | task of | approximating | sta- |
| --- | --- | --- | --- | -------- | ----- | ------ | ------- | ------------- | ---- |
40th
Proceedings of the International Conference on Machine tionary points in empirical nonconvex optimization
Learning,Honolulu,Hawaii,USA.PMLR202,2023.Copyright
|     |     |     |     | (a.k.a. finite-sum | case). | In  | this context, | we  | provide al- |
| --- | --- | --- | --- | ------------------ | ------ | --- | ------------- | --- | ----------- |
2023bytheauthor(s).
1

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
|     |     |     | (cid:0)(cid:2) √ d(cid:3)2/3(cid:1) |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
gorithms with rate O , and oracle complexity1 consideredbetterinpractice. Forthepopulationrisk,itis
nε
O˜(cid:0) (cid:8)(cid:0)n5ε2(cid:1)1/3 (cid:0) √nε(cid:1)2(cid:9)(cid:1) worthnotingthattheempiricalnormofthegradientdoes
| max |     | ,   |     | . This | rate | is sharper | than |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | ---- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
d
d not translate directly into population gradient guarantees,
thebestknownforthisproblem(Wangetal.,2017).
evenifthealgorithminuseisuniformlystable(Bousquet&
Wecontinuebyinvestigatingstationarypointsforconvex Elisseeff,2002),sincethistypeofguaranteedoesnotenjoy
lossesandgiveanalgorithmbasedontherecursiveregular- astability-implies-generalizationproperty. Therefore,we
izationtechniqueof(Allen-Zhu,2018)whichachievesthe optforsinglepassmethodsthatcombinevariance-reduction
√
| optimalrateofΘ˜(cid:0) |     |     | d(cid:1) |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
√1 + onpopulationstationarity. To withtree-aggregation;thesetechniquesareparticularlysuit-
|                                          |     | n   | nε  |     |     |         |             |                                                     |     |     |     |              |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | ------- | ----------- | --------------------------------------------------- | --- | --- | --- | ------------ | --- | --- |
|                                          |     |     |     |     |     |         | √           | ablefortheclassicalSpideralgorithm(Fangetal.,2018), |     |     |     |              |     |     |
| establishoptimality,wegivealowerboundofΩ |     |     |     |     |     | (cid:0) | d(cid:1) on |                                                     |     |     |     |              |     |     |
|                                          |     |     |     |     |     |         |             | whichistheonewebaseourmethodon.                     |     |     |     | Fortheconvex |     |     |
nε
empiricalstationarityunderDP(Theorem4.3)andanon-
setting,weuserecursiveregularization(Allen-Zhu,2018)
| private lower | bound |                                    | of Ω(√1 | ) on | population | stationarity |     |                                                  |     |     |     |     |     |     |
| ------------- | ----- | ---------------------------------- | ------- | ---- | ---------- | ------------ | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
|               |       |                                    |         | n    |            |              |     | whichwasusedtoachievetheoptimalnon-privaterateby |     |     |     |     |     |     |
| (TheoremA.2). |       | Wealsogivealinear-timemethod,which |         |      |            |              |     |                                                  |     |     |     |     |     |     |
(Fosteretal.,2019).
achievestheoptimalratewhenthesmoothnessparameteris
|             |                                     |     |     |     |     |     |     | Finally, | our method | for (non-convex) |     | GLMs | uses | the |
| ----------- | ----------------------------------- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ---------------- | --- | ---- | ---- | --- |
| notsolarge. | Weconcludethepapershowingablack-box |     |     |     |     |     |     |          |            |                  |     |      |      |     |
reductionthatconvertsanyDPmethodforfindingstation- Johnson-Lindenstraussbaseddimensionalityreductiontech-
arypointsofsmoothandLipschitzlossesintoaDPmethod niquesimilarto(Aroraetal.,2022),whichfocusedonthe
|     |     |     |     |     |     |     |     | convex setting. |     | Moreover, | for population | stationarity |     | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | -------------- | ------------ | --- | --- |
withdimension-independentratesforthecaseofgeneral-
izedlinearmodels(GLM).Usingourproposedmethodwith GLMs,wegiveanewuniformconvergenceresultofgradi-
|     |     |     |     |     |     |     |     | entsofLipschitzfunctions. |     |     | Thisguarantee,unliketheprior |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | ---------------------------- | --- | --- | --- |
PrivateSpiderboostasthebasealgorithmyieldsarateof
(cid:16) (cid:16)(cid:2) √ (cid:17)(cid:17) workof(Fosteretal.,2018),hasonlypoly-logarithmicde-
| O˜ √1 +min |     | rank(cid:3)2/3 |     | , 1 | on  | population | sta- |     |     |     |     |     |     |     |
| ---------- | --- | -------------- | --- | --- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
n nε (nε)2/5 pendenceontheradiusoftheconstraintset,whichiscrucial
| tionarity. | This | improves | upon | the | result | of (Song | et al., |     |     |     |     |     |     |     |
| ---------- | ---- | -------- | ---- | --- | ------ | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
forouranalysis.
| 2021)whichproposedamethodwithO˜(cid:0)(cid:2) |     |     |     |     |     | √ rank(cid:3)1/2(cid:1) |     |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
em-
nε
piricalstationarity2.
1.3.RelatedWork
Thecurrentworkfitswithintheliteratureofdifferentially
1.2.OurTechniques
|     |     |     |     |     |     |     |     | private optimization, |     | which | has primarily | focused |     | on the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | ----- | ------------- | ------- | --- | ------ |
Ourmethodscombinemultipletechniquesfromoptimiza-
convexcase(Chaudhurietal.,2011;Jainetal.,2012;Kifer
tionanddifferentialprivacyinnovelways.Thelowerbound etal.,2012;Bassilyetal.,2014;Talwaretal.,2014;Jain
fortheempiricalnormofthegradientusesfingerprinting
&Thakurta,2014;Talwaretal.,2015;Bassilyetal.,2019;
codestoalosssimilartothatusedforDifferentiallyPrivate- Feldmanetal.,2020;Asietal.,2021;Bassilyetal.,2021b).
Empirical Risk Minimization (DP-ERM) (Bassily et al., Theculminationofthislineofworkfortheconvexsmooth
| 2014),craftedtoworkintheunconstrainedcase. |     |     |     |     |     | Thislower |     |     |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
caseshowedthatoptimalratesareachievableinlineartime
boundcanbeextendedtothepopulationgradientnormbya (Feldmanetal.,2020;Asietal.,2021;Bassilyetal.,2021b).
| knownre-samplingargument(Bassilyet |     |     |     |     | al.,2019). |                | Wealso |                                    |       |             |        |                     |       |     |
| ---------------------------------- | --- | --- | --- | --- | ---------- | -------------- | ------ | ---------------------------------- | ----- | ----------- | ------ | ------------------- | ----- | --- |
|                                    |     |     |     |     | √          |                |        | Our work                           | shows | that in the | convex | case similar        | rates | are |
| giveanon-privatelowerboundofΩ(1/   |     |     |     |     |            | n)onpopulation |        |                                    |       |             |        |                     |       |     |
|                                    |     |     |     |     |            |                |        | achievableforthenormofthegradient: |       |             |        | thisresultisuseful, |       |     |
stationaritywithnsampleswhichholdsevenindimension e.g.,fordualformulationsoflinearlyconstrainedconvex
1,asopposedtopreviousresults(Fosteretal.,2019).
programs(Nesterov,2012),andmoreoverithasbecomea
problemofindependentinterest(Allen-Zhu,2018;Foster
| Efficient | algorithms |     | for (both | empirical |     | and population) |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | --------- | --------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
etal.,2019).3
| norm of | the gradient |     | are derived | using | noisy | versions | of  |     |     |     |     |     |     |     |
| ------- | ------------ | --- | ----------- | ----- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
variance-reducedstochasticfirstordermethods,whichhave Regarding stationary points for nonconvex losses, work
provedremarkablyusefulinDPstochasticoptimization(Asi in DP is far more recent, and primarily focused on the
etal.,2021;Bassilyetal.,2021b;a).Inthecaseoftheempir-
empiricalstationarity(Wangetal.,2017;Zhangetal.,2017;
icalrisk,weuseanoisyversionofSpiderBoost(Wangetal.,
2019c). Weremarkthatourmethodscanachievecompara- 3Toprovideaspecificexample,considerthedualofthereg-
ularizeddiscreteoptimaltransportproblem,asdiscussedin(Di-
blerateswhenappliedtosimilaralgorithmssuchasSpider
akonikolas&Guzma´n,2023),Section5.6.Ifthemarginalsµ,νin
(Fangetal.,2018)andStorm(Cutkosky&Orabona,2019),
thatmodelareaccessedthroughi.i.d.samples,thenthisbecomes
butSpiderBoostallowsforalargerlearningratewhichis
|     |     |     |     |     |     |     |     | an SCO problem. |     | Moreover, | it is argued | in that | reference | that |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | ------------ | ------- | --------- | ---- |
approximatestationarypointsprovideapproximatelyfeasibleand
1Weconsiderforcomplexitythefirst-orderoraclemodel,stan-
optimaltransportsthroughdualityarguments.Hence,theresultis
dardforcontinuousoptimization(Nemirovsky&Yudin,1983).
anSCOproblemwherewerequireapproximatestationarypoints.
2Thisistherateobtainedafterfixingamistakeintheproofof
Theorem4.1in(Songetal.,2021).Specifically,intheirproof,the
lastterminEq.(14)ismissingafactorofT.
2

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
Setting Convergence OurRate Previousbest-knownrate
(cid:16)√ (cid:17)2/3 (cid:16)√ (cid:17)1/2
Empirical d (Thm.4.2) d (Wangetal.,2017)
nε nε
Non-convex
Population 1 + (cid:16)√ d (cid:17)1/2 (Thm.3.2) √ dε+ (cid:0) √ d(cid:1)1/2 (Zhouetal.,2020)
n1/3 nε nε
√
Convex Population √1 + d (Thm.5.1) None
n nε
Empirical (cid:2) √ rank(cid:3)2/3 ∧ 1 (Cor.6.2) (cid:16)√ rank (cid:17)1/2 (Songetal.,2021)
Non-convex nε (nϵ)2/5 nε
GLM Population √1 + (cid:2)√ rank(cid:3)2/3∧ 1 (Cor.6.2) None
n nε (nϵ)2/5
√
ConvexGLM Population √1 + rank∧√1 (Cor.6.2) None
n nε nϵ
Table1.Resultssummary:Weomitlogfactorsandfunction-classparameters.Thesymbol∧standsforminimumofthequantities.
Wang & Xu, 2019; Wang et al., 2019a)4. Under similar theirratesareslowerthanours.6 Ontheotherhand,they
assumptions to ours these works approximate stationary provide results for (close to nearly) stationary points in
√
pointswithrateO˜(cid:0)(cid:2) d(cid:3)1/2(cid:1) ,whichisslowerthanours. constrained/unconstrainedsettings, forabroaderclassof
nε
weakly convex losses (possibly nonsmooth). This result
Works addressing population guarantees for the norm of is then more general, but the rate of O (cid:0) 1 + (cid:2) √ d(cid:3)1/3(cid:1)
thegradientunderDParescarce. (Zhouetal.,2020)pro- n1/4 nε
is substantially slower than ours, and their algorithm has
posedanoisygradientmethod,whosepopulationguaran-
oraclecomplexitywhichissuperlinearinn.
tee is obtained by generalization properties of DP. How-
ever, the best guarantee obtainable with their analysis is Theproblemofstationarypointsin(nonprivate)stochastic
√ √
O (cid:0)(cid:2) d(cid:3)1/2 + dε (cid:1)5. Note that for any ε this rate is optimizationhasdrawnmajorattentionrecently(Ghadimi&
nε
Ω
(cid:0) [d/n]1/3(cid:1)
. Under additional assumptions (on the Hes-
Lan,2013;2016;Fangetal.,2018;Allen-Zhu,2018;Foster
sian),(Wang&Xu,2019)obtainsarateofO˜( (cid:112) d/(nε))by etal.,2018;2019;Arjevanietal.,2019). Tothebestofour
knowledge,nolowerboundsforthesamplecomplexity7of
uniformconvergenceofgradients,whichissharperwhenε
thisproblemareknown(beyondthoseknownfortheconvex
isconstant. Bycontrast,ourrateismuchfasterthanboth
case(Fosteretal.,2019)). Ontheotherhand,oraclecom-
forε=Θ(1). Inparticular,inthisrange,ourratesarefaster
(cid:112) plexityisbynowunderstood: inhighdimensions,for(on
than those obtained by uniform convergence, O( d/n)
average)smoothlossestheoptimalstochasticoraclecom-
(Foster et al., 2018). Moreover, our method runs in time
plexityrateisO(1/n1/3)(Arjevanietal.,2019). Although
linear in n. On the other hand, in the much more restric-
thisprovidessomeevidenceofthesharpnessofourresults
tivesettingwherethelosssatisfiesthePolyak-Łojasiewicz
(seeAppendixB.2),notethattheselowerboundsrequire
(PL)inequality,(Zhangetal.,2021)providepopulationrisk
boundsofO˜(d/[nε]2)underDP.
veryhighdimensionalconstructions(namely,d=Ω(1/α4),
whereαistherate),whichlimitstheirapplicabilityinthe
Theworkof(Bassilyetal.,2021a)studiespopulationguar- privatesetting.
antees for stationarity in constrained settings, obtaining
√ Inanindependentandconcurrentwork,(Tran&Cutkosky,
rates O (cid:0) n1 1 /3 + (cid:2) nε d(cid:3)2/5(cid:1) in linear time. Notice first that 2022) achieve a rate of O( (cid:2) √ d(cid:3)2/3 + √1 ) on the empir-
theseguaranteesarebasedontheFrank-Wolfegap, mak- nϵ n
ing those results incomparable to ours. Despite this fact, ical gradient with gradient complexity O(n7/3ϵ3/4/d2/3)
usingaDPtreeaggregationmethod. Notethatourresult
√
4Anotherwork,(Wangetal.,2019b),claimstoachievethis
removesthe1/ ntermandimprovestheoraclecomplexity
w
co
i
n
th
ta
i
i
m
ns
pr
a
o
n
ve
e
d
rro
o
r
ra
w
cl
h
e
ic
c
h
om
is
p
n
le
o
x
t
i
e
ty
a
.
si
H
ly
ow
fix
e
e
v
d
e
.
r,
S
th
p
e
ec
a
i
n
fi
a
c
l
a
y
l
s
l
i
y
s
,
t
(
h
W
er
a
e
n
in
g
toO˜(cid:0) max (cid:8)(cid:0)n5
d
ε2(cid:1)1/3 , (cid:0) √nε
d
(cid:1)2(cid:9)(cid:1) ,whichisbetterwhenever
etal.,2019b,proofofTheorem4.1)usesσ2b2 >0.7toemploy
0 0
privacyamplificationviasubsampling.Thisisnottrueastheyset 6Webelieveourmethodscanbeextendedtoconstrainedset-
√ √
σ =1/[d1/4 n]andb = n/d1/4. tingsusinggradientmapping,aguaranteeforwhichisstronger
0 0 √
5(Zhouetal.,2020)omitstheterm dε,butthisomissionis thanforFrank-Wolfegap(Lan,2020,Section7.5.1).Wedeferthis
√
onlyvalidwhenε<1/[n d]1/3. extensiontofuturework.
7Samplecomplexityisthefundamentallimitonthesample
sizeneeded, asafunctionofα, toachieveαstationarity. This
isdifferentfromtheoraclecomplexityasoneisnotlimitedto
first-ordermethods.
3

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
d≤n2ϵ1/4(i.e.essentiallywhenevertheerrorisnontrivial). Searchtraversalofthetree. WedenotebyDFS[D]thesetof
Further,weaccomplishthiswithamuchsimpleranalysis. nodesinthevisitingorderexcludingtheroot,forexample:
|     |     |     |     |     |     |     |     | DFS[2] | = {u 0 ,u 00 | ,u 01 ,u | 1 ,u 10 ,u 11 | }. When | a left child |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | -------- | ------------- | ------- | ------------ |
nodeisvisited,itreceivesthesameparametervectorand
2.Preliminaries
gradientestimatoroftheparentnode.
|       | Rd  |     | R      |     |                 |     |      |     |     |     |     |     |     |
| ----- | --- | --- | ------ | --- | --------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
| Let f | : × | X → | denote | a   | (loss) function |     | tak- |     |     |     |     |     |     |
ing as input, the model parameter w and data point x ∈ Algorithm1Tree-basedPrivateSpider
X. We assume that the function w (cid:55)→ f(w;x) is L 0 - Input: S = (x ,...,x ) ∈ Xn: private dataset, (ε,δ):
|     |     |     |     |     |     |     |     |     | 1   | n   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Lipschitz and L -smooth. That is, for all x ∈ X and privacyparameters,T: numberofrounds,b: batchsize
1
| w ,w | ∈ Rd, | |f(w ;x)−f(w |     | ;x)| | ≤ L | ∥w −w | ∥   |                           |     |     |     |                    |     |
| ---- | ----- | ------------ | --- | ---- | --- | ----- | --- | ------------------------- | --- | --- | --- | ------------------ | --- |
| 1 2  |       | 1            |     | 2    |     | 0 1   | 2   | atbeginningofeachround,D: |     |     |     | depthoftreesateach |     |
and ∥∇f(w ;x)−∇f(w ;x)∥ ≤ L ∥w −w ∥. Given round,β: step-sizeparameter,α˜: accuracyparameter.
|           | 1   |             | 2         |     | 1 1        | 2         |     |              |     |     |     |     |     |
| --------- | --- | ----------- | --------- | --- | ---------- | --------- | --- | ------------ | --- | --- | --- | --- | --- |
| a dataset | S ∈ | Xn of       | n points, | we  | define the | empirical |     | w            | =0  |     |     |     |     |
|           |     |             |           |     |            |           |     | 1: 0,ℓ(2D−1) |     |     |     |     |     |
|           |     | 1 (cid:80)n |           |     |            |           |     |              |     |     |     |     |     |
risk as F(w;S) = f(w;x i ). Assuming that the 2: fort=1toT do
|             |     | n       | i=1    |      |            |         |     |     |         |             |     |     |     |
| ----------- | --- | ------- | ------ | ---- | ---------- | ------- | --- | --- | ------- | ----------- | --- | --- | --- |
| data points | are | sampled | i.i.d. | from | an unknown | distri- |     | 3:  | Setw =w |             |     |     |     |
|             |     |         |        |      |            |         |     |     | t,∅     | t−1,ℓ(2D−1) |     |     |     |
bution D, the population risk, denoted as F(w;D) is de- DrawabatchS t,∅ofbdatapoints,setS ←S\S
|     |     |     |     |     |     |     |     | 4:  |     |     |     |     | t,∅. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
finedasF(w;D)=E
|     |     | x∼D | f(w;x). | Furthermore,wedefine |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
8L2
F =F(0;S)−min {F(w;S)}whendiscussingthe 5: Setσ 2 := 0 lo g ( 1 .25/δ).
| 0   |     | w∈Rd |     |     |     |     |     |     | t ,∅ | b 2 ε | 2   |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | ---- | ----- | --- | --- | --- |
(cid:80)
e m p ir i c a l c a s e an d s im i l a r ly f o r th e p o p u l a t i o n l o s s w h e n 6: ∇ ,∅ = 1 ∇f(w t,∅;x) + g t,∅, where
|     |     |     |     |     |     |     |     |     | t b | x ∈ S t,∅ |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- |
d i sc u s s i n g s t a t io n a r y p o i n t s o f t h e p o p u la t i o n l o s s . W e u s e (cid:0) ,I (cid:1)
|     |     |     |     |     |     |     |     |     | g ∅ ∼ N 0 | σ 2 | .   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
w ∗ t o d e n o t e t h e p o p u la t i o n r i s k m i n i m i z e r . F i n a l l y , w e u s e t, d t ,∅
|              |     |     |     |     |     |     |     | 7:  | foru ∈DFS[D]do |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
| thenotationI |     |     |     |     |     |     |     |     | t,s            |     |     |     |     |
d todenotethed×didentitymatrixanduse
|     |     |     |     |     |     |     |     | 8:  | Lets=sc,wherec∈{0,1}. (cid:98) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- |
[a]todenotetheset{1,2,...,a}fora≥1.
|                   |     |                                |     |     |     |     |     | 9:  | ifc=0then |             |     |     |     |
| ----------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | --- | --- |
|                   |     |                                |     |     |     |     |     |     | ∇ =∇      |             |     |     |     |
|                   |     |                                |     |     |     |     |     | 10: | t,s       | t,s(cid:98) |     |     |     |
| Stationarypoints: |     | GivenadatasetS,ourgoalistofind |     |     |     |     |     |     |           |             |     |     |     |
|                   |     |                                |     |     |     |     |     | 11: | w =w      |             |     |     |     |
an α-stationary point w¯ of either empirical or population t,s t,s(cid:98)
|              |            |            |     |        |            |     |      | 12: | else        |     |        |                 |     |
| ------------ | ---------- | ---------- | --- | ------ | ---------- | --- | ---- | --- | ----------- | --- | ------ | --------------- | --- |
| r is k ; f o | rm a l ly, | ∥∇F(w¯;S)∥ |     | ≤ α or | ∥∇F(w¯;D)∥ |     | ≤ α, |     |             |     | b      |                 |     |
|              |            |            |     |        |            |     |      | 13: | DrawabatchS |     | t,s of | datapoints,setS | ←   |
| re s p ec t  | iv el y .  |            |     |        |            |     |      |     |             |     | 2| s|  |                 |     |
|              |            |            |     |        |            |     |      |     | S\S         | .   |        |                 |     |
t,s
8·2Dβ2log(1.25/δ).
|                                           |     |     |     |     |     |         |     | 14: | Setnoisevarianceσ2 |                | :=  |      |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | ------------------ | -------------- | --- | ---- | --- |
| DifferentialPrivacy(DP)(Dworketal.,2006): |     |     |     |     |     | Analgo- |     |     |                    |                | t,s | b2ε2 |     |
|                                           |     |     |     |     |     |         |     |     |                    | 2| s| (cid:80) |     |      |     |
rithm A is (ε,δ)-differentially private if for all datasets 15: ∆ = (∇f(w ;x)−∇f(w ;x))+
|                 |           |        |       |            |           |            |     |     | t,s       | b      |             | t,s           | t,s(cid:98) |
| --------------- | --------- | ------ | ----- | ---------- | --------- | ---------- | --- | --- | --------- | ------ | ----------- | ------------- | ----------- |
|                 | S′        |        |       |            |           |            |     |     |           | x∈St,s |             |               |             |
| S and           | differing | in     | one   | data point | and       | all events |     |     |           |        |             |               |             |
|                 |           |        |       |            |           |            |     |     | g ,whereg | ∼N     | (cid:0) 0,I | σ 2 (cid:1) . |             |
| E in the        | range     | of the | A, we | have,      | P(A(S)∈E) |            | ≤   |     | t,s       | t,s    |             | d t ,s        |             |
| eεP(A(S′)∈E)+δ. |           |        |       |            |           |            |     | 16: | ∇ t,s =∇  | +∆     | t,s .       |               |             |
t,s(cid:98)
|     |     |     |     |     |     |     |     | 17: | endif |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
if|s|=D(i.e,u
GeneralizedLinearModels(GLMs): Fordatadomain 18: t,s isaleaf)then
| ⊆RdandY            |     | ⊆R,alossfunctionf |                         |     | :Rd×X×Y | →Ris |     | 19: | if∥∇    | ∥≤2α˜then |     |     |     |
| ------------------ | --- | ----------------- | ----------------------- | --- | ------- | ---- | --- | --- | ------- | --------- | --- | --- | --- |
| X                  |     |                   |                         |     |         |      |     |     | t,s     |           |     |     |     |
|                    |     |                   |                         |     |         |      |     | 20: | Returnw |           |     |     |     |
| aGLMiff(w;(x,y))=ϕ |     |                   | (⟨w,x⟩)forsomefunctionϕ |     |         |      | .   |     |         | t,s       |     |     |     |
|                    |     |                   | y                       |     |         |      | y   |     |         |           |     |     |     |
|                    |     |                   |                         |     |         |      |     | 21: | endif   |           |     |     |     |
OurresultforGLMsusesrandommatriceswhichsatisfy
|                                                        |     |     |     |     |     |     |     | 22: | Letu | bethenextvertexinDFS[D]. |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------------------ | --- | --- | --- |
| theJohnson-Lindenstrauss(JL)property,definedasfollows. |     |     |     |     |     |     |     |     | t,s+ |                          |     |     |     |
β
|     |     |     |     |     |     |     |     | 23: | Setη | :=  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
Definition2.1((γ,β)-JLproperty). ArandommatrixΦ∈ t,s 2D/2L1 ∥∇t,s∥
|     |     |     |     |     |     |     |     |     | w =w | −η  | ∇   | .   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
Rk×d satisfies (γ,β)-JL property if for any u,v ∈ Rd, 24: t,s+ t,s t,s t,s
| P[|⟨Φu,Φv⟩−⟨u,v⟩|>γ∥u∥∥v∥]≤β. |     |     |     |     |     |     |     | 25: | endif  |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
|                               |     |     |     |     |     |     |     | 26: | endfor |     |     |     |     |
27: endfor
3.StationaryPointsofPopulationRisk
|     |     |     |     |     |     |     |     | 28: Returnw,chosenuniformlyatrandomfrom{w |     |     |     |     | :t∈ |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- |
t,s
|          |               |           |       |             |          |               |     | [T],u | isaleaf}. |     |     |     |     |
| -------- | ------------- | --------- | ----- | ----------- | -------- | ------------- | --- | ----- | --------- | --- | --- | --- | --- |
| For the  | population    | gradient, |       | we provide  | a linear | time          | al- |       | t,s       |     |     |     |     |
| gorithm; | see Algorithm |           | 1 for | pseudocode. |          | It is a noisy |     |       |           |     |     |     |     |
variantofSPIDER(Fangetal.,2018),andutilizesavari- On the other hand, when a right child node is visited, it
ancereductiontechniquetailoredtoanunderlyingbinary receives a fresh set of samples and uses it to update the
tree structure. Namely, we run T rounds, where at the gradient estimator coming from the parent node. Every
beginning of round t we build a binary tree of depth D, time a leaf node is reached, a gradient step is performed
,wheres∈{0,1}D.
whosenodesaredenotedbyu t,s Every usingthegradientestimatorassociatedtotheleaf. Finally,
node u is associated with a parameter vector w and theparametervectorofarightchildnodecomesfromthe
|     | t,s |     |     |     |     | t,s |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
agradientestimate∇ . Next,weperformaDepth-First- gradientstepperformedattheright-mostleafintheleftsub-
t,s
4

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
treeofit. Theuseofthebinarytreestructureisbenefitial worksbyrunningaseriesofphasesoflengthq. Eachphase
becauseeverygradientestimatorisupdatedatmostDtimes startswithaminibatchestimateofthegradient,andsubse-
withinaroundof2D optimizationsteps,asopposedtothe quentgradientestimateswithinthephasearethencomputed
originalSPIDERalgorithmwherethegradientestimators byaddinganestimateofthegradientvariation. Thekeyto
areupdatedateveryoptimizationstep.Thisway,weareable theanalysisistoboundtheerrorinthegradientestimate
toperformthesamenumberofoptimizationstepsbutadding ateachiteration. Towardsthisend,wehavethefollowing
substantiallysmalleramountsofnoise,leadingtoafaster generalizationofthe(Wangetal.,2019c)Lemma1,which
ratethantheonewewouldgetwithoutusingthetree. Inthe followsdirectlyfrom(Fangetal.,2018)Proposition1.
following,wedenotebyℓ(k)thebinaryrepresentationof Lemma 4.1. Consider Algorithm 2, and for any t ∈
anynumberk ∈[0,2D−1]andby|s|thedepthofu t,s for {0,..,T} let s = (cid:106) t (cid:107) q. If each ∇ computed in
anyt∈[T]. t q t
line 9 is an unbiased estimate of ∇F(w ;S) satisfying
t
(cid:104) (cid:105)
The proposed algorithm is similar to the one in Section E ∥∇ −∇F(w ;S)∥2 ≤ τ2 and each ∆ computed
5 of (Bassily et al., 2021b) for constrained Differentially
st st 1 t
inline13isanunbiasedestimateofthegradientvariation
Private-Stochastic Convex Optimization (DP-SCO), with (cid:104) (cid:105)
satisfying E ∥∆ −[∇F(w ;S)−∇F(w ;S)]∥2 ≤
the key difference that Algorithm 1 executes each round t t t−1
with fixed depth trees, which is key for our convergence τ2∥w −w ∥2. Then for any t ≥ s +1, the iterates
2 t t−1 t
analysis,whereasthepriorworkleveragesconvexitytocon- ofAlgorithm2satisfy
struct trees that increase depth by one at each round. In
t
addition,tochoosethestep-sizein(Bassilyetal.,2021b) E(cid:2) ∥∇ −∇F(w )∥2(cid:3) ≤τ2 (cid:88) E(cid:2) ∥w −w ∥2(cid:3) +τ2.
t t 2 k k−1 1
theauthorsleveragetheboundeddiameterofthedomain,
k=st+1
whileourstep-sizeischosenasthatof(Fangetal.,2018),
i.e.normalizedbythenormofthegradientestimatorand Forprivacy,usingsmoothnessweobservethesensitivityof
proportionaltothetargetaccuracy. Thischoiceiscrucial thegradientvariationestimateatiterationtisproportional
forcontrollingthesensitivityofthegradientvariationesti- to β∥w −w ∥. Thus we can apply the above lemma
t t−1
matorintheunconstrainedsetting,andconsequentlyforthe withτ2 = L2 0 +L2σ2andτ2 = L2 1 +L2σ2(notetheGaus-
privacyanalysisaswell. Ourresultsarepresentedbelow 1 b1 0 1 2 b2 1 2
siannoiseinline13isdrawnwithvariancescaleatmost
andtheproofsaredeferredtoAppendixC. σ2∥w −w ∥2). By carefully balancing the algorithm
2 t t−1
Theorem 3.1 (Privacy guarantee). For any ε,δ ∈ [0,1], parameters,wearethenabletoobtainthefollowingresult.
Algorithm1is(ε,δ)-DP. ThefullproofisdeferredtoAppendixB.1.
Theorem3.2(Accuracyguarantee). Letp∈(0,1),ε,δ > Theorem4.2(PrivateSpiderboostERM). Letε,δ ∈[0,1].
(cid:110) √ (cid:111) (cid:26) √ √ (cid:27)
0, b = max n2/3, n √ d1/4 , D be such that D2D+1 = Let n ≥ max (L0ε)2 , dmax{1, L1F0/L0 } . Al-
ε √ √ F0L1dlog(1/δ) ε
b, T = n , α = 2L max (cid:8) 1 , (cid:0) d(cid:1)1/2(cid:9) , gorithm 2 is (ε,δ)-DP. Further, there exist settings of
b(D/2+1) 0 n1/3 nε
β = αmin{1, √ √bε}, and α˜ = C˜α, where C˜ = T,η,q,b 1 ,b 2 such that Algorithm 2 has E[∥∇F(w¯;S)∥]
256log (cid:0)1.25(cid:1) log (cid:16) 2 d T2D+1 (cid:17) + 8L1F0 √ 2D(D/2+1). Then, boundedas
δ √ p 2L2 0 (cid:32)√ (cid:112) (cid:33)2/3 (cid:112) 
foranyn≥max{ d(D +1)2/ε,(D +1)3},withproba- F 0 L 1 L 0 dlog(1/δ) L 0 dlog(1/δ)
2 2 O + 
bility1−p,Algorithm1endsinline20,returninganiterate nε nε
w with
t,s
∥∇F(w ;D)∥≤3 √ 2L C˜max (cid:110) 1 , (cid:16) √ d(cid:17)1/2(cid:111) . andoraclecomplexityO˜ (cid:18) max (cid:26)(cid:16) n5 d / 1 3 / ε 3 2/3 (cid:17) , (cid:16) √nε d (cid:17)2 (cid:27)(cid:19) .
t,s 0 n1/3 nε
Note that the restriction on n in the theorem statement
is essentially trivial when the upper bound is nontrivial.
Furthermore,Algorithm1hasoraclecomplexityofn.
We remark that the case where the dominant error term
isα = O˜ (cid:16)(cid:2) √ d(cid:3)2/3 (cid:17) , thenweapproximatelyhaveoracle
4.StationaryPointsofEmpiricalRisk nε
complexityO˜(cid:0) max (cid:8) 1 ,n(cid:9)(cid:1) .
α3 α
4.1.EfficientAlgorithmwithFasterRate
4.2.LowerBound
Thealgorithmforourupperboundisanoisyversionofthe
SpiderBoostalgorithm(Wangetal.,2019c)8.Thealgorithm Wenowshowalowerboundforthesamplecomplexityof
findingastationarypointunderdifferentialprivacyintheun-
8SpiderBoostitselfisessentiallytheSpideralgorithm(Fang √
etal.,2018)withadifferentlearningrateandanalysis. constrainedsetting,whichshowsthattheO
(cid:0)L0 dlog(1/δ)(cid:1)
nε
5

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
Algorithm2 PrivateSpiderBoost ProofofTheorem4.3. For any r > 0, let W denote the
r
Input: Dataset: S ∈ Xn, Function: f : Rd ×X (cid:55)→ R, ballofradiusrcenteredattheorigin.LetB = L L 0 1 .Consider
Learning Rate: η, Phase Size: q, Batch Sizes b ,b , thelossfunction:
1 2
PrivacyParameters: (ε,δ),Iterations: T (cid:40) L1 ∥w−x∥2 if∥w−x∥≤B
1: w 0 =0 √ f(w;x)= 2
2: σ 1 = cL0 l ε og(1/δ) max (cid:110) b 1 1 ,√ √ q T n (cid:111) , wherecisauni- L 0 ∥w−x∥− 2 L L 2 0 1 otherwise
versalcon√stant.
(cid:110) √ (cid:111)
3: σ 2 = cL1 √ l ε og(1/δ) max b 1 2 , n T T L h is e pc f h u it n z c i t n io R n d. f W (w e ; r x e ) str i i s ctt c o on d v a e ta x s , ets L S 1 -s = m { o x oth }n and wh L er 0 e -
4 5 : : σ f (cid:98) o 2 r = t= 2c 0 L , 0 .. ε l . o , g T (1/ d δ o ) max (cid:110) b 1 2 , √ n T (cid:111) x be i t ∈ he W em B p /4 iri f c o a r l a ri l s l k i, o a n n S d . le T t h F e ( u w nc ; o S n ) st = rain n 1 e (cid:80) dm n i i = in i 1 = i f m 1 ( i w ze ; r x o i f )
6: if mod (t,q)=0then F(w;S)isw∗ = n 1 (cid:80)n i=1 x i whichliesinW B/4 .
7: SamplebatchS t ofsizeb 1 Foranyw ∈W 3B/4 ,wliesinthequadraticregionaround
8: Sampleg t ∼N(0,I d σ 1 2) alldatapoints. Hence,fromL 1 -strongconvexityofw (cid:55)→
9: ∇ t = b 1 1 (cid:80) x∈St ∇f(w t ;x)+g t F(w;S)onW 3B/4 ,wehavethatwheneverw¯ ∈W 3B/4 ,
10: else
∥∇F(w¯;S)∥∥w¯−w∗∥≥⟨∇F(w¯;S),w∗−w¯⟩
11: SamplebatchS t ofsizeb 2
12: g t ∼N (cid:16) 0,I d min (cid:110) σ 2 2∥w t −w t−1 ∥2,σ (cid:98)2 2 (cid:111)(cid:17) ≥F(w¯;S)−F(w∗;S)
13: ∆ t = b 1 2 (cid:80) x∈St [∇f(w t ;x)−∇f(w t−1 ;x)]+g t ≥ L 2 1 ∥w¯−w∗∥2.
14: ∇ t =∇ t−1 +∆ t LetE betheeventthatw¯ ∈W 3B/4 andletE E denotethe
15: endif conditionalexpectation(conditionedoneventE)operator.
16: w t+1 =w t −η∇ t Then,
17: endfor
L
18: returnw¯uniformlyatrandomfrom{w 1 ,...,w T } E ∥∇F(w¯;S)∥≥ 1E∥w¯−w∗∥
E 2
(cid:32)(cid:18) (cid:19) (cid:32) (cid:112) (cid:33)(cid:33)
L L dlog(1/δ)
≥ 1Ω 0 min 1, .
termintherategiveninTheorem4.2isnecessary. Further- 2 4L nε
1
more,asourlowerboundholdsforalllevelsofsmoothness,
italsoshowsthatourrateinTheorem4.2isoptimalinthe wherethelastinequalityfollowsfromknownlowerbounds
√
(admittedly uncommon) regime where L
1
≤
F0
d
n
L
ε
2 0. Our forDPmeanestimation(Steinke&Ullman,2015;Kamath
lowerboundinfactholdsevenforconvexfunctions. Fur- &Ullman,2020). Weremarkthatthelowerboundinthe
thermore,thisresultimpliesthesamelowerbound(upto referencedworkisforalgorithmswhichproduceoutputs
logfactors)forthepopulationgradientusingthetechnique in the ball of the same radius as the dataset, i.e. W .
B/4
in(Bassilyetal.,2019),AppendixC. However, a simple post-processing argument shows that
Theorem4.3. GivenL ,L ,n,ε = O(1),2−Ω(n) ≤ δ ≤ thesamelowerboundappliestoalgorithmswhichproduce
0 1
1/n1+Ω(1), there exists an L -Lispchitz, L -smooth (con- outputinW 3B/4 . Specifically,assumingthecontrary,we
0 1
vex) loss f : Rd ×X → R and a dataset S of n points simply project the output in W 3B/4 to W B/4 : privacy is
preservedbypost-processingandthedistancetothemean
suchthatany(ε,δ)-DPalgorithmrunonS withoutputw¯
cannotincreasebythenon-expansivenesspropertyofpro-
satisfies,
jection to convex sets, hence a contradiction. This gives
(cid:32) (cid:32) (cid:112) (cid:33)(cid:33) us,
dlog(1/δ)
∥∇F(w¯;S)∥=Ω L min 1, .
0 nε (cid:32) (cid:32) (cid:112) (cid:33)(cid:33)
dlog(1/δ)
E [∥∇F(w¯;S)∥]≥Ω L min 1,
E 0 nε
TheproofisbasedonareductiontoDPmeanestimation.
Specifically,weconsiderainstanceoftheHuberlossfunc-
tionforwhichtheminimizeristheempiricalmeanofthe Let W˜ = {w :∥w−w∗∥≤B/2}. Since W˜ ⊆ W ,
3B/4
dataset. We then argue that close to the minimizer, the wehavethattheaboveconditionallowerboundappliesfor
empirical stationarity is lower bounded by DP mean esti- w¯ ∈ W˜ as well. We now consider w¯ ̸∈ W˜. Let w′ be
mationbound(Steinke&Ullman,2015),andfaraway,by any point on the boundary of W˜, denoted as ∂W. Note
construction,theempiricalstationarityisL . that w′ lies in the region where, for any data point, the
0
6

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
|     |     |     |     |     |     |     |     |     |     |     | (cid:16)(cid:0)F0τ2τ1 |     | (cid:1)1/3 | (cid:17) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | ---------- | -------- |
correspondinglossisaquadraticfunction. Hence,bydirect satisfies E[∥∇L(A(O))∥] = Ω + √τ1 . If
G
| computation,∇F(w′;S)=L |     |     |     | (w′−w∗). |     | Therefore, |     |     |              |                   |     |            |           | G   |
| ---------------------- | --- | --- | --- | -------- | --- | ---------- | --- | --- | ------------ | ----------------- | --- | ---------- | --------- | --- |
|                        |     |     |     | 1        |     |            |     | O   | is a private | oracle satisfying | the | previously | mentioned |     |
conditions,wewouldthenhaveunderthesettingofτ
|     |                  |     |     |         |     | L B2 |     |     |                                                  |     |     |     |     | 1 and |
| --- | ---------------- | --- | --- | ------- | --- | ---- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | ----- |
|     | ⟨∇F(w′),w′−w∗⟩=L |     |     | ∥w′−w∗∥ |     | 2 1  |     |     |                                                  |     |     |     |     |       |
|     |                  |     |     | 1       |     | =    | .   | τ   | suggestedbyprivacythattheconvergenceguaranteefor |     |     |     |     |       |
|     |                  |     |     |         |     | 4    |     | 2   |                                                  |     |     |     |     |       |
E[∥∇L(A(O))∥]islowerboundedas
Wenowapplygradientmonotonicitytoobtainthefollowing
| (seeLemmaA.1,AppendixA), |     |             |     |     |      |      |     | (cid:32)√ |     |                     | (cid:33)2/3 |     |           |    |
| ------------------------ | --- | ----------- | --- | --- | ---- | ---- | --- | ---------- | --- | ------------------- | ----------- | --- | --------- | --- |
|                          |     |             |     |     |      |      |     |            |     | (cid:112)           |             |     | (cid:112) |     |
|                          |     |             |     |     |      |      |     |            | F   | 0 L 1 L 0 dlog(1/δ) |             | L 0 | dlog(1/δ) |     |
|                          |     |             |     |     |      |      |     | Ω         |     |                     |             | +   |           | .  |
|                          |     |             |     | L   | B2 2 | L    |     |            |     | nε                  |             |     | nε        |     |
|                          | E   | ∥∇F(w¯;S)∥≥ |     | 1   | ·    | = 0, |     |            |     |                     |             |     |           |     |
Ec
|     |     |     |     |     | 4 B | 2   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whereEcdenotesthecomplementsetofE.Wecombinethe
Thisindicatesasubstantialchallengeforfuturerateimprove-
aboveboundsusingthelawoftotalexpectationasfollows,
ments,asalternativemethodswhichavoidprivategradients
E[∥∇F(w¯;S)∥] (seee.g. (Feldmanetal.,2020))relycruciallyonstability
=E [∥∇F(w¯;S)∥]P{w¯∈E}+E Ec[∥∇F(w¯;S)∥]P{w¯∈Ec} guaranteesarisingfromconvexity.
E
(cid:112)
|     | (cid:16) | (cid:110) | dlog(1/δ)(cid:111)(cid:17) |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------- | --------- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
=Ω L min 1, P(w¯∈E)+Ω(L )P(w¯∈Ec) 5.StationaryPointsintheConvexSetting
|     | 0   |     | nε  |     |     | 0   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:112)
|     | (cid:16) | (cid:110) | dlog(1/δ)(cid:111)(cid:17) |     |     |     |     |                                   |                                  |     |     |     |     |           |
| --- | -------- | --------- | -------------------------- | --- | --- | --- | --- | --------------------------------- | -------------------------------- | --- | --- | --- | --- | --------- |
| =Ω  | L min    | 1,        |                            | .   |     |     |     |                                   |                                  |     |     |     |     |           |
|     | 0        |           | nε                         |     |     |     |     | Algorithm3RecursiveRegularization |                                  |     |     |     |     |           |
|     |          |           |                            |     |     |     |     | Input:                            | DatasetS,lossfunctionf,stepsT,{λ |     |     |     | t } | ,{R t } , |
|     |          |           |                            |     |     |     |     |                                   |                                  |     |     |     | t   | t         |
Thiscompletestheproof. PrivateSubRoutine, number of steps of sub-routine
|                                       |              |        |     |          |        |               |     |     | {K },selectorfunctions{S |     | (·)} | ,stepsize{η | }   | ,noise |
| ------------------------------------- | ------------ | ------ | --- | -------- | ------ | ------------- | --- | --- | ------------------------ | --- | ---- | ----------- | --- | ------ |
|                                       |              |        |     |          |        |               |     |     | t                        |     | t    | t           | t   | t      |
| ChallengesforFurtherRateImprovements: |              |        |     |          |        | Giventhe      |     |     | variances{σ              | }   |      |             |     |        |
|                                       |              |        |     |          |        |               |     |     |                          | t t |      |             |     |        |
| abov                                  | e lower      | bound, | the | question | arises | as to whether | the | 1:  | w =0,n                   | =1  |      |             |     |        |
|                                       | √            |        |     |          |        |               |     |     | 0                        | 0   |      |             |     |        |
| O˜(cid:0)(cid:2)                      | d]2/3(cid:1) |        |     |          |        |               |     |     |                          |     |      | f(0)(w;x)   |     |        |
termcanbeimproved. Aninformalargument 2: Define function (w,x) (cid:55)→ = f(w;x) +
nε
| usingtheoraclecomplexitylowerboundof(Arjevanietal., |     |     |     |     |     |     |     |     | λ 0 ∥w−w | ∥2  |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
|                                                     |     |     |     |     |     |     |     |     | 2        | 0   |     |     |     |     |
2019)suggestsseveralmajorchallengesinobtainingfurther fort=1toT −1do
3:
(cid:106) (cid:107)
rateimprovements.Amoredetailedversionofthefollowing 4: n =n + | S|
|     |     |     |     |     |     |     |     |     | t   | t−1 T |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
discussioncanbefoundinAppendixB.2.
|     |     |     |     |     |     |     |     |     | w¯  | = PrivateSubRoutine(S |     |         | ,f(t−1),R | ,   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | ------- | --------- | --- |
|     |     |     |     |     |     |     |     | 5:  | t   |                       |     | nt−1:nt |           | t   |
Considermethodswhichensureprivacybydirectlypriva- K ,η ,S (·),σ )
|     |     |     |     |     |     |     |     |     | t   | t t t |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
tizingthegradient/gradientvariationqueries. Theaimof 6: Define function (w,x) (cid:55)→ f(t)(w;x) =
|     |     |     |     |     |     |     |     |     |     | λ   |     | ∥2  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
suchmethodsistodesignsomeprivatestochasticfirstor- f(t−1)(w;x)+ t ∥w−w¯
|           |           |       |          |            |           |                |       |         |        | 2     |     | t   |     |     |
| --------- | --------- | ----- | -------- | ---------- | --------- | -------------- | ----- | ------- | ------ | ----- | --- | --- | --- | --- |
| der       | oracle,   | O     | , such   | that a set | of G      | queries to     | O     | 7:      | endfor |       |     |     |     |     |
|           |           | ε′,δ′ |          |            |           |                | ε′,δ′ |         |        |       |     |     |     |     |
| satisfies | (ε,δ)-DP, |       | and use  | this       | oracle in | some optimiza- |       |         |        |       |     |     |     |     |
|           |           |       |          |            |           |                |       | Output: | w¯     | =w¯ T |     |     |     |     |
| tion      | algorithm | A(O   | ε′,δ′ ). | Such       | a setup   | encapsulates   | nu-   |         |        |       |     |     |     |     |
merousresultsintheconvexsetting(Bassilyetal.,2019;
Inthissection,weadditionallyassumethatthelossfunction
Kulkarnietal.,2021),andisevenmoredominantinnon-
|     |     |     |     |     |     |     |     | isconvex. |     | Themotivationforthisistwo-fold: |     |     | firstly,this |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------------------------- | --- | --- | ------------ | --- |
convexsettings(Wangetal.,2017;Zhouetal.,2020;Abadi
|     |             |       |          |     |             |       |       | setting | has | recently gained | attention | in a | non-private | set- |
| --- | ----------- | ----- | -------- | --- | ----------- | ----- | ----- | ------- | --- | --------------- | --------- | ---- | ----------- | ---- |
| et  | al., 2016). | Under | advanced |     | composition | based | argu- |         |     |                 |           |      |             |      |
ting(Nesterov,2012;Allen-Zhu,2018;Fosteretal.,2019).
ments,tomakeGcallstosuchaprivateoracleoneneeds √
Secondly,inthissettingweareabletoestablishtightlythe
| ε′ ≤ε/ | G.  | Now,standardfingerprintingcodearguments |     |     |     |     |     |     |     |     |     |     |     |     |
| ------ | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
samplecomplexityofapproximatestationarypoints.
suggestlowerboundsonthelevelofaccuracyofanysuch
privateoracle(Steinke&Ullman,2015). Specifically,with- Ourmethodisbasedontherecursiveregularizationtech-
outleveragingfurtherproblemstructurebeyondLipschitz- niqueproposedin(Allen-Zhu,2018),andfurtherimproved
ness,oneneedsthegradientestimationerrortobeatleast √ by(Fosteretal.,2019).Themainidea,asthenamesuggests,
(cid:16) L0 Gdlog(1/δ) (cid:17) istorecursivelyregularizetheobjectiveandoptimizeitvia
| τ   | =Ω  |     |     | . Asimilarargumentsuggeststhe |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1 nε some solver. For the DP setting, the key idea is to use a
errorinthegradientvariationbetweeniteratesw,w′must
|     |     |     |     |                 | √   |     |          | privatesub-routineastheinnersolver. |     |     |     | Furthermore,whilea |     |     |
| --- | --- | --- | --- | --------------- | --- | --- | -------- | ----------------------------------- | --- | --- | --- | ------------------ | --- | --- |
|     |     |     |     | (cid:16) ∥w−w′∥ |     |     | (cid:17) |                                     |     |     |     |                    |     |     |
at least τ ∥w−w′∥ = Ω L1 Gdlog(1/δ) . Now solverfortheunconstrainedproblemsufficesnon-privately,
2
|     |     |     |     |     | nε  |     |     | weneedtocarefullyincreasetheradiusoftheconstrained |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
considersomeoptimizationalgorithm,A,whichtakesas
setoverwhichthesolveroperates.
| input | a stochastic |     | oracle | O for some | smooth | function | L.  |     |     |     |     |     |     |     |
| ----- | ------------ | --- | ------ | ---------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Thelowerboundof(Arjevanietal.,2019)suggeststhatifA Theorem 5.1. Let L ,L ,ε,δ > 0, d,n ∈ N. Let w (cid:55)→
|     |     |     |     |     |     |     |     |     |     | 0 1 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
makesatmostGqueriestoO(asablackbox)thealgorithm f(w;x)beanL -LipschitzL -smoothconvexfunctionfor
|     |     |     |     |     |     |     |     |     |     | 0   | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
7

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
√
all x. Let R = (cid:0) 2 (cid:1)t ∥w∗∥,λ = 2tλ, η = log(Kt), 6.GeneralizedLinearModels
t t t λtKt
T = (cid:4) log 2 (cid:0)L λ 1 (cid:1)(cid:5) ,σ t 2 = 64L2 0 K n t 2 2ε lo 2 g(1/δ),andS t ({w k } k )= Inthissection,weassumethatthelossfunctionisageneral-
1 (cid:80)Kt (1−η λ )−kw . izedlinearmodel(GLM),f(w;(x,y))=ϕ (⟨w,x⟩).Also,
(cid:80)K
k=
t
1
(1−ηtλt)−k k=1 t t k
assumethenormofdatapointsxarebound
y
edby∥X∥and
1. (Optimal rate) Algorithm 3 run with NoisyGD thefunctionϕ : R → RisL -LipschitzandL -smooth
y 0 1
(Algorithm 7 in Appendix D) as the Pri- forally. Furthermore,letrankdenotetherankofdesign
vateSubRoutine with above parameter set- matrixX ∈Rn×d.
tings and λ = L2 0 min (cid:0)1, d (cid:1) and
L1∥w∗∥ n n2ε2 Algorithm4JLmethod
(cid:18) (cid:16) (cid:17) n2ε2 (cid:16) L2λ+L3/2(cid:17)(cid:19)
K
t
= max L1
λ
+
t
λt log L1
λ
+
t
λt ,
T2λdL2 0
0
log(1
1
/δ)
Inpu
J
t
L
:
m
D
a
a
t
t
r
a
ix
se
Φ
tS
∈
,f
R
u
k
n
×
ct
d
i
,
o
L
n(
,
z
L
,y)
,∥
(cid:55)→
X∥
ϕ
y
(z),AlgorithmA,
satisfies (ε,δ)-DP, and given a dataset S of n i.i.d. 0 1
samplesfromD,outputsw¯suchthat 1: w˜ = A((z,y) (cid:55)→ ϕ y (z),{(Φx i ,y i )}n i=1 ,
2L ∥X∥,2L ∥X∥2,ε,δ/2)
(cid:32) √ (cid:33) 0 1
L L d Output: w¯ =Φ⊤w˜
E∥∇F(w¯;D)∥=O˜ √0 + 0 .
n nε
Algorithm 4 is a generic method which converts any for
Furthermore, the above rate is tight up to poly-
smoothLipschitzlosseswithanempiricalstationarityguar-
logarithmicfactors.
anteetogetdimension-independentratesonpopulationsta-
2. (Linear time rate) Algorithm 3 run with
tionarityforsmoothLipschitzGLMs. Thisalgorithmisthe
PhasedSGD (Algorithm 5) as the PrivateSub-
JL method from (Arora et al., 2022) used therein to give
Routine with with above parameter settings and
λ = max (cid:16) L1∥ L w 2 0 ∗∥2 min (cid:0) n 1, n2 d ε2 (cid:1) ,L1lo n g(n) (cid:17) and e th x e ce J s L s m ris e k th b o o d un th d e s re fo i r s c li o m nv it e e x d G to L t M he . W No e is n y ot G e D tha m t e w th h o il d e ,
K =⌊n⌋satisfies(ε,δ)-DPandgivenadatasetS ofn oursisablack-boxreduction. Furthermore,unlike(Arora
t T
i.i.d. samplesfromD,inlineartime,outputsw¯with etal.,2022),weshowthattheJLmethodgivesfinerrank
(cid:32) √ (cid:33) basedguaranteesbyleveragingthefactitactsasanoblivi-
E∥∇F(w¯;D)∥=O˜ √ L 0 + L 0 d + L 1√ ∥w∗∥ . ousapproximatesubspaceembedding(seeDefinitionE.1in
n nε n AppendixE).
Theorem6.1. LetAbean(ε,δ)-DPalgorithmwhichwhen
The proof of the above result is deferred to Appendix D.
run on a L -smooth L -Lipschitz function on a dataset
1 0
For the √ tightness of the rate, the necessity of the second S = {(x i ,y i )}n i=1 where x i ∈ X ⊆ Rd, guarantees
term L0 d is due to our DP empirical stationarity lower E[∥∇F(A(S);S)∥]≤g(d,n,L ,L ,ε,δ)and∥A(S)∥≤
nε 1 0
bound,Theorem4.3. Forthefirst“non-private”term √L0
n
, poly(n,d,L
0
,L
1
)withprobabilityatleast1− √1
n
. Then,
even though (Foster et al., 2019) proved a sample com- Algorithm4runwith
plexitylowerbound,theirinstanceisnotLipschitzandhas
(cid:24) (cid:18) (cid:18)
d=Ω(nlog(n)),hencenotapplicable.Toremedythis,we k = min argmin g(j,n,2L ∥X∥,2L ∥X∥2,ε,δ/2)
0 1
giveanewlowerboundconstructionwithaLispchitzfunc- j∈N
tionind = 1, TheoremA.2inAppendixA.Thepolylog L ∥X∥log(n) (cid:19) (cid:18) 2n (cid:19)(cid:19)(cid:25)
dependenceonL and∥w∗∥intheupperbounds,isconsis- + 0 √ ,ranklog
1 j δ
tentwiththenon-privatesamplecomplexityin(Fosteretal.,
2019). onaL -Lipschitz,L -smoothGLMloss,is(ε,δ)-DP.Fur-
0 1
thermore, given a dataset of n i.i.d samples from D, its
The second result is a linear time method which has an
additional L ∥w∗∥/
√
n term. Firstly, if the smoothness
outputw¯hasE[∥∇F(w¯;D)∥]boundedas
1
parameterissmallenough,thenthereisnooverhead;this
(cid:18) (cid:19)
L ∥X∥
small-enoughsmoothnessispreciselytheregimeinwhich O˜ 0√ +g(k,n,2L ∥X∥,2L ∥X∥2,ε,δ/2)
n 0 1
wehavelineartimemethodswithoptimalratesforsmooth
DP-SCO(Feldmanetal.,2020). Moreimportantly, (Fos-
ter et al., 2019) showed that even in the non-private set- Theexpressionfork abovecomesfromthesubspaceem-
ting, a polynomial dependence on L ∥w∗∥ is necessary beddingpropertyofJL,andfrombalancingthedimension
1
inthestochasticoraclemodel. However,theoptimalnon- of the embedding with respect to the error of A and the
privateterm,shownin(Fosteretal.,2019),isL ∥w∗∥/n2, approximation error of the JL embedding. The proof is
1
achieved by accelerated methods. Improving this depen- basedonthepropertiesofJLmatrices: oblivioussubspace
dency,ifpossible,isaninterestingdirectionforfuturework. embeddingandpreservationofnorms,togetherwithanew
8

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
uniformconvergenceresultforgradientsofLipschitzGLMs. Asi, H., Feldman, V., Koren, T., and Talwar, K. Private
ThefullproofisdeferredtoAppendixE. stochasticconvexoptimization: Optimalratesinl1geom-
etry. InInternationalConferenceonMachineLearning,
| Below, | we  | instantiate | the | above | with our | proposed algo- |     |     |     |     |     |     |     |
| ------ | --- | ----------- | --- | ----- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
pp.393–403.PMLR,2021.
rithms.
UndertheassumptionsofTheorem6.1,Al- Bassily,R.,Smith,A.,andThakurta,A. Privateempirical
Corollary6.2.
|     |     |     |     |     |     |     | risk minimization: |     | Efficient | algorithms |     | and | tight error |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --------- | ---------- | --- | --- | ----------- |
gorithm4runwithAas
|     |     |     |     |     |     |     | bounds. | In2014IEEE55thAnnualSymposiumonFoun- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------------------------------ | --- | --- | --- | --- | --- |
1. Private Spiderboost (Alg. 2) yields ∥∇F(w¯;D)∥ = dationsofComputerScience,pp.464–473.IEEE,2014.
|     | (cid:18) |     | (cid:18)(cid:16)√ |             | (cid:19)(cid:19) |     |     |     |     |     |     |     |     |
| --- | -------- | --- | ----------------- | ----------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | O˜       |     |                   | (cid:17)2/3 |                  |     |     |     |     |     |     |     |     |
√1 +min rank , 1 . Bassily, R., Feldman, V., Talwar, K., andGuhaThakurta,
|     | n   |     | nε  |     | (nε)2/5 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
A. Privatestochasticconvexoptimizationwithoptimal
2. Algorithm3withNoisyGDasPrivateSubRoutine,un- rates. In Wallach, H., Larochelle, H., Beygelz-
|     | der the | additional | assumption |     | that w | (cid:55)→ f(w;(x,y)) |           |               |     |     |      |         |          |
| --- | ------- | ---------- | ---------- | --- | ------ | -------------------- | --------- | ------------- | --- | --- | ---- | ------- | -------- |
|     |         |            |            |     |        |                      | imer, A., | d'Alche´-Buc, |     | F., | Fox, | E., and | Garnett, |
is convex for all x,y, yields ∥∇F(w¯;D)∥ = R. (eds.), Advances in Neural Information Pro-
|     | (cid:16) |      | (cid:16)√ | (cid:17)(cid:17) |     |     |             |          |        |                      |        |     |             |
| --- | -------- | ---- | --------- | ---------------- | --- | --- | ----------- | -------- | ------ | -------------------- | ------ | --- | ----------- |
|     | O˜       |      | rank,√1   |                  |     |     | cessing     | Systems, |        |                      |        |     |             |
|     | √1       | +min |           |                  | .   |     |             |          | volume | 32.                  | Curran |     | Associates, |
|     | n        |      | nε        | nε               |     |     |             |          |        |                      |        |     |             |
|     |          |      |           |                  |     |     | Inc., 2019. |          | URL    | https://proceedings. |        |     |             |
neurips.cc/paper/2019/file/
Weremarkthattheabovetechniquealsogivesboundson
3bd8fdb090f1f5eb66a00c84dbc5ad51-Paper.
| empiricalstationarity. |             |     | Inparticular,thefirstterm |         |             | √1 ,inthe |      |     |     |     |     |     |     |
| ---------------------- | ----------- | --- | ------------------------- | ------- | ----------- | --------- | ---- | --- | --- | --- | --- | --- | --- |
|                        |             |     |                           |         |             | n         | pdf. |     |     |     |     |     |     |
| above                  | guarantees, |     | is the                    | uniform | convergence | bound and |      |     |     |     |     |     |     |
thesecondtermistheboundonempiricalstationarity. Bassily, R., Guzma´n, C., and Menart, M. Differentially
|     |     |     |     |     |     |     | private stochastic |     | optimization: |     | New | results | in convex |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------------- | --- | --- | ------- | --------- |
andnon-convexsettings.AdvancesinNeuralInformation
Acknowledgements
ProcessingSystems,34,2021a.
| RA  | and | EU are | supported, | in  | part, by NSF | BIGDATA |              |         |     |         |        |     |      |
| --- | --- | ------ | ---------- | --- | ------------ | ------- | ------------ | ------- | --- | ------- | ------ | --- | ---- |
|     |     |        |            |     |              |         | Bassily, R., | Guzman, |     | C., and | Nandi, | A.  | Non- |
awardIIS-1838139andNSFCAREERawardIIS-1943251.
|     |     |     |     |     |     |     | euclidean | differentially |     | private | stochastic |     | convex op- |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | --- | ------- | ---------- | --- | ---------- |
RB’s and MM’s research is supported by NSF CAREER timization. In Belkin, M. and Kpotufe, S. (eds.),
| Award | 2144532 |     | and NSF | Award | AF-1908281. | CG and |             |     |        |        |            |     |           |
| ----- | ------- | --- | ------- | ----- | ----------- | ------ | ----------- | --- | ------ | ------ | ---------- | --- | --------- |
|       |         |     |         |       |             |        | Proceedings | of  | Thirty | Fourth | Conference |     | on Learn- |
TG’sresearchwaspartiallysupportedbyINRIAAssociate
|     |     |     |     |     |     |     | ing Theory, |     | volume | 134 of | Proceedings |     | of Ma- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------ | ------ | ----------- | --- | ------ |
Teamsproject,FONDECYT1210362grant,ANIDAnillo
|     |     |     |     |     |     |     | chine Learning |     | Research, | pp. | 474–499. | PMLR, | 15–19 |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | --- | -------- | ----- | ----- |
ACT210005grant,andNationalCenterforArtificialIntelli-
|                               |     |     |     |     |     |     | Aug 2021b.                  | URL | https://proceedings.mlr. |                             |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | ------------------------ | --------------------------- | --- | --- | --- |
| genceCENIAFB210017,BasalANID. |     |     |     |     |     |     | press/v134/bassily21a.html. |     |                          |                             |     |     |     |
|                               |     |     |     |     |     |     | Bousquet,O.andElisseeff,A.  |     |                          | Stabilityandgeneralization. |     |     |     |
References
TheJournalofMachineLearningResearch,2:499–526,
| Abadi, | M.,      | Chu,         | A., Goodfellow, |          | I., McMahan, | H. B.,      | 2002.                                         |        |               |     |        |     |             |
| ------ | -------- | ------------ | --------------- | -------- | ------------ | ----------- | --------------------------------------------- | ------ | ------------- | --- | ------ | --- | ----------- |
|        | Mironov, | I.,          | Talwar,         | K., and  | Zhang, L.    | Deep learn- |                                               |        |               |     |        |     |             |
|        |          |              |                 |          |              |             | Bun, M.,                                      | Dwork, | C., Rothblum, |     | G. N., | and | Steinke, T. |
|        | ing with | differential |                 | privacy. | In 23rd      | ACM Confer- |                                               |        |               |     |        |     |             |
|        |          |              |                 |          |              |             | Composableandversatileprivacyviatruncatedcdp. |        |               |     |        |     | In          |
enceonComputerandCommunicationsSecurity,CCS
|     |     |     |     |     |     |     | Proceedings | of  | the 50th | Annual | ACM | SIGACT | Sympo- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | ------ | --- | ------ | ------ |
’16,pp.308–318,NewYork,NY,USA,2016.Associa-
siumonTheoryofComputing,STOC2018,pp.74–86,
|     | tionforComputingMachinery.    |     |     |     | ISBN9781450341394. |     |           |     |      |                   |     |     |         |
| --- | ----------------------------- | --- | --- | --- | ------------------ | --- | --------- | --- | ---- | ----------------- | --- | --- | ------- |
|     |                               |     |     |     |                    |     | New York, | NY, | USA, | 2018. Association |     | for | Comput- |
|     | doi: 10.1145/2976749.2978318. |     |     |     | URLhttps://doi.    |     |           |     |      |                   |     |     |         |
org/10.1145/2976749.2978318. ing Machinery. ISBN 9781450355599. doi: 10.1145/
|     |     |     |     |     |     |     | 3188745.3188946. |     | URL | https://doi.org/10. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | ------------------- | --- | --- | --- |
1145/3188745.3188946.
| Allen-Zhu,Z. |        | Howtomakethegradientssmallstochasti- |     |     |     |          |                                              |     |     |     |     |     |       |
| ------------ | ------ | ------------------------------------ | --- | --- | --- | -------- | -------------------------------------------- | --- | --- | --- | --- | --- | ----- |
|              | cally: | Evenfasterconvexandnonconvexsgd.     |     |     |     | Advances |                                              |     |     |     |     |     |       |
|              |        |                                      |     |     |     |          | Carmon,Y.,Duchi,J.C.,Hinder,O.,andSidford,A. |     |     |     |     |     | ”con- |
inNeuralInformationProcessingSystems,31,2018. vexuntilprovenguilty”: Dimension-freeaccelerationof
|     |     |     |     |     |     |     | gradientdescentonnon-convexfunctions. |     |     |     |     | InProceed- |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | ---------- | --- |
Arjevani,Y.,Carmon,Y.,Duchi,J.C.,Foster,D.J.,Srebro,
|     |                   |     |     |                          |     |     | ings of | the 34th | International |     | Conference | on  | Machine |
| --- | ----------------- | --- | --- | ------------------------ | --- | --- | ------- | -------- | ------------- | --- | ---------- | --- | ------- |
|     | N., andWoodworth, |     | B.  | Lowerboundsfornon-convex |     |     |         |          |               |     |            |     |         |
Learning-Volume70,ICML’17,pp.654–663.JMLR.org,
stochasticoptimization,2019.
2017.
Arora, R., Bassily, R., Guzma´n, C., Menart, M., and Ul- Chaudhuri,K.,Monteleoni,C.,andSarwate,A.D. Differ-
lah,E. Differentiallyprivategeneralizedlinearmodels entiallyprivateempiricalriskminimization. Journalof
revisited. arXivpreprintarXiv:2205.03014,2022. MachineLearningResearch,12(Mar):1069–1109,2011.
9

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
Cohen,M.B. Nearlytightoblivioussubspaceembeddings Foster, D.J., Sekhari, A., Shamir, O., Srebro, N., Sridha-
bytraceinequalities.InProceedingsofthetwenty-seventh ran,K.,andWoodworth,B. Thecomplexityofmaking
annualACM-SIAMsymposiumonDiscretealgorithms, thegradientsmallinstochasticconvexoptimization. In
pp.278–287.SIAM,2016. ConferenceonLearningTheory,pp.1319–1345.PMLR,
2019.
| Cutkosky, | A. and | Orabona, | F.  | Momentum-based |     | vari- |     |     |     |     |     |     |
| --------- | ------ | -------- | --- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
ance reduction in non-convex sgd. In Wallach, H., Ge,R.,Lee,J.D.,andMa,T. Matrixcompletionhasnospu-
| Larochelle, | H., | Beygelzimer, |     | A., | d'Alche´-Buc, | F., |     |     |     |     |     |     |
| ----------- | --- | ------------ | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
riouslocalminimum.InLee,D.,Sugiyama,M.,Luxburg,
Fox, E., and Garnett, R. (eds.), Advances in Neural U.,Guyon,I.,andGarnett,R.(eds.),AdvancesinNeural
InformationProcessingSystems,volume32.CurranAs-
InformationProcessingSystems,volume29.CurranAs-
sociates,Inc.,2019. URLhttps://proceedings. sociates,Inc.,2016. URLhttps://proceedings.
| neurips.cc/paper/2019/file/ |     |     |     |     |     |     | neurips.cc/paper/2016/file/ |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- |
b8002139cdde66b87638f7f91d169d96-Paper.
7fb8ceb3bd59c7956b1df66729296a4c-Paper.
| pdf. |     |     |     |     |     |     | pdf. |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
Diakonikolas,J.andGuzma´n,C. Complementarycompos- Ghadimi,S.andLan,G. Stochasticfirst-andzeroth-order
| iteminimization,smallgradientsingeneralnorms,and |     |     |     |     |     |     |     |     |     |     |     | SIAM |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
methodsfornonconvexstochasticprogramming.
applications,2023.
JournalonOptimization,23(4):2341–2368,2013.
| Duchi, J.                        | Lecture     |      | notes | for statistics |                   | 311/elec- |               |        |           |                |                  |     |
| -------------------------------- | ----------- | ---- | ----- | -------------- | ----------------- | --------- | ------------- | ------ | --------- | -------------- | ---------------- | --- |
|                                  |             |      |       |                |                   |           | Ghadimi,      | S. and | Lan, G.   | Accelerated    | gradient methods |     |
| trical                           | engineering | 377. |       | URL:           | https://stanford. |           |               |        |           |                |                  |     |
|                                  |             |      |       |                |                   |           | for nonconvex |        | nonlinear | and stochastic | programming.     |     |
| edu/class/stats311/Lectures/full |             |      |       | notes.         | pdf.              | Last      |               |        |           |                |                  |     |
MathematicalProgramming,156(1):59–99,2016.
visitedon,2:23,2016.
|                      |           |                              |                 |     |             |     | Jain,P.andThakurta,A.                   |     |     | (near)dimensionindependentrisk |              |     |
| -------------------- | --------- | ---------------------------- | --------------- | --- | ----------- | --- | --------------------------------------- | --- | --- | ------------------------------ | ------------ | --- |
| Dwork, C.            | and Roth, | A.                           | The algorithmic |     | foundations | of  |                                         |     |     |                                |              |     |
|                      |           |                              |                 |     |             |     | boundsfordifferentiallyprivatelearning. |     |     |                                | InICML,2014. |     |
| differentialprivacy. |           | FoundationsandTrends®inTheo- |                 |     |             |     |                                         |     |     |                                |              |     |
reticalComputerScience,9(3–4):211–407,2014. Jain,P.,Kothari,P.,andThakurta,A. Differentiallyprivate
|     |     |     |     |     |     |     | onlinelearning. |     | In25thAnnualConferenceonLearning |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------------------------------- | --- | --- | --- |
Dwork,C.,McSherry,F.,Nissim,K.,andSmith,A.Calibrat-
Theory(COLT),pp.24.1–24.34,2012.
| ingnoisetosensitivityinprivatedataanalysis. |     |     |     |     |     | InTheory |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
ofcryptographyconference,pp.265–284.Springer,2006.
Jin,C.,Netrapalli,P.,Ge,R.,Kakade,S.M.,andJordan,
|           |        |          |         |        |     |         | M. I. | A short | note on | concentration | inequalities | for |
| --------- | ------ | -------- | ------- | ------ | --- | ------- | ----- | ------- | ------- | ------------- | ------------ | --- |
| Fang, C., | Li, C. | J., Lin, | Z., and | Zhang, | T.  | Spider: |       |         |         |               |              |     |
Near-optimal non-convex optimization via stochastic randomvectorswithsubgaussiannorm. arXivpreprint
arXiv:1902.03736,2019.
| path-integrated |                 | differential | estimator. |          | In  | Bengio, S., |                       |     |     |                             |     |     |
| --------------- | --------------- | ------------ | ---------- | -------- | --- | ----------- | --------------------- | --- | --- | --------------------------- | --- | --- |
| Wallach,        | H., Larochelle, |              | H.,        | Grauman, |     | K., Cesa-   |                       |     |     |                             |     |     |
|                 |                 |              |            |          |     |             | Kamath,G.andUllman,J. |     |     | Aprimeronprivatestatistics. |     |     |
Bianchi,N.,andGarnett,R.(eds.),AdvancesinNeural
arXivpreprintarXiv:2005.00010,2020.
InformationProcessingSystems,volume31.CurranAs-
sociates,Inc.,2018. URLhttps://proceedings. Kifer,D.,Smith,A.,andThakurta,A. Privateconvexempir-
neurips.cc/paper/2018/file/
icalriskminimizationandhigh-dimensionalregression.
1543843a4723ed2ab08e18053ae6dc5b-Paper. InConferenceonLearningTheory,pp.25–1,2012.
pdf.
|                                  |     |                           |     |     |                   |        | Kulkarni,    | J., Lee, | Y. T.,          | and Liu, D. | Private non-smooth |     |
| -------------------------------- | --- | ------------------------- | --- | --- | ----------------- | ------ | ------------ | -------- | --------------- | ----------- | ------------------ | --- |
| Feldman,V.,Koren,T.,andTalwar,K. |     |                           |     |     | Privatestochastic |        |              |          |                 |             |                    |     |
|                                  |     |                           |     |     |                   |        | erm and      | sco      | in subquadratic | steps.      | In Ranzato,        | M., |
| convexoptimization:              |     | optimalratesinlineartime. |     |     |                   | InPro- |              |          |                 |             |                    |     |
|                                  |     |                           |     |     |                   |        | Beygelzimer, |          | A., Dauphin,    | Y., Liang,  | P., andVaughan,    |     |
ceedingsofthe52ndAnnualACMSIGACTSymposium J.W.(eds.),AdvancesinNeuralInformationProcessing
onTheoryofComputing,pp.439–449,2020.
|            |              |     |     |            |     |         | Systems, | volume      | 34, | pp. 4053–4064.       | Curran | Asso- |
| ---------- | ------------ | --- | --- | ---------- | --- | ------- | -------- | ----------- | --- | -------------------- | ------ | ----- |
|            |              |     |     |            |     |         | ciates,  | Inc., 2021. | URL | https://proceedings. |        |       |
| Foster, D. | J., Sekhari, | A., | and | Sridharan, | K.  | Uniform |          |             |     |                      |        |       |
neurips.cc/paper/2021/file/
| convergence | of  | gradients | for non-convex |     | learning | and |     |     |     |     |     |     |
| ----------- | --- | --------- | -------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
211c1e0b83b9c69fa9c4bdede203c1e3-Paper.
| optimization. | In  | Bengio, | S., | Wallach, | H., | Larochelle, |     |     |     |     |     |     |
| ------------- | --- | ------- | --- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
pdf.
| H., Grauman, |          | K., Cesa-Bianchi, |           |     | N., and     | Garnett, |     |     |     |     |     |     |
| ------------ | -------- | ----------------- | --------- | --- | ----------- | -------- | --- | --- | --- | --- | --- | --- |
| R. (eds.),   | Advances |                   | in Neural |     | Information | Pro-     |     |     |     |     |     |     |
Lan,G. First-orderandstochasticoptimizationmethodsfor
| cessing     | Systems, | volume | 31.                  | Curran |     | Associates, |                  |     |                |     |     |     |
| ----------- | -------- | ------ | -------------------- | ------ | --- | ----------- | ---------------- | --- | -------------- | --- | --- | --- |
|             |          |        |                      |        |     |             | machinelearning. |     | Springer,2020. |     |     |     |
| Inc., 2018. |          | URL    | https://proceedings. |        |     |             |                  |     |                |     |     |     |
neurips.cc/paper/2018/file/ Ma, C., Wang, K., Chi, Y., and Chen, Y. Implicit regu-
59ab3ba90ae4b4ab84fe69de7b8e3f5f-Paper. larizationinnonconvexstatisticalestimation: Gradient
| pdf. |     |     |     |     |     |     | descentconvergeslinearlyforphaseretrievalandmatrix |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
10

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
completion. In Dy, J. and Krause, A. (eds.), Proceed- Wang,D.,Ye,M.,andXu,J. Differentiallyprivateempiri-
ings of the 35th International Conference on Machine calriskminimizationrevisited: Fasterandmoregeneral.
Learning,volume80ofProceedingsofMachineLearn- AdvancesinNeuralInformationProcessingSystems,30,
| ing Research, |     | pp. 3345–3354. | PMLR, | 10–15 | Jul 2018. | 2017. |     |     |     |     |     |     |
| ------------- | --- | -------------- | ----- | ----- | --------- | ----- | --- | --- | --- | --- | --- | --- |
URLhttps://proceedings.mlr.press/v80/
|     |     |     |     |     |     | Wang,D.,Chen,C.,andXu,J. |     |     | Differentiallyprivateem- |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | ------------------------ | --- | --- | --- |
ma18c.html.
piricalriskminimizationwithnon-convexlossfunctions.
Nemirovsky,A.S.andYudin,D.B. Problemcomplexity InProceedingsofthe36thInternationalConferenceon
andmethodefficiencyinoptimization.Wiley-Interscience, Machine Learning, volume 97 of Proceedings of Ma-
1983.
|           |        |         |               |        |         | chine       | Learning | Research,                   | pp. 6526–6535. |     | PMLR, | 09– |
| --------- | ------ | ------- | ------------- | ------ | ------- | ----------- | -------- | --------------------------- | -------------- | --- | ----- | --- |
|           |        |         |               |        |         | 15Jun2019a. |          | URLhttps://proceedings.mlr. |                |     |       |     |
| Nesterov, | Y. How | to make | the gradients | small. | Optima. |             |          |                             |                |     |       |     |
press/v97/wang19c.html.
MathematicalOptimizationSocietyNewsletter,(88):10–
11,2012. Wang, L., Jayaraman, B., Evans, D., and Gu, Q. Effi-
|                         |     |            |                           |              |     | cientprivacy-preservingnonconvexoptimization. |     |     |                      |     |     | CoRR, |
| ----------------------- | --- | ---------- | ------------------------- | ------------ | --- | --------------------------------------------- | --- | --- | -------------------- | --- | --- | ----- |
| Nesterov,Y.andPolyak,B. |     |            | Cubicregularizationofnew- |              |     |                                               |     |     |                      |     |     |       |
|                         |     |            |                           |              |     | abs/1910.13659,2019b.                         |     |     | URLhttp://arxiv.org/ |     |     |       |
| ton method              | and | its global | performance.              | Mathematical |     |                                               |     |     |                      |     |     |       |
abs/1910.13659.
Programming,108:177–205,2006.
|                            |                   |                        |                        |                   |            | Wang,     | Z., Ji,     | K., Zhou, | Y., Liang,  | Y., | and             | Tarokh,  |
| -------------------------- | ----------------- | ---------------------- | ---------------------- | ----------------- | ---------- | --------- | ----------- | --------- | ----------- | --- | --------------- | -------- |
| Rudelson,M.andVershynin,R. |                   |                        | Non-asymptotictheoryof |                   |            |           |             |           |             |     |                 |          |
|                            |                   |                        |                        |                   |            | V.        | Spiderboost | and       | momentum:   |     | Faster          | variance |
| randommatrices:            |                   | extremesingularvalues. |                        |                   | InProceed- |           |             |           |             |     |                 |          |
|                            |                   |                        |                        |                   |            | reduction | algorithms. |           | In Wallach, |     | H., Larochelle, |          |
| ings of                    | the International |                        | Congress               | of Mathematicians |            |           |             |           |             |     |                 |          |
2010 (ICM 2010) (In 4 Volumes) Vol. I: Plenary Lec- H., Beygelzimer, A., d'Alche´-Buc, F., Fox, E., and
|                                               |     |     |     |     |     | Garnett,   | R.  | (eds.),  | Advances in | Neural | Information |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | -------- | ----------- | ------ | ----------- | --- |
| turesandCeremoniesVols.II–IV:InvitedLectures, |     |     |     |     | pp. |            |     |          |             |        |             |     |
|                                               |     |     |     |     |     | Processing |     | Systems, | volume 32.  | Curran | Associates, |     |
1576–1602.WorldScientific,2010.
|     |     |     |     |     |     | Inc., | 2019c. | URL | https://proceedings. |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ------ | --- | -------------------- | --- | --- | --- |
Song,S.,Steinke,T.,Thakkar,O.,andThakurta,A.Evading neurips.cc/paper/2019/file/
thecurseofdimensionalityinunconstrainedprivateglms. 512c5cad6c37edb98ae91c8a76c3a291-Paper.
| InInternationalConferenceonArtificialIntelligenceand |     |     |     |     |     | pdf. |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
Statistics,pp.2638–2646.PMLR,2021.
|     |     |     |     |     |     | Zhang, | J., Zheng, | K., Mou, | W., and | Wang, | L.  | Efficient |
| --- | --- | --- | --- | --- | --- | ------ | ---------- | -------- | ------- | ----- | --- | --------- |
Steinke,T.andUllman,J. Betweenpureandapproximate privateermforsmoothobjectives. InProceedingsofthe
| differentialprivacy. |     | JournalofPrivacyandConfidential- |     |     |     |      |               |       |            |     |            |        |
| -------------------- | --- | -------------------------------- | --- | --- | --- | ---- | ------------- | ----- | ---------- | --- | ---------- | ------ |
|                      |     |                                  |     |     |     | 26th | International | Joint | Conference | on  | Artificial | Intel- |
ity,7,012015. doi: 10.29012/jpc.v7i2.648. ligence, IJCAI’17, pp. 3922–3928. AAAI Press, 2017.
Sun, J., Qu, Q., and Wright, J. A geometric analysis of ISBN9780999241103.
| phaseretrieval.                              |     | In2016IEEEInternationalSymposium |     |     |      |                                                 |     |     |     |                   |     |     |
| -------------------------------------------- | --- | -------------------------------- | --- | --- | ---- | ----------------------------------------------- | --- | --- | --- | ----------------- | --- | --- |
|                                              |     |                                  |     |     |      | Zhang,Q.,Ma,J.,Lou,J.,andXiong,L.               |     |     |     | Privatestochastic |     |     |
| onInformationTheory(ISIT),pp.2379–2383,2016. |     |                                  |     |     | doi: |                                                 |     |     |     |                   |     |     |
|                                              |     |                                  |     |     |      | non-convexoptimizationwithimprovedutilityrates. |     |     |     |                   |     | In  |
10.1109/ISIT.2016.7541725. ProceedingsoftheThirtiethInternationalJointConfer-
Talwar,K.,Thakurta,A.,andZhang,L. Privateempirical enceonArtificialIntelligence,IJCAI-21,pp.3370–3376,
2021.
riskminimizationbeyondtheworstcase:Theeffectofthe
| constraintsetgeometry. |     |     | arXivpreprintarXiv:1411.5417, |     |     |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Zhou,Y.,Chen,X.,Hong,M.,Wu,Z.S.,andBanerjee,A.
| 2014. |     |     |     |     |     | Private | stochastic | non-convex | optimization: |     |     | Adaptive |
| ----- | --- | --- | --- | --- | --- | ------- | ---------- | ---------- | ------------- | --- | --- | -------- |
Talwar, K., Thakurta, A., and Zhang, L. Nearly optimal algorithms and tighter generalization bounds. CoRR,
|               |     |              |     |     |     | abs/2006.13501,2020. |     |     | URLhttps://arxiv.org/ |     |     |     |
| ------------- | --- | ------------ | --- | --- | --- | -------------------- | --- | --- | --------------------- | --- | --- | --- |
| privatelasso. |     | InNIPS,2015. |     |     |     |                      |     |     |                       |     |     |     |
abs/2006.13501.
| Tran, H.  | and Cutkosky, |       | A. Momentum             | aggregation | for           |     |     |     |     |     |     |     |
| --------- | ------------- | ----- | ----------------------- | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| private   | non-convex    | erm.  | In Advances             |             | in Neural In- |     |     |     |     |     |     |     |
| formation | Processing    |       | Systems, volume         | 35.         | Curran As-    |     |     |     |     |     |     |     |
| sociates, | Inc.,         | 2022. | URL https://openreview. |             |               |     |     |     |     |     |     |     |
net/pdf?id=x56v-UN7BjD.
| Wang, D.andXu,                                 |     | J. Differentiallyprivateempiricalrisk |     |     |     |     |     |     |     |     |     |     |
| ---------------------------------------------- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| minimizationwithsmoothnon-convexlossfunctions: |     |                                       |     |     | A   |     |     |     |     |     |     |     |
| non-stationaryview.                            |     | InProceedingsoftheAAAIConfer-         |     |     |     |     |     |     |     |     |     |     |
enceonArtificialIntelligence,volume33,pp.1182–1189,
2019.
11

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
A.Lowerbounds
A.1.MissingdetailsfromDPEmpiricalStationarityLowerBound
ProofofTheorem4.3. Foranyr >0,letW denotetheballofradiusrcenteredattheorigin. LetB = L 0. Considerthe
r
L 1
lossfunction:
|     |     |     |     | (cid:40) L1 ∥w−x∥2 |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
if∥w−x∥≤B
|     |     |     | f(w;x)= | 2   |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
L 2
|     |     |     |     | L ∥w−x∥− | 0   | otherwise |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --------- | --- | --- | --- | --- |
|     |     |     |     | 0        | 2 L |           |     |     |     |     |
1
Thefunctionf(w;x)isconvex,L -smoothandL -LispchitzinRd. WerestricttodatasetsS ={x }n wherex ∈W
|     |     | 1         |     | 0   |     |     |     |     | i   | i B/4 |
| --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | ----- |
|     |     | (cid:80)n |     |     |     |     |     |     | i=1 |       |
for all i, and let F(w;S) = 1 f(w;x ) be the empirical risk on S. The unconstrained minimizer of F(w;S) is
|                  |               | n   | i=1 | i   |     |     |     |     |     |     |
| ---------------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| w∗ = 1 (cid:80)n | x whichliesin | W   | .   |     |     |     |     |     |     |     |
|                  | i             | B/4 |     |     |     |     |     |     |     |     |
| n                | i=1           |     |     |     |     |     |     |     |     |     |
Foranyw ∈W ,wliesinthequadraticregionaroundalldatapoints.Hence,fromL -strongconvexityofw (cid:55)→F(w;S)
|      | 3B/4                  |     |      |     |     |     |     | 1   |     |     |
| ---- | --------------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
| onW  | ,wehavethatwheneverw¯ |     | ∈W   | ,   |     |     |     |     |     |     |
| 3B/4 |                       |     | 3B/4 |     |     |     |     |     |     |     |
L
∥∇F(w¯;S)∥∥w¯−w∗∥≥⟨∇F(w¯;S),w∗−w¯⟩≥F(w¯;S)−F(w∗;S)≥ 1 ∥w¯−w∗∥2.
2
LetE betheeventthatw¯ ∈W andletE denotetheconditionalexpectation(conditionedoneventE)operator. Then,
|     |               | 3B/4 |            | E   |                  |          |          |           |                  |     |
| --- | ------------- | ---- | ---------- | --- | ---------------- | -------- | -------- | --------- | ---------------- | --- |
|     |               |      |            |     | (cid:32)(cid:18) | (cid:19) | (cid:32) | (cid:112) | (cid:33)(cid:33) |     |
|     |               |      | L          |     | L                | L        |          | dlog(1/δ) |                  |     |
|     | E ∥∇F(w¯;S)∥≥ |      | 1E∥w¯−w∗∥≥ |     | 1Ω               | 0        | min 1,   |           | .                |     |
E
|     |     |     | 2   |     | 2   | 4L  |     | nε  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
wherethelastinequalityfollowsfromknownlowerboundsforDPmeanestimation(Steinke&Ullman,2015;Kamath
&Ullman,2020). Weremarkthatthelowerboundinthereferencedworkisforalgorithmswhichproduceoutputsinthe
ballofthesameradiusasthedataset,i.e. W . However,asimplepost-processingargumentshowsthatthesamelower
B/4
boundappliestoalgorithmswhichproduceoutputinW . Specifically,assumingthecontrary,wesimplyprojectthe
3B/4
outputinW toW : privacyispreservedbypost-processingandthedistancetothemeancannotincreasebythe
3B/4 B/4
non-expansivenesspropertyofprojectiontoconvexsets,henceacontradiction. Thisgivesus,
|     |     |     |     |     | (cid:32) (cid:32) |     |     | (cid:33)(cid:33) |     |     |
| --- | --- | --- | --- | --- | ----------------- | --- | --- | ---------------- | --- | --- |
(cid:112) dlog(1/δ)
E
|     |     |     | [∥∇F(w¯;S)∥]≥Ω |     | L min | 1,  |     |     |     |     |
| --- | --- | --- | -------------- | --- | ----- | --- | --- | --- | --- | --- |
|     |     |     | E              |     | 0     |     | nε  |     |     |     |
Let W˜ = {w :∥w−w∗∥≤B/2}. Since W˜ ⊆ W , we have that the above conditional lower bound applies for
3B/4
| W˜  |     |     | W˜. | beanypointontheboundaryofW˜, |     |     |     |     |     |     |
| --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
w¯ ∈ aswell. Wenowconsiderw¯ ̸∈ Letw′ denotedas∂W. Notethatw′
liesintheregionwhere,foranydatapoint,thecorrespondinglossisaquadraticfunction. Hence,bydirectcomputation,
| ∇F(w′;S)=L | (w′−w∗). | Therefore, |     |     |     |     |     |     |     |     |
| ---------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
1
2 L B2
|     |     |     | ⟨∇F(w′),w′−w∗⟩=L |     | ∥w′−w∗∥ |     | = 1 | .   |     |     |
| --- | --- | --- | ---------------- | --- | ------- | --- | --- | --- | --- | --- |
|     |     |     |                  |     | 1       |     | 4   |     |     |     |
WenowapplyLemmaA.1whichgivesus,
B2
|     |     |     |     |             | L 1 | 2   | L 0, |     |     |     |
| --- | --- | --- | --- | ----------- | --- | --- | ---- | --- | --- | --- |
|     |     |     | E   | ∥∇F(w¯;S)∥≥ |     | · = |      |     |     |     |
|     |     |     | Ec  |             | 4   | B   | 2    |     |     |     |
whereEcdenotesthecomplementsetofE.
Wecombinetheaboveboundsusingthelawoftotalexpectationasfollows,
|     | E[∥∇F(w¯;S)∥] |     | E [∥∇F(w¯;S)∥]P{w¯ |     | ∈E}+E |     | [∥∇F(w¯;S)∥]P{w¯ |     | ∈Ec} |     |
| --- | ------------- | --- | ------------------ | --- | ----- | --- | ---------------- | --- | ---- | --- |
|     |               |     | = E                |     |       | Ec  |                  |     |      |     |
(cid:112)
|     |     |     | (cid:16) | (cid:110) | dlog(1/δ)(cid:111)(cid:17) |      |         |     |            |     |
| --- | --- | --- | -------- | --------- | -------------------------- | ---- | ------- | --- | ---------- | --- |
|     |     |     | = Ω L    | min 1,    |                            | P(w¯ | ∈E)+Ω(L |     | )P(w¯ ∈Ec) |     |
|     |     |     |          | 0         |                            |      |         | 0   |            |     |
nε
(cid:112)
|     |     |     | (cid:16) | (cid:110) | dlog(1/δ)(cid:111)(cid:17) |     |     |     |     |     |
| --- | --- | --- | -------- | --------- | -------------------------- | --- | --- | --- | --- | --- |
|     |     |     | = Ω L    | 0 min 1,  |                            | .   |     |     |     |     |
nε
Thiscompletestheproof.
12

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
LetG,R≥0,d∈N.LetW
LemmaA.1. (w )denotetheEuclideanballaroundw ofradiusRandlet∂W (w )denote
|     |     |     | R 0 |     |     | 0   |     | R 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
itsboundary. Letf :Rd →Rbeadifferentiableconvexfunction. Supposew ∈Rdissuchthatforeveryv ∈∂W (w ),
|     |     |     |     |     | 0   |     |     | R 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
G.
| ⟨∇f(v),v−w | 0 ⟩≥G,thenforanyw |     | ̸∈W R (w 0 | ),wehave∥∇f(w)∥≥ |     |     |     |     |
| ---------- | ----------------- | --- | ---------- | ---------------- | --- | --- | --- | --- |
R
Proof. Foraunitvectoru ∈ Rd,definedirectionaldirectivef′(w) = ⟨∇f(w),u⟩. Wefirstshowthatforanyu ∈ Rd :
u
|                   | ∈Rd,thefunctionf′(w′+ru)isnon-decreasinginr |                       |     |     | ∈R        |                                     |     |     |
| ----------------- | ------------------------------------------- | --------------------- | --- | --- | --------- | ----------------------------------- | --- | --- |
| ∥u∥=1andanyw′     |                                             |                       |     |     |           | . Thissimplyfollowsfrommonotonicity |     |     |
|                   |                                             |                       | u   |     |           | +                                   |     |     |
| ofgradientssincef | isconvex.                                   | Inparticular,foranyr′ |     | >r  | >0,wehave |                                     |     |     |
f′(w′+r′u)−f′(w′+ru)=⟨∇f(w′+r′u)−∇f(w′+ru),u⟩
|     | u   | u   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
|     |     |     | =   | ⟨∇f(w′+r′u)−∇f(w′+ru),w′+ru−(w′+ru)⟩ |     |     |     |     |
| --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- |
r′−r
>0
Wenowprovetheclaiminthelemmastatement. Letw ̸∈ ∂W anddefineu = w − w 0 . ThenfromCauchy-Schwarz
|     |     |     |     |     | R   | ∥ w − w 0∥ |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
inequalityandtheabovemonotonicityproperty,wehave,
|     |     | ∥∇f(w)∥≥⟨∇f(w),u⟩=f′(w)≥f′(w |              |     | +Ru)=⟨∇f(w | +Ru),u⟩ |     |     |
| --- | --- | ---------------------------- | ------------ | --- | ---------- | ------- | --- | --- |
|     |     |                              |              | u   | u 0        | 0       |     |     |
|     |     |                              | 1            |     | G          |         |     |     |
|     |     |                              | = ⟨∇f(v),v−w | ⟩≥  |            |         |     |     |
0
|     |     |     | R   |     | R   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
whichfinishestheproof.
A.2.Non-privateSampleComplexityLowerBound
TheoremA.2. ForanyL ,L ,n,d ∈ N,thereexistsadistributionD oversomesetX andaL -Lipschitz,L -smooth
|     |     | 0 1 |     |     |     |     | 0   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
(convex)lossfunctionw (cid:55)→f(w;x)suchthatgivenni.i.dsamplesfromD,theoutputw¯ofanyalgorithmsatisfies,
(cid:18) L (cid:19)
|     |     |     | E∥∇F(w¯;D)∥=Ω |     | √0  |     |     |     |
| --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
n
Proof. Weconstructahardinstanceind=1dimension. Letp∈[0,1]beaparametertobesetlaterandletv ∈{−1,1}be
chosenbyanadversary. LetthedatadomainX ={−1,1}andconsiderthedistributionDonX asfollows:
(cid:40)
|     |     |     |     | 1 withprobability  | 1+vp |     |     |     |
| --- | --- | --- | --- | ------------------ | ---- | --- | --- | --- |
|     |     |     | x=  |                    | 2    |     |     |     |
|     |     |     |     | −1 withprobability | 1−vp |     |     |     |
2
| NotethatE[x]=vp. |     | Considerthelossfunctionf(w;x)as |     |     |            |     |     |     |
| ---------------- | --- | ------------------------------- | --- | --- | ---------- | --- | --- | --- |
|                  |     |                                 |     | L   | L          |     |     |     |
|                  |     |                                 |     |     | 0wx+ 1∆(w) |     |     |     |
f(w;x)=
|     |     |     |     | 2   | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
where∆istheHuberregularizationfunction,definedas,
|     |     |     |     | (cid:40) |w|2 | L0  |     |     |     |
| --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
if |w|≤
|     |     |     | ∆(w)= |     | 2L1 |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- |
L0|w| L2
|     |     |     |     | −   | 0 otherwise |     |     |     |
| --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
L1 4L2
1
Note that the loss function w (cid:55)→ f(w;x) is convex, L -Lipschitz and L -smooth in Rd, for all x. The population risk
|     |     |     |     | 0   | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
functionis,
|     |     |     |     | L   | 0wpv+ L 1∆(w) |     |     |     |
| --- | --- | --- | --- | --- | ------------- | --- | --- | --- |
F(w;D)=
|                                        |     |     |               | 2   | 2                 |     |     |     |
| -------------------------------------- | --- | --- | ------------- | --- | ----------------- | --- | --- | --- |
| Letw¯beoutputsomealgorithmgivenni.i.d. |     |     | samplesfromD. |     | Considertwocases: |     |     |     |
13

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
L0
Case1: |w¯|> : Thegradientnorminthiscaseis
2L1
|     |     |             | (cid:12) L L             | w¯ (cid:12) 2 |      |     |
| --- | --- | ----------- | ------------------------ | ------------- | ---- | --- |
|     |     | |∇F(w¯;D)|2 | (cid:12) 0vp+            | 0 (cid:12)    |      |     |
|     |     |             | = (cid:12)               | (cid:12)      |      |     |
|     |     |             | (cid:12) 2 2|w¯|(cid:12) |               |      |     |
|     |     |             | L2p2 L2                  | L2            |      |     |
|     |     |             | = 0 +                    | 0 + 0         | vpw¯ |     |
|     |     |             | 4 4                      | 2|w¯|         |      |     |
L2 L2
|     |     |     | ≥ 0 − 0p |     |     |     |
| --- | --- | --- | -------- | --- | --- | --- |
4 2
L2 L2
|     |     |     | = 0 − √0 |     |     |     |
| --- | --- | --- | -------- | --- | --- | --- |
|     |     |     | 4 8 n    |     |     |     |
L2
0
≥
8
|     |     | w¯  |     |     |     | √1  |
| --- | --- | --- | --- | --- | --- | --- |
wherethefirstinequalityfollowssincev ≥−1,thethirdequalityfollowsbysettingp= andthesecondinequality
|                                 |     | |w¯| |     |     |     | 16n |
| ------------------------------- | --- | ---- | --- | --- | --- | --- |
| WethereforehavethatE|∇F(w¯;D)|≥ |     |      | L√0 |     |     |     |
followssincen≥1. .
2 2
Case2: |w¯|≤ L0 : Inthiscase,thegradientnormis,
2L1
|     |     |             | (cid:12)   | (cid:12)   | 2   |     |
| --- | --- | ----------- | ---------- | ---------- | --- | --- |
|     |     |             | (cid:12) L | (cid:12)   |     |     |
|     |     | |∇F(w¯;D)|2 | = 0vp+L    | w¯         |     |     |
|     |     |             | (cid:12)   | 1 (cid:12) |     |     |
|     |     |             | (cid:12) 2 | (cid:12)   |     |     |
(cid:16) (cid:17)
Supposethereexistsanalgorithmwithoutputw¯,which,withnsamplesguaranteesthatE|∇F(w¯;D)|<o √L0 . Then
n
|     |     |     |     |     | (cid:16) L2 | (cid:17) |
| --- | --- | --- | --- | --- | ----------- | -------- |
fromMarkov’sinequality,withprobabilityatleast0.9,wehavethat|∇F(w¯;D)|2 <o 0 . Letw˜ =−2L1w¯ ,thenwe
n L0
havethatwithprobabilityatleast0.9,
|     |     |     | (cid:18) L2(cid:19) |     | (cid:18) (cid:19) |     |
| --- | --- | --- | ------------------- | --- | ----------------- | --- |
1
|     | |∇F(w¯;D)|2 | ≤o  | 0 ⇐⇒ |vp−w˜|2 |     | <o  |     |
| --- | ----------- | --- | ------------- | --- | --- | --- |
|     |             |     | n             |     | n   |     |
Thiscontradictsthewell-knownbiasestimationlowerbounds,withp = √1 ,usingLeCam’smethod((Duchi,2016),
16n
|     |     | (cid:16) (cid:17) |     |     |     |     |
| --- | --- | ----------------- | --- | --- | --- | --- |
Example7.7),henceE|∇F(w¯;D)|≥Ω √L0 . Combiningthetwocasesfinishestheproof.
n
B.MissingResultsforEmpiricalStationaryPoints
B.1.PrivateSpiderboost
The following lemma largely follows from the analysis in (Wang et al., 2019c). We present a full proof below for
completeness.
|     |     |     |     |     | (cid:16) | (cid:17) |
| --- | --- | --- | --- | --- | -------- | -------- |
LemmaB.1. LettheconditionsofLemma4.1besatisfied. Letη ≤ 1 andq ≤O 1 . ThentheoutputofPrivate
|     |     |     |     | 2L1 | τ 2η2 |     |
| --- | --- | --- | --- | --- | ----- | --- |
2
SpiderBoost,w¯satisfies
|     |     |                 | (cid:32)(cid:115) |     | (cid:33) |     |
| --- | --- | --------------- | ----------------- | --- | -------- | --- |
|     |     | E[∥∇F(w¯;S)∥]=O |                   | F 0 |          |     |
+τ . (1)
ηT 1
(cid:106) (cid:107)
Proof. Inthefollowing,foranyt∈[T],lets = t q(i.e. theindexcorrespondingtothestartofthephasecontaining
t
q
iterationt).
By a standard analysis for smooth functions we have (recalling that ∇ is an unbiased estimate of ∇F(w ;S) for any
t t
t∈[T])
|         |         | η      |               |     | (cid:18) η L η2(cid:19) |      |
| ------- | ------- | ------ | ------------- | --- | ----------------------- | ---- |
|         |         |        |               | ∥2− | 1                       | ∥2.  |
| F(w t+1 | ;S)≤F(w | t ;S)+ | ∥∇F(w t ;S)−∇ | t   | −                       | ∥∇ t |
|         |         | 2      |               |     | 2 2                     |      |
14

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
TakingexpectationwehavethefollowingmanipulationusingtheupdateruleofAlgorithm2
η (cid:104) (cid:105) (cid:18) η L η2(cid:19) (cid:104) (cid:105)
E[F(w ;S)−F(w ;S)]≤ E ∥∇F(w ;S)−∇ ∥2 − − 1 E ∥∇ ∥2
t+1 t 2 t t 2 2 t
≤ ητ 2 2 (cid:88) t E (cid:104) ∥w −w ∥2 (cid:105) + η E (cid:104) ∥∇ −F(w ;S)∥2 (cid:105)
2 k+1 k 2 st st
k=st+1
(cid:18) η L η2(cid:19) (cid:104) (cid:105)
− − 1 E ∥∇ ∥2
2 2 t
≤ η3τ 2 2 (cid:88) t E (cid:104) ∥∇ ∥2 (cid:105) + ητ 1 2 − (cid:18) η − L 1 η2(cid:19) E (cid:104) ∥∇ ∥2 (cid:105) ,
2 k 2 2 2 t
k=st+1
wherethesecondinequalityfollowsfromLemma4.1andthelastinequalityfollowsfromtheupdaterule. Notethatif
t=s thesumisempty. Summingoveragivenphasewehave
t
E[F(w t+1 ;S)−F(w st ;S)]≤ η3 2 τ 2 2 (cid:88) t (cid:88) k E (cid:104) ∥∇ j ∥2 (cid:105) + (cid:88) t (cid:104) ητ 2 1 2 − (cid:16) η 2 − L1 2 η2 (cid:17) E (cid:104) ∥∇ k ∥2 (cid:105)(cid:105)
k=stj=st+1 k=st
≤ η3τ 2 2 2q (cid:88) t E (cid:104) ∥∇ k ∥2 (cid:105) + (cid:88) t (cid:104) ητ 2 1 2 − (cid:16) η 2 − L1 2 η2 (cid:17) E (cid:104) ∥∇ k ∥2 (cid:105)(cid:105)
k=st k=st
=− (cid:88) t (cid:34)(cid:18) η − L 1 η2 − η3τ 2 2q (cid:19) E (cid:104) ∥∇ ∥2 (cid:105) − ητ 1 2 (cid:35) , (2)
2 2 2 k 2
k=st
(cid:124) (cid:123)(cid:122) (cid:125)
A
wherethesecondinequalitycomesfromthefactthateachgradientappearsatmostqtimesinthesum. Wenowsumoverall
(cid:110) (cid:106) (cid:107) (cid:111)
phases. LetP ={p ,p ,...,}= 0,q,2q,..., T−1 q,T . Wehave
0 1 q
|P|
E[F(w ;S)−F(w ;S)]≤ (cid:88) E(cid:2) F(w ;S)−F(w ;S) (cid:3)
T 0 pi pi−1
i=1
≤− (cid:88) T AE (cid:104) ∥∇ ∥2 (cid:105) + Tητ 1 2 .
k 2
t=0
Rearrangingtheaboveyields
1 (cid:88) T E (cid:104) ∥∇ ∥2 (cid:105) ≤ F 0 + ητ 1 2 . (3)
T k TA 2A
t=0
Nowleti∗denotetheindexofw¯selectedbythealgorithm. Notethat
(cid:104) (cid:105) (cid:104) (cid:105) (cid:104) (cid:105)
E ∥∇F(w ;S)∥2 ≤2E ∥∇F(w ;S)−∇ ∥2 +2E ∥∇ ∥2 . (4)
i∗ i∗ i∗ i∗
15

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
Thesecondtermabovecanbeboundedviainequality(3). ToboundthefirsttermwehavebyLemma4.1that
t∗
E (cid:104) ∥∇ −∇F(w ;S)∥2 (cid:105) ≤τ2 (cid:88) E (cid:104) ∥w −w ∥2 (cid:105) +τ2
i∗ i∗ 2 k k−1 1
k=st∗+1
t∗
=η2τ2 (cid:88) E (cid:104) ∥∇ ∥2 (cid:105) +τ2
2 k 1
k=st∗+1
≤ qη2τ 2 2 (cid:88) T E (cid:104) ∥∇ ∥2 (cid:105) +τ2
T k 1
k=0
τ2η2qF η3qτ2
≤ 2 0 + 2τ2+τ2,
TA 2A 1 1
wherethelastinequalitycomesfrominequality(3)andtheexpectationoveri∗. Pluggingintoinequality(4)onecanobtain
(cid:104) (cid:105) 2F (cid:18) η τ2η3q (cid:19)
E ∥∇F(w ;S)∥2 ≤ 0(1+τ2η2q)+ +2+ 2 τ2. (5)
i∗ TA 2 A A 1
NowrecallA= η − L1η2 − η3τ 2 2q. Sinceq ≤O (cid:16) 1 (cid:17) andη ≤ 1 wehaveA=Θ(η). Thuspluggingintoinequality
2 2 2
(cid:16) (cid:17)
τ
2
2η2 2L1
(5)andagainusingthefactthatq ≤O 1 wehave
τ2η2
2
(cid:104) (cid:105) (cid:18) F (cid:18) τ2η3q (cid:19) (cid:19) (cid:18) F (cid:19)
E ∥∇F(w ;S)∥2 =O 0(1+τ2η2q)+ 3+ 2 τ2 =O 0 +τ2 .
i∗ Tη 2 A 1 Tη 1
TheclaimthenfollowsfromtheJenseninequality.
Forprivacy,wewillrelyonthemomentsaccountantanalysisof(Abadietal.,2016). Thisroughlygivesthesameanalysis
asusingprivacyamplificationviasubsamplingandtheadvancedcompositiontheorem,butallowsforimprovementsin
logfactors. Weprovidethefollowingtheoremimplicitin(Abadietal.,2016)Theorem1below. Thesameresultcanbe
obtainedusingtheanalysisfor(Kulkarnietal.,2021)Theorem3.1whichusesthetruncatedcentraldifferentialprivacy
guaranteesoftheGaussianmechanism(Bunetal.,2018).
TheoremB.2((Abadietal.,2016;Kulkarnietal.,2021)). Letε,δ ∈(0,1]andcbeauniversalconstant. LetD ∈Ynbea
datasetoversomedomainY,andleth ,...,h :Y (cid:55)→Rdbeaseriesof(possiblyadaptive)queriessuchthatforanyy ∈Y,
√1 T
(cid:110) √ (cid:111)
t∈[T],∥h (y)∥ ≤λ . Letσ = cλt log(1/δ) max 1, T . ThenthealgorithmwhichsamplesbatchesofsizeB ,..,B
t 2 t t ε b n 1 t
ofsizebuniformlyatrandomandoutputs 1 (cid:80) h (y)+g forallt∈[T]whereg ∼N(0,Iσ2),is(ε,δ)-DP.
n y∈Bt t t t t
√
WenotethattheoriginalstatementoftheTheoremin(Abadietal.,2016)requiresσ ≥ cλt Tlog(1/δ) andT ≥ n2ε (or
t nε b2
T ≥ n2 solongasε≤1). However,inthecasewhereT ≤ n2 ,onecansimplyconsiderthemetaalgorithmthatdoesrun
b2 b2
T′ = n2 stepsandonlyoutputsthefirstT results. Thisalgorithmisatleastasprivateasthealgorithmwhichoutputsevery
b2 √
result,andunderthesettingT′thescaleofnoiseis 8λt log(1/δ) .
bε
WecannowprovethemainresultforPrivateSpiderboost,restatedbelow. Wenotethatthesettingofb givenbelowwill
2
alwaysbelessthannunderrequiredconditions. Moredetailsareprovidedintheproofbelow.
(cid:26) √ √ (cid:27)
Theorem B.3 (Private Spiderboost). Let n ≥ max
(L0ε)2
,
dmax{1, L1F0/L0 }
. Private Spiderboost
F0L1dlog(1/δ) ε
(cid:36) (cid:40)(cid:18) (cid:19)2/3 (cid:41)(cid:37)
run with parameter settings η =
2L
1
1
, b
1
= n, b
2
= max √
F0L
L
1d
0n
lo
ε
g(1/δ)
,(L
(
0
L
n
1
d
F
l
0
o
)
g
1
(
/
1
6
/
ε
δ
2
)
/
)
3
1/3 , T =
(cid:36) (cid:40)(cid:18) (cid:19)4/3 (cid:41)(cid:37) (cid:106) (cid:107)
max √(F0L1)1/4nε ,√ nε ,andq = n2ε2 satisfies
L0dlog(1/δ) dlog(1/δ) L2 1 Tdlog(1/δ)
(cid:32)(cid:112) (cid:33)2/3 (cid:112) 
F L L dlog(1/δ) dlog(1/δ)L
E[∥∇F(w˜)∥]=O 0 1 0 + 0 
nε nε
16

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
|                                    |     |     |     |     | (cid:18) | (cid:26)(cid:16) | (cid:17) (cid:16) | (cid:17)2 | (cid:27)(cid:19) |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | -------- | ---------------- | ----------------- | --------- | ---------------- | --- | --- | --- | --- | --- |
| is(ε,δ)-DPandhasoraclecomplexityO˜ |     |     |     |     |          | n5/3ε2/3         |                   | √nε       |                  |     |     |     |     |     |
|                                    |     |     |     |     | max      |                  | ,                 |           | .                |     |     |     |     |     |
|                                    |     |     |     |     |          | d1/3             |                   | d         |                  |     |     |     |     |     |
Proof. Forprivacy,werelyonthemomentaccountantanalysisoftheGaussianmechanismasperTheoremB.2. Notethat
eachgradientestimatecomputedinline9haselementswithℓ -normatmostL ,andthisestimateiscomputedatmost T
|     |     |     |     |     |     |     | 2   |     |     | 0   |     |     |     | q   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
times. Similarly,foragradientvariationatsteptinline13wehavenormboundL 1 ∥w t −w t−1 ∥,andhavethatatmostT
suchestimatesarecomputed. Assuch,thescaleofnoiseinbothcasesensurestheoverallalgorithmis(ε,δ)-DPbyTheorem
B.2.
√
dlog(1/δ)
Wenowprovetheconvergenceresult. Tosimplifynotationinthefollowing,wedefineα¯ = . Ifb 1 = n(full
|     |     |     |     |     |     |     |     |     | (cid:16) Tα¯2(cid:17) |     |     | (cid:16) nϵ | (cid:17) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | ----------- | -------- | --- |
|     |     |     |     |     |     |     |     |     | L2                    |     |     | L2          |          |     |
batchgradient),theconditionsofLemma4.1aresatisfiedwithτ2 =O 0 andτ2 =O 1 +L2Tα¯2 andsome
|     |     |     |     |     |     |     |     | 1   | q   |                       | 2   | b2  | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     | (cid:0) L2Tα¯2(cid:1) |     |     |     |     |
settingofqsolongasT ≥qn2 =qandT ≥ n2 . Further,ifb ≥ 1 thenτ2 =O . Thustheconditiononqin
|     |     |     | b2  |     |     | b2  | 2   | Tα¯2 | 2   |     | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
|     |     |     | 1   |     |     | 2   |     |      |     |     |     |     |     |     |
L2
| LemmaB.1issatisfiedwithq |     |     | =   | 1 = | 1 sinceη | =   | 1   |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                          |     |     |     | τ 2 | Tα¯2     | 2L1 |     |     |     |     |     |     |     |     |
2
| PluggingintoEqn. |     | (1)weobtain |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
√
|     |     |     |     |               |     |     | (cid:32)(cid:114) |       |       | (cid:33) |     |     |     |     |
| --- | --- | --- | --- | ------------- | --- | --- | ----------------- | ----- | ----- | -------- | --- | --- | --- | --- |
|     |     |     |     |               |     |     | F                 | L     | L Tα¯ |          |     |     |     |     |
|     |     |     |     | E[∥∇F(w˜)∥]=O |     |     |                   | 0 1 + | 0 √   |          |     |     |     |     |
|     |     |     |     |               |     |     |                   | T     | q     |          |     |     |     |     |
|     |     |     |     |               |     |     | (cid:32)(cid:114) |       |       | (cid:33) |     |     |     |     |
F 0 L 1
|     |     |     |     |     |     | =O  |     | +L  | Tα¯2 | .   |     |     |     | (6) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | T   | 0    |     |     |     |     |     |
We now consider the setting of T. Since q = 1 , it suffices to set T ≥ 1 to ensure T ≥ q. We now set T =
| (cid:26)(cid:16) |     |     | (cid:27) |     |     | Tα¯2 |     |     |     | α¯  |     |     |     |     |
| ---------------- | --- | --- | -------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
√1F0)1/4 (cid:17)4/3
| max (L |     | ,   | 1 . UsingEqn. |     | (6)abovewehave |     |     |     |     |     |     |     |     |     |
| ------ | --- | --- | ------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
α¯
L0α¯
|     |     |     |     |     |     | (cid:18)(cid:16)(cid:112) |     |     |     | (cid:19) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | -------- | --- | --- | --- | --- |
(cid:17)2/3
|     |     |     |     | E[∥∇F(w˜)∥]=O |     |     | F   | L L α¯ | +L  | α¯ . |     |     |     |     |
| --- | --- | --- | --- | ------------- | --- | --- | --- | ------ | --- | ---- | --- | --- | --- | --- |
|     |     |     |     |               |     |     | 0   | 1 0    |     | 0    |     |     |     |     |
Theclaimedratenowfollowsifthereexistsavalidsettingforb satisfyingthepreviouslystatedconditions. Therestrictions
2
|     |     |     |     |     |     |     |     |     |     |     |     | 1/ 3 | 2 / 3 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----- | --- |
on the batch size implied by T imply we need b ≥ √n and thus it suffices to have b ≥ L 0 n α¯ to satisfy this
|     |     |          |     |               |     | 2   |     |     |     |     | 2   | (L F | )1 / 6 |     |
| --- | --- | -------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | ---- | ------ | --- |
|     |     |          |     |               |     |     | T   |     |     |     |     | 1    | 0      |     |
|     |     | (cid:16) |     | (cid:17) 4/ 3 |     |     |     |     |     |     |     |      |        |     |
c o n d it i on s inc e T ≥ ( L √1 F 0 ) 1 / 4 . W e r e c all th a t f o r t h e s et ti n g o f q t o be v ali d w e a ls o r e q u ir e b ≥ 1 a n d
|     |     |     |     |     |     |     |     |     |     |     |     |     | 2 T | α ¯ 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
L 0 α¯
(cid:16) (cid:17) 4 / 3 (cid:16) (cid:17) 2 /3 (cid:26) (cid:16) (cid:17) 2/ 3 (cid:27)
|     | (L √1F | ) 1/ 4 |     |     |     | L   |     |     |     |     |     | L   | L 1/ 3 | n α¯ 2 / 3 |
| --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------- |
b e ca u s e T ≥ 0 i t s u ffi c e st ha t b 2 ≥ √ 0 . T h u s w e n e ed b 2 = m a x √ 0 , 0 .
|     |     | L α¯ |     |     |     | F   | L α¯ |     |     |     |     | F L      | α¯ (L 1 F   | 0 ) 1 / 6 |
| --- | --- | ---- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | -------- | ----------- | --------- |
|     |     | 0    |     |     |     |     | 0 1  |     |     |     |     | 0        | 1           |           |
|     |     |      |     |     |     |     |      |     |     |     |     | (cid:16) | (cid:17)2/3 |           |
L
Finally, we need b 2 ≤ n whenever q ≥ 1. Note that by the setting of q and T we have q ≤ √ 0 and thus
F 0L 1α¯
(cid:16)√
|     |     | (cid:17) |     |     |     |     |     | L 1/3nα¯2/3 |     |     |     |     | (cid:16) (cid:17)2/3 |     |
| --- | --- | -------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | -------------------- | --- |
q ≥ 1 =⇒ L1F0α¯ ≤ 1. Underthissameconditionwehave 0 ≤ n. Wefurtherhave √ L0 ≤ n
|     |     | L0  |     |     |     |     |     | (L1F0)1/6 |     |     |     |     | F0L1α¯ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | ------ | --- |
(L0ε)2
undertheassumptionn≥ giveninthetheoremstatement. Itcanalsobeverifiedthatundertheconditionon
F0L1dlog(1/δ)
ngiveninthetheoremstatementthatq ≥1. Thustheparametersettingsobtaintheclaimedrate.
Notethenumberofgradientcomputationsisboundedby
|     |     | (cid:18) |     | (cid:19) | (cid:32)(cid:18) | (cid:19)4/3      | (cid:40)(cid:18)   | (cid:19)2/3 |                  | (cid:41) | (cid:18) | (cid:19)2/3 | (cid:33) |     |
| --- | --- | -------- | --- | -------- | ---------------- | ---------------- | ------------------ | ----------- | ---------------- | -------- | -------- | ----------- | -------- | --- |
|     |     |          | Tb  |          |                  | nε               |                    | nε          | (nd)1/3          |          | nε       |             |          |     |
|     |     | O Tb     | +   | 1 =O˜    |                  | √ max            |                    | √           | ,                | +n       | √        |             |          |     |
|     |     |          | 2   | q        |                  |                  |                    |             | ε2/3             |          |          |             |          |     |
|     |     |          |     |          |                  | d                |                    | d           |                  |          |          | d           |          |     |
|     |     |          |     |          | (cid:32)         | (cid:40)(cid:18) |                    |             | (cid:41)(cid:33) |          |          |             |          |     |
|     |     |          |     |          |                  |                  | (cid:19)2 n5/3ε2/3 |             |                  |          |          |             |          |     |
|     |     |          |     | =O˜      |                  | nε               |                    |             |                  |          |          |             |          |     |
|     |     |          |     |          | max              | √                | ,                  |             | .                |          |          |             |          |     |
d1/3
d
B.2.AdditionalDiscussionofRateImprovementChallenges
WeheregiveamoredetailedversionoftheinformaldiscussioninSection4.2. Wewanttoemphasizethatthegoalofthe
followingdiscussionisnottoprovideauniversallowerbound,butrathertoinformfutureresearch.
17

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
| Rd  | Rbealossfunction. |     |     |     |     | Rd×(Rd∪⊥) |     | Rd,isa(τ |     |
| --- | ----------------- | --- | --- | --- | --- | --------- | --- | -------- | --- |
LetL : (cid:55)→ WesaytherandomizedmappingO : (cid:55)→ ,τ )-accurate
1 2
| oracleforLif∀w,w′ | ∈Rd               |     |           |     |                         |           |             |     |     |
| ----------------- | ----------------- | --- | --------- | --- | ----------------------- | --------- | ----------- | --- | --- |
|                   | E[O(w,⊥)]=∇L(w),  |     |           |     | E[O(w,w′)]=∇L(w)−∇L(w′) |           |             |     |     |
|                   | O                 |     |           |     | O                       |           |             |     |     |
|                   | (cid:104)         |     | (cid:105) |     |                         | (cid:104) | (cid:105)   |     |     |
|                   | E ∥O(w,⊥)−∇L(w)∥2 |     | ≤τ2,      |     | E                       | ∥O(w,w′)∥ | 2 ≤τ2∥w−w′∥ | 2 . |     |
|                   |                   |     | 1         |     |                         |           | 2           |     |     |
|                   | O                 |     |           |     | O                       |           |             |     |     |
Inshort,Oisanunbiasedandaccurategradient/gradientvariationoracleforL. Define
|     |       |          |             | (cid:110)     |     |     |                | (cid:111) |     |
| --- | ----- | -------- | ----------- | ------------- | --- | --- | -------------- | --------- | --- |
|     | m(G,L | ,L ,τ ,τ | )=infsupinf | α:E[∥∇L(A(O,L |     |     | ,L ,τ ,τ )∥]≤α | ,         |     |
|     |       | 1 0 1    | 2           |               |     |     | 1 0 1 2        |           |     |
A O,L
wherethesupremumistakenoverL -smoothfunctionsLsatisfyingL(0)−argmin{L(w)}≤L ,and(τ ,τ )-accurate
|     |     | 1   |     |     |     |     |     | 0   | 1 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
w∈Rd
oraclesforL. TheinfimumistakenoveralgorithmswhichmakeatmostGcallstoO.
Wehavethefollowinglowerboundonm(i.e.
alowerboundontheaccuracyofoptimizationalgorithmswhichmakeat
mostGqueriestotheoracle)followingfrom(Arjevanietal.,2019,Theorem3)andthefactthattheoraclemodeldescribed
aboveisaspecialcaseofthemulti-queryoraclesconsideredby(Arjevanietal.,2019).
|     |     |     |     |     |     |     | (cid:0)L0 (cid:1)1/3 |     | (cid:16)(cid:2)L (cid:3)2 (cid:17) |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ---------------------------------- |
TheoremB.4((Arjevanietal.,2019)). LetG,L ,L ,τ ,τ ≥0anddefineα= τ2τ1 + √τ1 . Ifd=Ω˜ 0L 1 ,
|           |                  |          | 0 1             | 1 2 |     |     | G   | G         | α 2         |
| --------- | ---------------- | -------- | --------------- | --- | --- | --- | --- | --------- | ----------- |
| thenm(G,L | ,L ,τ ,τ )=Ω(α). |          |                 |     |     |     |     |           |             |
|           | 1 0 1 2          |          |                 |     |     |     |     |           |             |
|           | L                | L(w) = 1 | (cid:80) ℓ(w;x) |     | L   |     | L   | ℓ : Rd ×X | (cid:55)→ R |
Now consider such that for some 0 -Lipschitz and 1 -smooth loss and
n x∈S
S ∈Xn. Weareinterestedindesigningsome(τ ,τ )-accurateanddifferentiallyprivateoracle,O(cid:98),whichcanthenbeused
(cid:98)1 (cid:98)2
byanoptimizationalgorithm,A,toobtainanapproximatestationarypointw¯ =A(O(cid:98),L ,L ,τ ,τ ). Specifically,wewant
|     |     |     |     |     |     |     | 1 0 | (cid:98)1 (cid:98)2 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- |
O(cid:98)tobecapableofansweringGqueriesunder(ε,δ)-DP.Acommonmethodforachievingthisistoensureeachqueryto
Oisatleast(√ε ,δ)-DPanduseadvancedcomposition(orthemorerefinedmomentaccountant)analysis. Suchasetup
G
encapsulatesnumerousresultsintheconvexsetting(Bassilyetal.,2019;Kulkarnietal.,2021),andisevenmoredominant
innon-convexsettings(Wangetal.,2017;Zhouetal.,2020;Abadietal.,2016).
Ourkeyobservationisthatundersuchasetup,anyincreaseinthenumberoforaclecallstoGmustbemetwithaproportional
increaseintheaccuracyparameters(τ ,τ ). Thus,ifsuchanoracle,O(cid:98)isappliedinablackboxfashiontoastochastic
(cid:98)1 (cid:98)2
optimizationalgorithmA,onecanobtainalowerboundontheaccuracyoftheoverallalgorithmindependentofG.
Specifically,sinceestimatingthegradientandgradientvariationcanbeviewedasmeanestimationproblemsonnvectors,
wecanusefingerprintingcodeargumentstolowerboundτ andτ (Steinke&Ullman,2015). InLemmaB.5below,we
|     |     |     |     | (cid:98)1 | (cid:98)2 |     |     |          | √        |
| --- | --- | --- | --- | --------- | --------- | --- | --- | -------- | -------- |
|     |     |     |     |           |           |     |     | (cid:16) | (cid:17) |
)-accurateoraclewhichensuresthatanyqueryis(√ε L0 Gd l og(1/δ)
provethatany( τ (cid:98)1 ,τ (cid:98)2 ,δ)-DPmusthaveτ (cid:98)1 = Ω
|     | √        |          |     |     |     | G   |     |     | n ε |
| --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
|     | (cid:16) | (cid:17) |     |     |     |     |     |     |     |
L1 Gdlog(1/δ)
| andτ =Ω   |         | . Now,observethatbyTheoremB.4,wehave |            |               |     |             |             |     |     |
| --------- | ------- | ------------------------------------ | ---------- | ------------- | --- | ----------- | ----------- | --- | --- |
| (cid:98)2 | nε      |                                      |            |               |     |             |             |     |     |
|           |         |                                      | (cid:32)√ |               |     |             |             |    |     |
|           |         |                                      |            | (cid:112)     |     | (cid:33)2/3 | (cid:112)   |     |     |
|           |         |                                      | F          | L L dlog(1/δ) |     |             | L dlog(1/δ) |     |     |
|           |         |                                      |            | 0 1 0         |     |             | 0           |     |     |
|           | m(G,L 1 | ,L 0 ,τ (cid:98)1 ,τ (cid:98)2       | )=Ω       |               |     |             | +           | ,  |     |
|           |         |                                      |            | nε            |     |             | nε          |     |     |
whichmatchesourupperbound.
We now remark on several ways the above barrier could be circumvented. The first and most obvious possibility is to
employadifferentprivatizationmethodthanprivateoracles. However,thisisparticularlydifficultinthenonconvexsetting
asexistingmethodswhichavoidprivategradients(seee.g. (Feldmanetal.,2020)forseveralsuchmethods)relycrucially
on stability guarantees arising from convexity. Other possible ways to beat the above rate is by designing a stochastic
optimizationalgorithmwhichleveragesthestructureofthenoiseusedinprivateimplementationsoftheoracleormakesuse
|                                   |     |     | (cid:16)(cid:0)L0τ2τ1 | (cid:17)                 |     |     |     |     |     |
| --------------------------------- | --- | --- | --------------------- | ------------------------ | --- | --- | --- | --- | --- |
|                                   |     |     | (cid:1)1/3            | √τ1                      |     |     |     |     |     |
| ofadditionalassumptionstobeattheΩ |     |     |                       | + non-privatelowerbound. |     |     |     |     |     |
|                                   |     |     | G                     | G                        |     |     |     |     |     |
Additional Details on Fingerprinting Bound We conclude by giving a concrete construction for the fingerprinting
argumentmentionedabove.
18

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
LemmaB.5. LetL ,L ≥ 0,ε = O(1),2−Ω(n) ≤ δ ≤ 1 and (cid:112) dlog(1/δ)/(nε) = O(1). Letℓ,L,S satisfythe
0 1 n1+Ω(1)
assumptionsabove. Thenthereexistsℓ,S suchthatforanyoracle,O,whichis(τ ,τ )-accurateforLitholdsthat
1 2
(cid:32) (cid:112) (cid:33) (cid:32) (cid:112) (cid:33)
L dlog(1/δ) L dlog(1/δ)
0 1
τ =Ω and τ =Ω .
1 nε 2 nε
Proof. Inthefollowing,weuseu
j
todenotethej’thcomponentofsomevectoru. LetB = L√0 anddefineh:R(cid:55)→Ras
L1 d
(cid:40)
L1w2 if|w|≤B
h(z)= 2
√L0|w|− L2 0 otherwise
d 2dL1
Define d′ = d (assume d is even for simplicity) and for any vector u ∈ Rd let u(1) = [u ,...,u ]⊤ and u(2) =
2 1 d′
[u ,...,u ]⊤. Defineℓ(w;x)=ℓ (w;x)+ℓ (w;x)where
d′+1 d 1 2
d
ℓ (w;x)= √ L 0 (cid:68) w(1),x(1) (cid:69) , ℓ (w;x)= 1 (cid:88) h(w )x .
1 d 2 2 j j
j=d′+1
LetW ={w :∥w∥ ≤B}andnoteforanyw ∈W wehave
∞
x x
∇ℓ(w;x)=[√1 ,...,√d′ ,w x ,...,w x ]⊤, ∇2ℓ (w;x)=L ·Diag(0,...,0,x ,...,x )
d′+1 d′+1 d d 2 1 d′+1 d
d d
Thatis,theHessianofℓ (w;x)isadiagonalmatrixwithentriesfromx. Thusonecanobservethatforanyx∈{±1}dwe
2
havethatℓ(·;x)isL -LipschitzandL -smoothoverRd.
0 1
Toprovealowerboundonτ andτ ,itsufficestoshowthatforany(ε,δ)-DPimplementationofOthereexistsw ∈Rd
1 2
(cid:104) (cid:105) (cid:104) (cid:105)
suchthatE ∥O(w;⊥)−∇L(w)∥2 ≥ τ2 andthereexistw,w′ ∈ Rd suchthatE ∥O(w,w′)∥2 ≥ τ2∥w−w′∥2. For
1 2
O O
sakeofgenerality,wewillshowthatthesepropertiesholdforasetofw,w′.
Notethattolowerboundthegradienterror,itsufficestolowerboundtheerrorwithrespecttothefirstd′components. We
thusargueusingℓ ,andwillinfactshowalowerboundforanyw ∈Rd. Letw ∈Rd. Wehaveforany(ε,δ)-DPoracleO
1
thereexistsadatasetS ⊆{±1}d,where|S|=n,offingerprintingcodessuchthat
(cid:34)(cid:13) (cid:13)(cid:35) (cid:32) (cid:112) (cid:33)
E[∥O(w;⊥)−∇L(w)∥]≥E (cid:13) (cid:13)O(w;⊥)(1)− 1 (cid:88) x(1) (cid:13) (cid:13) =Ω L 0 dlog(1/δ) .
O O (cid:13) (cid:13) n (cid:13) (cid:13) nε
x∈S
Theboundfollowsfromstandardfingerprintingcodearguments. See(Bassilyetal.,2014,Lemma5.1)foralowerbound
(cid:112)
and(Steinke&Ullman,2015,Theorem1.1)foragroupprivacyreductionthatobtainstheadditional log(1/δ)factor.This
(cid:18) √ (cid:19)
fingerprintingresultalsoinducestheparameterconstraintsinthetheoremstatement. Wethushaveτ =Ω
L0 dlog(1/δ)
.
1 nε
Similarly,wewillargueaboundonthegradientvariationusingℓ . Letw,w′ ∈W andu=(w−w′)(2). Inwhatfollows,
2
we only use the second half of the components for each vector, and thus omit the superscript (2) from all vectors for
readability. Wehave∇ℓ
2
(w;x)−∇ℓ
2
(w′;x) = L
1
[u
1
x
1
,...,u
d′
x
d′
]⊤. Thenforanyc ∈ (0, 2L√0 ]andu ∈ {±c}2 we
L1 d
19

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
have
|     |                          |           |          |         |              |          |     |                    |           |     |
| --- | ------------------------ | --------- | -------- | -------- | ------------ | -------- | --- | ------------------- | --------- | --- |
|     |                          |           |          | d′       | (cid:32)     |          |     | (cid:33)2           |           |     |
|     | (cid:104)                | (cid:105) |          | (cid:88) |              |          | u   | (cid:88)            |           |     |
| E   | ∥O(w,w′)−(∇L(w)−∇L(w′))∥ | 2         | =L2      | ·E       | O(w,w′)      |          | − j | x                   |           |     |
|     |                          |           | 1        |         |              |          | j   | j                  |           |     |
| O   |                          |           |          | O        |              |          | n   |                     |           |     |
|     |                          |           |          | j=1      |              |          |     | x∈S                 |           |     |
|     |                          |           |          |         |              |          |     |                     |          |     |
|     |                          |           |          | d′       | (cid:32)     |          |     |                     | (cid:33)2 |     |
|     |                          |           |          | (cid:88) | (cid:16)O(w  | ,        | w′) | 1 (cid:88) (cid:17) |           |     |
|     |                          |           | =L2      | ·E       | u            |          | j − | x                   |           |     |
|     |                          |           | 1        |         | j            |          |     | j                   |          |     |
|     |                          |           |          | O        |              | u        |     | n                   |           |     |
|     |                          |           |          | j=1      |              |          | j   | x∈S                 |           |     |
|     |                          |           |          |         |              |          |     |                     |          |     |
|     |                          |           |          |          | d′ (cid:32)  |          |     | (cid:33)2           |           |     |
|     |                          |           |          |          | (cid:88) O(w | , w′)    |     | 1 (cid:88)          |           |     |
|     |                          |           | =L2      | ·E c2   |              |          | j − | x                   |           |     |
|     |                          |           | 1        |          |              |          |     | j                   |          |     |
|     |                          |           |          | O        |              | u        |     | n                   |           |     |
|     |                          |           |          |          | j=1          | j        |     | x∈S                 |           |     |
|     |                          |           | (cid:18) |          |              | (cid:19) |     |                     |           |     |
d2log(1/δ)
|     |     |     | =Ω  | L2c2 |     |     | ,   |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
1
n2ε2
wherethelaststepagaincomesfromfingerprintingresults. Notethattheextrafactorofdascomparedtotheprevious
√
boundcomesfromthefactthatweareconsideringfingerprintingcodeswithnormlargerbyafactorof d. Wealsousethe
∥w −w′∥
factthatthevectorO(w,w′)transformedusinguis(ε,δ)-DPbypostprocessing. Nowsincec= √ wehave
d
|     |     |     |     | (cid:32) |     |     |     | (cid:33) |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | -------- | --- | --- |
(cid:112)
dlog(1/δ)
|     | E[∥O(w,w′)−(∇L(w)−∇L(w′))∥]= |     |     | L   | ∥w−w′∥ |     |     | .   |     |     |
| --- | ---------------------------- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
|     |                              |     |     | 1   |        |     | nε  |     |     |     |
O
√
|     | (cid:104) |     | (cid:105) | (cid:104) |     | (cid:105) |     | (cid:16) |     | (cid:17) |
| --- | --------- | --- | --------- | --------- | --- | --------- | --- | -------- | --- | -------- |
Finally,notingthatE ∥O(w,w′)−(∇L(w)−∇L(w′))∥2 ≤E ∥O(w,w′)∥2 L1 dlog(1/δ)
|     |     |     |     |     |     | weobtainτ |     | 2 =Ω |     | . This |
| --- | --- | --- | --- | --- | --- | --------- | --- | ---- | --- | ------ |
|     | O   |     |     | O   |     |           |     |      | nε  |        |
completestheproof.
Weremarkthattheaccuracylowerboundforthegradientvariationcanholdforamuchmoregeneralsetofvectorsthanthat
Specifically,thesameresultcanbeobtainedforanyu=w−w′suchthatuhasΘ(d)componentswhich
givenintheproof.
(cid:0)∥ u∥(cid:1)
areΩ √ (i.e. anysufficientlyspreadoutvector). Thisusesthefactthatitsufficestoboundthenumberofcomponents
d
whichdisagreeinsignwiththefingerprintingmeanandthatfingerprintingcodesaresampledusingaproductdistribution,
andthusthetracingattackusedbyfingerprintingconstructionsholdsoveranysufficientlylargesubsetofdimensions.
C.MissingResultsforPopulationStationaryPoints
HerewepresenttheproofofprivacyandaccuracyforAlgorithm1. Westartbyprovingtheprivacyguarantee.
ProofofTheorem3.1. Byparallelcompositionofdifferentialprivacy,andsincetheusedbatchesaredisjoint,itsufficesto
provethateachstepinlines6and15ofthealgorithmis(ε,δ)-DP.Notethatthegradientestimatorinstep6hasℓ 2 -sensitivity
2L /b,sobytheGaussianmechanismthisstepis(ε,δ)-DP.
0
|     | andS′ |     |     |     |     |     |     | ̸=x′ |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
Forstep15,supposeS t,s areneighboringdatasetsthatdifferinatmostoneelement: x i∗ ,andletη t,si and
t,s i∗
| η′ therespectivestepsizesusedinstep23. | Then |     |     |     |     |     |     |     |     |     |
| -------------------------------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t,si
2|s|
|     | −∆′ |     |     |     |     | ;x′ |     | ;x′ |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∥∆ t,s t,s ∥= ∥∇f(w t,s ;x i∗ )−∇f(w t,s(cid:98) ;x i∗ )−(∇f(w t,s i∗ )−∇f(w t,s(cid:98) i∗ ))∥,
b
andnotebetweentheparentnodeu andu thereare2D−|s| iteratesgeneratedbythealgorithm,whichwedenoteas
t,s(cid:98) t,s
20

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
w =w ,w ,...,w =w . Then,bysmoothnessoff andthetriangleinequality
t,s(cid:98) t,s0 t,s1 t,s 2|D|−s t,s
∥∆ −∆′ ∥
t,s t,s
2|s|
= ∥∇f(w ;z )−∇f(w ;z )−(∇f(w ;z′ )−∇f(w ;z′ ))∥
b t,s i∗ t,s(cid:98) i∗ t,s i∗ t,s(cid:98) i∗
≤
2D
(cid:88)
−|s|
2|s| (cid:2) ∥∇f(w ;z )−∇f (cid:0) w ;z (cid:1) ∥+∥ (cid:0) ∇f(w ;z′ )−∇f (cid:0) w ;z′ (cid:1)(cid:1) ∥ (cid:3)
b t,si i∗ t,si−1 i∗ t,si i∗ t,si−1 i∗
i=1
2D
(cid:88)
−|s|
2|s|
2D
(cid:88)
−|s|
2|s|
≤ L η ∥∇ ∥+ L η′ ∥∇′ ∥
b 1 t,si−1 t,si−1 b 1 t,si−1 t,si−1
i=1 i=1
2D
(cid:88)
−|s|
2|s| β 2β2D/2
=2 = .
b 2D/2 b
i=1
TheGaussianmechanismcombinedwithourchoiceofσ certifiesprivacyofthisstep.
t,s
ToproveTheorem3.2wewillneedsometechnicallemmas. Define(T,S)asarandomstoppingtimethatindicateswhen
Algorithm1ends. Also,wesay(t ,s )⪯ (t ,s )wheneverw comesbeforew inthealgorithmiterates.
1 1 2 2 2 t1,s1 t2,s2
LemmaC.1(Gradientestimationerror,extensionofLemma6in(Fangetal.,2018)). Letp∈(0,1). Then,withprobability
1−ptheevent
E ={∥∇ −∇F(w ;D)∥2 ≤α·α˜ ∀(t,s)⪯ (T,S)}
t,s t,s 2
holds,undertheparametersettingofσ t,∅,σ
t,s
andη
t,s
inAlgorithm1,for
(cid:18) L2 β2D2D(cid:19) (cid:26) (d+1) (cid:27) (cid:18) 1.25 (cid:19) (cid:18) 2T2D+1(cid:19)
α2 ≥ 0 + max 1, and α˜ ≥256log log α.
b b bε2 δ p
Proof. Recallthegradientestimateassociatedtoaleftchildnodeisthesameasthatoftheparentnode. Hence,thegradient
estimateofanon-leafnodeisthesameasthatoftheleft-mostleafofitsleftsub-tree. Inaddition,weonlyneedtocontrol
the gradient estimation error when we perform a gradient step, which occurs at the leaves. Then, to prove the claim,
itsufficestoprovethatwecancontrolthegradientestimationerrorattheleaves. Since, thenumberofiterations(and
leaves)isatmostT2D−1,toproveeventE happenswithprobability1−p,bytheunionbounditsufficestoprovethat
P[∥∇ −∇F(w ;D)∥2 >α·α˜]≤ p forevery(t,s)⪯ (T,S)whereu isaleaf.
t,s t,s T2D−1 2 t,s
DenotebyF thesigmaalgebrageneratedbyrandomnessinthealgorithmuntiltheendofroundt. Fix(t,s)⪯ (T,S)
t 2
suchthatu isleaf,andletu =u ,u ,...,u =u bethepathfromtheroottos. Next,extractasub-sequence
t,s t,s∅ t,s0 t,s1 t,sk t,s
ofitincludingonlytherootandthenodesthatarerightchildren,obtainingu =u ,u ,...,u =u . Now
t,s∅ t,sa0 t,sa1 t,sam t,s
wecanwrite
m
(cid:88) (cid:88) 1
∇
t,s
−∇F(w
t,s
;D)= g
t,sai
+
b
(∇f(w t,∅;x)−∇F(w t,∅;D))
i=0 x∈St,∅(cid:124) (cid:123)(cid:122) (cid:125)
γ1,x
(cid:88) m (cid:88) 2|sai |(cid:104)(cid:16) (cid:17) (cid:16) (cid:17)(cid:105)
+ ∇f(w ;x)−∇f(w ;x) − ∇F(w ;D)−∇F(w ;D) .
b t,sai t,sai−1 t,sai t,sai−1
i=1x∈St,sai (cid:124)
γ2
(cid:123)
,
(cid:122)
x,i
(cid:125)
Toboundtheestimationerror,wenotethat
P[∥∇ −∇F(w ;D)∥2 >α·α˜|F ]
t,s t,s t−1
(cid:104)(cid:13)(cid:88) m (cid:13)2 α·α˜(cid:12) (cid:105) (cid:104)(cid:13) (cid:88) (cid:88) m (cid:88) (cid:13)2 α·α˜(cid:12) (cid:105)
≤P (cid:13) g (cid:13) > (cid:12)F +P (cid:13) γ + γ (cid:13) > (cid:12)F .
(cid:13) t,sai (cid:13) 4 (cid:12) t−1 (cid:13) 1,x 2,x,i(cid:13) 4 (cid:12) t−1
i=0 x∈St,∅ i=1x∈St,sai
21

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
andproceedtoboundeachtermontherighthandsideseparately. Byvectorsubgaussianconcentration(seeLemma1in
(Jinetal.,2019))andnotingthatthegaussiansareindependentofF ,weknowthat
t−1
(cid:13) (cid:13)(cid:88) m (cid:13) (cid:13) 2 α·α˜  (cid:32) α·α˜ (cid:33)
P  (cid:13) (cid:13)
(cid:13) i=0
g t,sai (cid:13) (cid:13)
(cid:13)
> 4 ≤4dexp − 32(σ
t
2
,∅
+ (cid:80)m
i=1
σ
t
2
,sai
) ,
andinordertoboundthisprobabilityby p ,sincem≤D,itsufficesthat
2T2D−1
(cid:18) 4dT2D(cid:19)(cid:20) 8L2log(1.25/δ) 8D2Dβ2log(1.25/δ) (cid:21)
α·α˜ >32log 0 +
p b2ε2 b2ε2
(cid:18) 1.25 (cid:19)(cid:20) (cid:18) T2D(cid:19)(cid:21)(cid:20) L2 D2Dβ2(cid:21)
=256log dlog(4)+log 0 + .
δ p b2ε2 b2ε2
Now,notingthatsurely
2L 2β2D/2
∥γ ∥≤ 0 and ∥γ ∥≤ ,
1,x b 2,x,i b
where the second bound comes from following similar steps as in the privacy analysis in Theorem 3.1, we have that
(cid:80)
γ +
(cid:80)m (cid:80)
γ isasumofboundedmartingaledifferenceswhenconditionedonF ,thusby
x∈St,∅ 1,x i=1 x∈St,sai 2,x,i t−1
concentrationofmartingale-differencesequencesinℓ (seeProposition2in(Fangetal.,2018)),andusingthefactthat
2
|S t,∅|=band|S
t,sai
|=b/2|sai |itfollowsthat
(cid:13) (cid:13)2   
(cid:13) m (cid:13)
P  (cid:13) (cid:13) (cid:13) (cid:13)x∈ (cid:88) St,∅ γ 1,x + (cid:88) i=1x∈ (cid:88) St,sai γ 2,x,i (cid:13) (cid:13) (cid:13) (cid:13) > α 4 ·α˜ |F t−1   ≤4exp− 16 (cid:104) 4L b 2 0 + α (cid:80) ·α˜ m i=1 2 4 | β s 2 a 2 i D |b (cid:105).
Repeatingasimilarargumentasbefore,toboundthistermby p ,itsufficesthat
2T2D−1
(cid:18) 2T2D+1(cid:19)(cid:20) L2 β2D2D(cid:21)
α·α˜ ≥64log 0 + .
p b b
Finally,bothconditionsholdsimultaneouslyfor
(cid:18) L2 β2D2D(cid:19) (cid:26) (d+1) (cid:27)
α2 ≥ 0 + max 1,
b b bε2
and
(cid:18)
1.25
(cid:19) (cid:18) 2T2D+1(cid:19)
α˜ ≥256log log α.
δ p
LemmaC.2(Descentlemma;Lemma7in(Fangetal.,2018)). UndertheassumptionthattheeventE fromLemmaC.1
occursandβ ≤2D/2α˜,wehavethatifAlgorithm1reachesthelastline,then
β·α˜
F(w ;D)−F(0;D)≤−(T2D−1) .
T,ℓ(2D) 4·2D/2L
1
wherew isthelastiterateintheT-thtreeofAlgorithm1.
T,ℓ(2D)
WeprovidetheproofofLemmaC.2adaptedtoourcaseforcompleteness.
22

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
Proof. Bystandardanalysisforsmoothfunctionswehave
η η
F(w ;D)≤F(w ;D)− t,s(1−η L )∥∇ ∥2+ t,s∥∇ −∇F(w ;D)∥2,
t,s+ t,s 2 t,s 1 t,s 2 t,s t,s
whereη = β andu isthenodeafteru inthetree. Sinceβ ≤ 2D/2α˜ and∥∇ ∥ > 2α˜,wehavethat
t,s 2D/2L1∥∇t,s∥ t,s+ t,s t,s
(1−η L )≥1/2. Usingthisinequality,thedefinitionofη andthefactthatweareassumingE occurs,weobtain
t,s 1 t,s
β β
F(w ;D)−F(w ;D)≤− ∥∇ ∥2+ α·α˜
t,s+ t,s 4·2D/2L ∥∇ ∥ t,s 2·2D/2L ∥∇ ∥
1 t,s 1 t,s
β
≤− ·α˜,
4·2D/2L
1
wherethesecondinequalitycomesfrom∥∇ ∥>2α˜andα≤α˜. ThentelescopingoverallT2D−1iterationsprovidesthe
t,s
claimedbound.
WearenowreadytoprovetheconvergenceguaranteeofAlgorithm1.
ProofofTheorem3.2. FromLemmaC.1,weknowthat∥∇ −∇F(w ;D)∥2 ≤α·α˜withprobability1−pwhen
t,s t,s
α= √ 2L max (cid:26) 1 , (cid:16)√ d (cid:17)1/2 (cid:27) ,α˜ = (cid:16) 256log (cid:0)1.25(cid:1) log (cid:16) 2T2D+1 (cid:17) + 8L1F0 √ 2D(D/2+1) (cid:17) α.
0 n1/3 nε δ p 2L2
0
Indeed,usingourparametersetting,andnotingthatd>bε2ifandonlyif,d>n2/3ε2,yields
L2 (cid:26) (d+1) (cid:27) β2 (cid:26) (d+1) (cid:27)
α2 ≥ 0 max 1, + max 1,
b bε2 2 bε2
(cid:32) 1 √ d (cid:33) α2 (cid:26) bε2(cid:27) (cid:26) (d+1) (cid:27)
=L2 1 + 1 + min 1, max 1,
0 n2/3 {d+1≤n2/3ε2} nε {d+1>n2/3ε2} 2 d bε2
(cid:40) √ (cid:41)
1 d α2
≥L2max , + ,
0 n2/3 nε 2
whichshowsourvaluesofαandα˜arevalidforcontrollingthegradientestimationerrorwithhighprobability,asclaimedin
LemmaC.1.
Now,supposeforthesakeofcontradictionthatAlgorithm1doesnotendinline20underE. ThismeansitperformsT2D−1
gradientupdates. We’llshowthisimplies(T2D−1) β·α˜ > F andthuscontradictsLemmaC.2,whichclaimsthat
4·2D/2L1 0
F ≥−[F(w ;D)−F(w ;D)]≥(T2D−1) β·α˜ . Indeed,notethatbyourparametersetting:
0 T,ℓ(2D) 0,ℓ(2D) 4·2D/2L1
β·α˜ 8L F
(T2D−1) >F ⇐⇒ β·α˜ > 1 0
4·2D/2L 0 T2D/2
1
(cid:40) √ (cid:41) √
bε 8L F 2D
⇐⇒ αmin 1, √ ·α˜ > 1 √0
d T b
√ √ (cid:40) √ (cid:41)
8L F 2D(D/2+1) b d
⇐⇒ α·α˜ > 1 0 max 1,√
n bε
(cid:40)√ √ (cid:41)
√ b d
⇐⇒ α·α˜ >8L F 2D(D/2+1)max , ,
1 0 n nε
23

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
|     |     |     |     |     |     | (cid:110)√ √ | (cid:111) | (cid:110) √ (cid:111) |     |
| --- | --- | --- | --- | --- | --- | ------------ | --------- | --------------------- | --- |
andnotingthatbythesettingofbwehavemax b, d =max 1 , d ,weconcludethefollowing
|     |     |     |     |     |     | n nε |     | n2/3 nε |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | ------- | --- |
√
(cid:40) (cid:41)
|     |     |     |     | β·α˜ |     |     |     | √   | 1 d |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
(T2D−1)
|     |     |     |         |     | >F 0 ⇐⇒ | α·α˜ | >8L | 1 F 0 2D(D/2+1)max | ,       |
| --- | --- | --- | ------- | --- | ------- | ---- | --- | ------------------ | ------- |
|     |     |     | 4·2D/2L |     |         |      |     |                    | n2/3 nε |
1
√
|     |     |     |     |     |     |      | 8L  | 1 F 0 2D(D/2+1) |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --------------- | --- |
|     |     |     |     |     | ⇐⇒  | α·α˜ | >   | α2.             |     |
2L2
0
|     |     |     | (cid:16) |     |         |     |               | √ (cid:17) |     |
| --- | --- | --- | -------- | --- | ------- | --- | ------------- | ---------- | --- |
|     |     |     |          |     | (cid:0) |     | (cid:1) 8L1F0 | 2D(D/2+1)  |     |
Finally,noteα·α˜ = 256log(1.25/δ)log 2T2D+1/p + α2andthusthelastinequalityholdsunder
2L2
0
ourparametersetting. Sincethisisequivalentto(T2D−1) β·α˜ >F ,wearedonewiththecontradiction. Itfollows
|     |     |     |     |     |     |     | 4·2D/2L1 | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
thatwithhighprobability,Algorithm1endsinline20returningw suchthat∥∇ ∥≤2α˜. Also,byLemmaC.1wehave
t,s t,s
∥∇F(w ;D)−∇ ∥<α˜,sothereturnediteratesatisfiesbythetriangleinequality
|     | t,s | t,s |     |     |     |       |           |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --------- | --- | --- |
|     |     |     |     |     |     | ∥∇F(w | ;D)∥<3α˜. |     |     |
t,s
Inaddition,thelineartimeoraclecomplexityfollowsfromthefactthatateachbinarytreeweusebsamplesattheroot,and
thenb/2inlevels1toD. Thisgivesatotalofb(D/2+1)samplesusedateveryround. SincewerunthealgorithmforT =
√
n rounds,wecomputeexactlyngradients.Toconclude,notetheconditionn≥max{ d(D/2+1)2/ε,(D/2+1)3}
b(D/2+1)
impliesthenumberofroundsT isatleast1. Besides,sincethedefinitionofDimplies2D <b,thesizeofthemini-batches
arewell-defined(meaningAlgorithm1usesbatcheswithatleast1sample). Thisconcludestheproof.
D.MissingResultsforStationaryPointsintheConvexSetting
Wefirstgivepseudo-codesofalgorithmsusedinthesection.
Algorithm5PhasedSGD(S,(w,x)(cid:55)→f(w;x)),R,η,S(·),σ)
Input: DatasetS,lossfunctionf(·;x)),radiusRoftheconstraintsetW,stepsT,η,SelectionfunctionS,Noisevariance
σ
1: w =0
1
| 2:  | K =⌈log(|S|)⌉andT |     | =1  |     |     |     |     |     |     |
| --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
0
3: fork =1toK−1do
| 4:  | T =2−k|S|,η |                       | =4−kη,σ |     | =η σ        |      |     |        |     |
| --- | ----------- | --------------------- | ------- | --- | ----------- | ---- | --- | ------ | --- |
|     | k           |                       | k       | k   | k           |      |     |        |     |
|     | w           | =OutputPerturbedSGD(w |         |     | ,S          | ,R,η | ,σ  | ,S(·)) |     |
| 5:  | k+1         |                       |         |     | k Tk−1+1:Tk |      | k   | k      |     |
6: endfor
| Output: | w¯  | =w  |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
K
| Algorithm6OutputPerturbedSGD(w |     |     |     |     | 1 ,S,(w,x)(cid:55)→f(w;x),∆(·),R,η,S(·) |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- |
Input: DatasetS,lossfunctionf(·;x)),regularizer∆(·),radiusRoftheconstraintsetW,stepsT,η,Selectionfunction
S,Noisevarianceσ
1: fort=1to|S|−1do
| 2:  | w t+1 | =Π W (w | t −η(∇f(w | t ;x | t ))) |     |     |     |     |
| --- | ----- | ------- | --------- | ---- | ----- | --- | --- | --- | --- |
3: endfor
ξ ∼N(0,σ2I)
4:
|         | (cid:16) |         | (cid:17) |     |     |     |     |     |     |
| ------- | -------- | ------- | -------- | --- | --- | --- | --- | --- | --- |
|         | w˜ =S    | {w }| S | |        |     |     |     |     |     |     |
| 5:      |          | t t =   | 1        |     |     |     |     |     |     |
| Output: | w¯       | =w˜+ξ   |          |     |     |     |     |     |     |
ProofofTheorem5.1. The privacy guarantee, in both cases, follows from the privacy guarantees of Algorithm 7 and
Algorithm5,inLemmasD.3andD.6respectively,togetherwithparallelcomposition.
24

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
Algorithm7NoisyGD(S,(w,x)(cid:55)→f(w;x)),R,T,η,S(·),σ)
Input: DatasetS,lossfunction(w,x)(cid:55)→f(w;x),radiusRoftheconstraintsetW,stepsT,η,SelectionfunctionS,Noise
varianceσ
1: w 1 =0
2: fort=1toT −1do
3: ξ t ∼N(0,σ2I)
4: w t+1 =Π W (w t −η(∇F(w t ;S)+ξ t ))
5: endfor
(cid:16) (cid:17)
Output: w¯ =S {w }T
t t=1
Wenowproceedtotheutilitypart. Forsimplicityofnotation,letR=∥w∗∥. Recallthedefinitionoftheregularizedlosses
f(t)(w,x)inAlgorithm3. Let{α } besuchthatE[F(t−1)(w¯ ;D)]−F(t−1)(w∗ ;D) ≤ α wherew¯ aretheiterates
t t t t−1 t t
producedinthealgorithmandw∗ =argmin F(t−1)(w;D). Following(Allen-Zhu,2018;Fosteretal.,2019),we
t−1 w∈Rd
firstestablishageneralresultwhichwillbeusefulforbothpartsoftheresult.
(cid:13) (cid:13)
(cid:13) (cid:88) T (cid:13)
E∥∇F(w¯ ;D)∥=E(cid:13)∇F(T−1)(w¯ ;D)+λ 2t(w¯ −w¯ )(cid:13)
T (cid:13) T t T (cid:13)
(cid:13) (cid:13)
t=0
≤E (cid:13) (cid:13) (cid:13) ∇F(T−1)(w¯ T ;D) (cid:13) (cid:13) (cid:13) +λ T (cid:88) −1 2tE(cid:0)(cid:13) (cid:13)w¯ t −w T ∗ −1 (cid:13) (cid:13)+ (cid:13) (cid:13)w¯ T −w T ∗ −1 (cid:13) (cid:13) (cid:1)
t=0
≤2E (cid:13) (cid:13) (cid:13) ∇F(T−1)(w¯ T ;D) (cid:13) (cid:13) (cid:13) +λ T (cid:88) −1 2tE(cid:13) (cid:13)w¯ t −w T ∗ −1 (cid:13) (cid:13)+λE(cid:13) (cid:13)w 0 −w T ∗ −1 (cid:13) (cid:13)
t=1
(cid:13) (cid:13) T (cid:88) −1 (cid:112)
≤2E(cid:13)∇F(T−1)(w¯ ;D)(cid:13)+4 λ2tα +λR
(cid:13) T (cid:13) t T−1
t=1
T−1
(cid:112) (cid:88)(cid:112)
≤4 L α +4 λ2t+1α +λ2T/2R
1 T t
t=1
T
(cid:88)(cid:112) (cid:112)
≤4 λ2t+1α + λL R
t 1
t=1
wherethethirdandfourthinequalityfollowsfromstrongconvexityofF(T−1)(·;D)andLemmaD.2respectively. The
lastinequalityfollowsfromthesettingofT sincewehavethatF(T−1) isL + (cid:80)T−12tλ ≤ L +λ2T ≤ 2L smooth.
(cid:13) (cid:13) 1 t=1 1 1
NotethatthedefinitionofR
t
andLemmaD.1,(cid:13)w
T
∗
−1
(cid:13)≤R
T−1
,sotheunconstrainedm
√
inimizerliesintheconstraintset.
ThereforeE(cid:13)
(cid:13)∇F(T−1)(w¯
T
;D)
(cid:13) (cid:13)=E(cid:13)
(cid:13)∇F(T−1)(w¯
T
;D)−∇F(T−1)(w
T
∗
−1
;D)
(cid:13)
(cid:13)≤2 L
1
α
T
.
ObservethatfromthesettingofT,F(T) is4L smoothforallt. Furthermore,theradiusoftheconstraintsetinthet-th
1
roundisR = 2T/2R. Hence, theLipschitzconstantG ≤ L +8L R ≤ O (cid:0) L +L 2T/2(cid:1) . Nowweinstantiateα ,
t t 0 1 t 0 1 t
whichistheexcesspopulationriskboundoftheDP-SCOsub-routine.
Optimalrate: TheexcesspopulationriskguaranteeofAlgorithm7isinLemmaD.3,with(incontextofthenotationin
theLemma)LipschitzparameterL beingthesameandG =O (cid:0) L 2T/2(cid:1) . Therefore,wehaveα =O˜ (cid:16) G2 + dG2 (cid:17) .
0 ∆ 1 t λtn λtn2ε2
Pluggingintheaboveestimate,weget,
(cid:32) √ (cid:114) (cid:33) (cid:32) √ (cid:33)
G dG λ G dG
E∥∇F(w¯;D)∥=O˜ √ + + R =O˜ √ +
n nε L n nε
1
wherethelaststepfollowsbysettingofλ.
Theoptimalityclaimfollowsbycombiningthenon-privatelowerboundinTheorem5.1,andtheDPempiricalstationarity
lowerboundinTheorem4.3togetherwithareductiontopopulationstationarityasin(Bassilyetal.,2019,AppendixC).
25

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
Lineartimerate: TheexcesspopulationriskguaranteeofAlgorithm5isinLemmaD.6,withLipschitzparameterL
|                  |     |     |                |         |             |                |     | (cid:16)  |          | (cid:17)   |     |     |          | 0   |
| ---------------- | --- | --- | -------------- | ------- | ----------- | -------------- | --- | --------- | -------- | ---------- | --- | --- | -------- | --- |
|                  |     |     |                | (cid:0) | 2T/2(cid:1) |                | =O˜ |           | L 2      | d L 2      |     |     |          |     |
| beingthesameandG |     |     |                | =O L    |             | . Thisgivesusα |     |           | 0 +      | 0 ,andthus |     |     |          |     |
|                  |     |     | ∆              | 1       |             |                | t   |           | λ t n λt | n 2 ε2     |     |     |          |     |
|                  |     |     |                |         |             | √              |     |           |          |            | √   |     |          |     |
|                  |     |     |                |         |             | (cid:32)       |     |           | (cid:33) | (cid:32)   |     |     | (cid:33) |     |
|                  |     |     |                |         |             | L              | dL  | (cid:112) |          | L          |     | dL  | L R      |     |
|                  |     |     | E∥∇F(w¯;D)∥=O˜ |         |             | √ 0 +          | 0 + | λL        | R =O˜    | √ 0        | +   | 0 + | √1       |     |
1
|                                      |     |     |     |     |     | n                                           | nε  |     |     | n   |     | nε  | n                 |      |
| ------------------------------------ | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------------- | ---- |
|                                      |     |     |     |     |     |                                             |     |     |     |     |     |     | (cid:16) (cid:17) |      |
|                                      |     |     |     |     |     | Finally,notethattheLemmaD.6requiresthatn=Ω˜ |     |     |     |     |     |     | L1+λt             |      |
| wherethelaststepfollowsbysettingofλ. |     |     |     |     |     |                                             |     |     |     |     |     |     | forallt.          | This |
λt
| canbecheckedtobesatisfiedbysubstitutingthevalueofλ |     |     |     |     |     |     |     | t . |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
D.1.UtilityLemmas
Wefirstpresentsomekeyresultswhichwillbeusefulintheproofs.
LemmaD.1. Letf : Rd → RbeanL -smoothconvexfunctionandletw∗ = argmin f(w). LetR = ∥w∗∥and
|     |     |     |     |     |             | 1   |     |     |     |     |              | w∈Rd |     |     |
| --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | ------------ | ---- | --- | --- |
|     |     |     |     |     | Definef˜(w) |     |     |     | ∥2  |     | argminf˜(w). |      |     |     |
w ∈ Rd suchthat∥w ∥ ≤ R. = f(w)+ λ∥w−w andletw˜ = Thenforanyλ ≥ 0,
| 0   | √   |     | 0   |     |     |     |     | 2   | 0   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∥w˜∥≤ 2R.
∇f˜(w˜)
Proof. From optimality criterion, 0 = = ∇f(w˜)+λ(w˜−w 0 ). Therefore, ∇f(w˜) = λ(w 0 −w˜) and thus
⟨∇f(w˜),w −w˜⟩>0. Furthermore,sincef isconvex,frommonotonicity,⟨∇f(w˜),w∗−w˜⟩≤0. Sincebothw andw∗
|     |     | 0   |     |     |     |     |     |     |     |     |     |     |     | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
lieintheballofradiusR(sayW ),theabovetwoimpliesthatthehyperplaneH ={w :⟨∇f(w˜),w−w˜⟩=0}intersects
R
withW . Furthermore,since∇f(w˜)=λ(w −w˜),wehavethatw˜istheprojectionofw onH i.e. Π (w ).
|     | R   |     |     |     |     | 0   |     |     |     |     |     | 0   | H 0 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Letw′ =Π (0). Wehavethatw′ ∈W ;thisisbecausethehyperplanecutsthehypersphereW creatingasphericalcap
|     |     | H   |     |     |     | R   |     |     |     |     |     |     | R   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andw′isthecenterofthecap. Frompropertiesofconvexprojections∥Π (w )−Π (0)∥≤∥w −0∥≤R. Furthermore,
|     |     |     |     |     |     |     |     |     | H   | 0   | H   |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Π (0) and Π (w )−Π (0) are orthogonal. Hence ∥w˜∥2 = ∥Π (w )∥2 = ∥Π (0)∥2 +∥Π (w )−Π (0)∥2 ≤
| H   |     | H   | 0   | H   |     |     |     |     | H   | 0   | H   |     | H 0 | H   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2R2.
Westatethefollowingresultfrom(Allen-Zhu,2018;Fosteretal.,2019).
|     |     |     |     |     |     | E[F(t−1)(w¯ |     | ;D)]−F(t−1)(w∗ |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
Lemma D.2. Suppose for every t = 1,2,...T, t ;D) ≤ α t where w¯ t are the iterates
t−1
producedinthealgorithm,w∗ =argmin F(t−1)(w;D)andλ =2tλ,wehave,
|     |                   |     |     | t−1             |              | w∈Rd    |     |     | t   |     |     |     |     |     |
| --- | ----------------- | --- | --- | --------------- | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | Foreveryt≥1,E[    |     |     | (cid:13)        | ∗ (cid:13) 2 | 2 α     |     |     |     |     |     |     |     |     |
| 1.  |                   |     |     | (cid:13)w¯ t −w | (cid:13)     | ]≤ t    |     |     |     |     |     |     |     |     |
|     |                   |     |     |                 | t −1         | λ t − 1 |     |     |     |     |     |     |     |     |
| 2.  | Foreveryt≥1,E[∥w¯ |     |     | −w              | ∗∥2]≤        | α t     |     |     |     |     |     |     |     |     |
|     |                   |     |     | t               | t            | λt      |     |     |     |     |     |     |     |     |
√
|     | E[ (cid:80)T |         | −w∗∥]≤4 |     | (cid:80)T |         |     |     |     |     |     |     |     |     |
| --- | ------------ | ------- | ------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3.  |              | λ t ∥w¯ | t       |     |           | α t λ t |     |     |     |     |     |     |     |     |
|     | t=1          |         |         | T   | t=1       |         |     |     |     |     |     |     |     |     |
D.2.LemmasforNoisyGD(Algorithm7)
Lemma D.3. Consider a function f(w;x) = ℓ(w;x) + ∆(w), where w (cid:55)→ ℓ(w;x) is convex and L Lipschitz for
0
all x, and ∆(w) is λ strongly convex, G ∆ Lipschitz and H ∆ smooth over a bounded convex set W. Algorithm 6 run
|     |     |     |     |     |      |     |     | (cid:18) |     |            |         |            | (cid:19)  |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | -------- | --- | ---------- | ------- | ---------- | --------- | --- |
|     |     |     |     |     | 64L2 |     |     |          |     | (cid:0)L1+ | (cid:1) | n 2 ε2 ( L | 2 + G 2 ) |     |
with parameters η = lo g( T), σ2 = 0 T lo g (1/δ), T = max L1+ H∆ log H∆ , 0 ∆ and S({w } ) =
|     |     |     |     | λ T |     | n2 ε 2 |     |     | λ   |     | λ   | d L 2 l og | ( 1 /δ ) | t t |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | ---------- | -------- | --- |
0
1 (cid:80)T (1−ηλ)−tw satisfies(ε,δ)-DPandgivenadatasetSofni.i.d. pointsfromD,theexcesspopulation
| (cid:80)T | (1−ηλ)−t |     | t=1 |     | t   |     |     |     |     |     |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t=1
riskofitsoutputw¯isboundedby,
|     |     |     |     | (cid:20) |          |     |        | (cid:21) | (cid:18) |             |     | (cid:19) |     |     |
| --- | --- | --- | --- | -------- | -------- | --- | ------ | -------- | -------- | ----------- | --- | -------- | --- | --- |
|     |     |     |     |          |          |     |        |          | L2       | dL2log(1/δ) |     |          |     |     |
|     |     |     |     | E        | F(w¯;D)− | min | F(w;D) | =O       | 0        | + 0         |     | .        |     |     |
λn2ε2
|     |     |     |     |     |     | w∈WR |     |     | λn  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Proof. Fortheprivacyanalysis,asin(Bassilyetal.,2014),forfixedw,thesensitivityofthegradientupdateisboundedby
64L2
2L0. Applyingadvancedcomposition,wehavethatσ2 = 0 Tlog(1/δ) sufficesfor(ε,δ)-DP.
| n   |     |     |     |     |     |     |     | n2ε2 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
}and{w′}besequenceof
Forutility,wefirstcomputeaboundonuniformargumentstabilityofthealgorithm;let{w t
t
iteratesonneighbouringdatasets. Notethatthefunctionw (cid:55)→f(w;x)isL +H -smoothandλ-stronglyconvexforallx.
|     |     |     |     |     |     |     |     |     |     | 1 ∆ |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
FromthesettingofT,wehavethatthestepsizeη ≤ 1 ,hencefromthestandardstabilityanalysis,
L1+H∆
26

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
| w −w′ | =w −η∇L(w | ;S)−η∇∆(w |          |     | )−w′                | +η∇L(w′;S′)+η∇∆(w′) |     |     |
| ----- | --------- | --------- | -------- | --- | ------------------- | ------------------- | --- | --- |
| t+1   | t+1 t     | t         |          | t   | t                   |                     | t   | t   |
|       | =w −w′    | −η(∇L(w   | ;S)+∇∆(w |     | )−∇L(w′;S)−η∇∆(w′)) |                     |     |     |
|       | t         | t         | t        |     | t                   |                     | t   | t   |
+η(∇L(w′;S′)−∇L(w′;S))
|     |              | t              |            | t   |                     |      |     |     |
| --- | ------------ | -------------- | ---------- | --- | ------------------- | ---- | --- | --- |
|     | = (cid:0)I−η | (cid:0) ∇2L(w˜ | ;S)+∇2∆(w˜ |     | ) (cid:1)(cid:1) (w | −w′) |     |     |
|     |              |                | t          |     | t                   | t    | t   |     |
+η(∇L(w′;S′)−∇L(w′;S))
|     |     | t   |     | t   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
wherethelastequalityfollowsfromTaylorremaindertheoremwherew˜ issomeintermediatepointonthelinejoiningw
t t
andw′. Usingthefactthatη ≤ 1 ,wehave
t L1+H∆
|     |              |                   |     |     |     | 2η L | 2 L |     |
| --- | ------------ | ----------------- | --- | --- | --- | ---- | --- | --- |
|     | (cid:13)     | ′ (cid:13)        |     |     | ′∥+ |      | 0 0 |     |
|     | (cid:13)w −w | (cid:13)≤(1−ηλ)∥w |     | −w  |     |      | ≤   |     |
|     | t+1          | t +1              |     | t   | t   | n    | λ n |     |
TheabovegivesthesameboundfortheiterateusingtheselectorS,
2L
|     |     | ∥S({w | })−S({w′})∥≤ |     |     | 0   |     |     |
| --- | --- | ----- | ------------ | --- | --- | --- | --- | --- |
|     |     |       | t            | t   |     | λn  |     |     |
NotethattheoverallLipschitzconstantfortheempiricallossisL˜
|     |     |     |     | 0 =L | 0 +G | ∆ . | Fortheexcessempiricalriskguarantee,we |     |
| --- | --- | --- | --- | ---- | ---- | --- | ------------------------------------- | --- |
useLemma5.2in(Feldmanetal.,2020)toget,
| E[L(w¯;S)+∆(w¯)−L(w∗;S)−∆(w∗)]=E[F |     |     |     |     |     | (w¯;S)−F(w∗;S)]    |     |     |
| ---------------------------------- | --- | --- | --- | --- | --- | ------------------ | --- | --- |
|                                    |     |     |     |     |     | (cid:32) 2(cid:33) |     |     |
L˜
|     |     |     |     |     | =O˜ | 0   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
λT
|     |     |     |     |     |     | (cid:32) L˜ 2 | (cid:33) |     |
| --- | --- | --- | --- | --- | --- | ------------- | -------- | --- |
+σ2d
|     |     |     |     |     | =O˜ | 0   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
λT
|     |     |     |     |     |     | (cid:32) L˜ 2 |     | (cid:33) |
| --- | --- | --- | --- | --- | --- | ------------- | --- | -------- |
dL2log(1/δ)
|     |     |     |     |     | =O˜ | 0   | + 0 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
λn2ε2
λT
|     |     |     |     |     |     | (cid:18) | (cid:19) |     |
| --- | --- | --- | --- | --- | --- | -------- | -------- | --- |
dL2log(1/δ)
|     |     |     |     |     | =O  | 0   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
λn2ε2
wherethelaststepfollowsfromthesettingofT. Forthepopulationriskguarantee,wehave,
E[F(w¯;D)−F(w∗;D)]=E[F(w¯;D)−F(w¯;S)]+E[F(w¯;D)−F(w∗)]
|     |     |                       |     |     |     |     | (cid:18) dL2log(1/δ) | (cid:19) |
| --- | --- | --------------------- | --- | --- | --- | --- | -------------------- | -------- |
|     |     | =E[L(w¯;D)−L(w¯;S)]+O |     |     |     |     | 0                    |          |
λn2ε2
|     |     |     |             |     | (cid:18) | dL2log(1/δ) | (cid:19) |     |
| --- | --- | --- | ----------- | --- | -------- | ----------- | -------- | --- |
|     |     |     | E∥w¯−w¯′∥+O |     |          | 0           |          |     |
≤L 0
λn2ε2
|     |     |     | (cid:18) |             |     | (cid:19) |     |     |
| --- | --- | --- | -------- | ----------- | --- | -------- | --- | --- |
|     |     |     | L2       | dL2log(1/δ) |     |          |     |     |
|     |     | =O˜ | 0 +      | 0           |     |          |     |     |
λn2ε2
λn
wheretheinequalityfollowsfromLipschitznessandstandardgeneralizationgaptostabilityargument.
D.3.LemmasforPhasedSGD(Algorithm5)
Thefollowinglemmagivespopulationriskguaranteesforstronglyconvexfunctionsunderprivacy,intermsofvarianceof
stochasticgradients,asopposedtostandardLipschitznessbounds.
Lemma D.4 (Variance based bound for constant step-size SGD for strongly-convex functions). Consider a func-
tion f(w;x) such that w (cid:55)→ f(w;x) is λ strongly convex, L smooth over a convex set W for all x and let
1
27

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
E ∥∇f(w;x)−E ∇f(w;x)∥2 ≤ V2 for all w ∈ W. Let γ = (1−ηλ)−t. Given a dataset S = {x ,x ,...,x }
x x t 1 2 n
sampledi.i.dfromDandη ≤ 1 asinput,foranyw ∈W,theiteratesofAlgorithm6satisfy
2β
(cid:34) n (cid:35)
E 1 (cid:88) γ F(w ;D) −F(w)≤ λ ∥w −w∥2+ηV2
(cid:80)n γ t t eηλn−1 0
t=1 t t=1
Furthermore,forn=Ω (cid:0)L λ 1 log (cid:0)L λ 1 (cid:1)(cid:1) ,withη = lo λ g( n n) andS({w t } t )= (cid:80)n
t=
1
1
γt (cid:80)n t=1 γ t w t ,theexcesspopulationriskof
w˜ =S({w } )satisfies
t t
(cid:20) (cid:21) (cid:18) V2log(n) (cid:19)
E F(w˜;D)− min F(w;D) =O
w∈W λn
Proof. AnequivalentwaytowritetheupdateinAlgorithm6is
(cid:18) (cid:19)
1
w =argmin ⟨∇f(w ,x ),w⟩+ ∥w −w∥2+ψ(w)
t+1 t t η t
w∈W
whereψ(w)=0ifw ∈W,otherwise∞.
Followingstandardargumentsinconvexoptimization,foranyw ∈W,wehave
F(w ;D)−F(w)
t+1
=F(w ;D)+ψ(w )−F(w;D)−ψ(w)
t+1 t+1
L
≤F(w )+⟨∇F(w ),w −w ⟩+ 1 ∥w −w ∥2+ψ(w )
t t t+1 t 2 t+1 t t+1
+F(w;D)−ψ(w)
λ L
≤⟨∇F(w ),w −w ⟩+⟨∇F(w ),w −w⟩− ∥w −w∥2+ 1 ∥w −w ∥2
t t+1 t t t 2 t 2 t+1 t
+ψ(w )+F(w;D)−ψ(w)
t+1
(cid:20) (cid:21)
L
=E ⟨∇p(w ;z )−∇F(w;D),w −w ⟩+ 1 ∥w −w ∥2+⟨∇p(w ;z ),w −w⟩
zt t t t t+1 2 t+1 t t t t
λ
− ∥w −w∥2+ψ(w )+F(w;D)−ψ(w)
2 t t+1
(cid:104) (cid:18) 1 L (cid:19)
≤E ⟨∇p(w ;z )−∇F(w;D),w −w ⟩− − 1 ∥w −w ∥2
zt t t t t+1 2η 2 t+1 t
(cid:18) 1 λ (cid:19) 1 (cid:105)
+ − ∥w −w∥2− ∥w −w∥2
2η 2 t 2η t+1
(cid:104) η (cid:18) 1 λ (cid:19) 1 (cid:105)
≤E ∥∇p(w ;z )−∇F(w;D)∥2+ − ∥w −w∥2− ∥w −w∥2
zt 2(1−ηL ) t t 2η 2 t 2η t+1
1
(cid:20)(cid:18) (cid:19) (cid:21)
1 λ 1
≤ηV2+E − ∥w −w∥2− ∥w −w∥2
zt 2η 2 t 2η t+1
wherethefirstinequalityfollowsfromsmoothness,thesecondfromstrongconvexity,thethirdfromFactD.1in(Allen-Zhu,
2018),fourthfromAM-GMinequalityandthelastfromtheassumptionaboutvarianceboundontheoracle.
Now,theaboveisexactlytheboundobtainedintheproofofLemma5.2in(Feldmanetal.,2020)withthesecondmoment
ongradientnormreplacedbyvariance. RepeatingtherestoftheargumentsinthatLemmagivesustheclaimedresult.
LemmaD.5(PrivacyofAlgorithm6). Considerafunctionf(w;x)=ℓ(w;x)+∆(w)suchthatw (cid:55)→ℓ(w;x)isconvex,
L Lipschitz,L -smoothforallz,and∆(·)isλstronglyconvex,G LipschitzandH smoothoveraboundedsetW.
0 1 ∆ ∆
For n = Ω (cid:0)L1+H∆ log (cid:0)L1+H∆ (cid:1)(cid:1) , Algorithm 6 with input as function (w,x) (cid:55)→ f(w;x), σ2 = 64G2(log(n))2log(1/δ),
λ λ λ2n2ε2
η = log(n) andS({w }n )= 1 (cid:80)n γ w foranyweightsγ satisfies(ε,δ)-DP.
λn t t=1 (cid:80)n
t=1
γt t=1 t t t
28

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
Proof. Westartwithcomputingthesensitivityofthealgorithm’soutput:let{w }and{w′}besequenceofiteratesproduced
|     |     |     |     |     |     |     |     |     |     | t   | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
byAlgorithm6onneighbouringdatasets. Notethatthefunctionw (cid:55)→f(w;x)isL′ =L +H -smoothandλ-strongly
|     |     |     |     |     |     |     |     |     |     |     | 1 1 | ∆   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
convexforallx. Fromtheassumptiononn,wehavethatthestepsizeη ≤ . Supposethedifferingsamplebetween
H+H∆
| neighbouringdatasetsisx |     |     | ,thenw        |      | =w′ forallt≤j. |              | Also,         |     |                |     |            |     |     |
| ----------------------- | --- | --- | ------------- | ---- | -------------- | ------------ | ------------- | --- | -------------- | --- | ---------- | --- | --- |
|                         |     |     | j             | t    | t              |              |               |     |                |     |            |     |     |
|                         |     |     |               |      |                |              |               |     |                |     | 2L lo g(n) |     |     |
|                         |     |     | (cid:13)      | ′    | (cid:13)       | (cid:13)     |               | ;x′ | (cid:13)       |     | 0          |     |     |
|                         |     |     | (cid:13)w j+1 | −w   | (cid:13)=η     | (cid:13)∇ℓ(w | j ;x j )−∇ℓ(w | j   | ) (cid:13)≤2ηL | 0   | =          |     |     |
|                         |     |     |               | j +1 |                |              |               |     | j              |     | λ n        |     |     |
Now,foranyt>j,asinthestandardstabilityanalysiswehave,
|     |     |     | −w′ |     |                    |     |             |     | +η∇ℓ(w′;x      |      | )+η∇∆(w′) |     |     |
| --- | --- | --- | --- | --- | ------------------ | --- | ----------- | --- | -------------- | ---- | --------- | --- | --- |
|     |     | w   |     | =w  | −η∇ℓ(w             | ;x  | )−η∇∆(w     | )−w |                |      |           |     |     |
|     |     | t+1 |     | t+1 | t                  | t   | t           | t   | t              |      | t t       | t   |     |
|     |     |     |     |     | (cid:0)I−η (cid:0) |     |             |     | (cid:1)(cid:1) |      |           |     |     |
|     |     |     |     | =   | ∇2ℓ(w˜             |     | ;x )+∇2∆(w˜ | )   | (w             | −w′) |           |     |     |
|     |     |     |     |     |                    |     | t t         | t   | t              | t    |           |     |     |
wherethelastequalityfollowsfromTaylorremaindertheoremwherew˜ issomeintermediatepointinthelinejoiningw
t t
| andw′. | Usingthefactthatη |     |           | ≤ 1   | andλstrongconvexity,wehave |     |     |               |     |             |              |     |     |
| ------ | ----------------- | --- | --------- | ----- | -------------------------- | --- | --- | ------------- | --- | ----------- | ------------ | --- | --- |
| t      |                   |     |           | L1+H∆ |                            |     |     |               |     |             |              |     |     |
|        |                   |     | (cid:13)  |       | (cid:13)                   |     |     | (cid:13)      |     | (cid:13)    | 2L 0 lo g(n) |     |     |
|        |                   |     | (cid:13)w | −w ′  | (cid:13)≤(1−ηλ)∥w          |     | −w  | ′∥≤ (cid:13)w | −w  | ′ (cid:13)≤ |              |     |     |
|        |                   |     | t+1       | t +1  |                            |     | t   | t             | j+1 | j +1        | λ n          |     |     |
ApplyingconvexitytotheweightsinthedefinitionoftheselectorfunctionS,weget,
2L log(n)
|     |     |     |     |     |       | })−S({w′})∥≤ |     |     | 0   |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | ∥S({w | t            |     |     |     |     |     |     |     |
|     |     |     |     |     |       |              | t   |     | λn  |     |     |     |     |
TheprivacyproofnowfollowsfromtheGaussianmechanismguarantee.
LemmaD.6(PhasedSGDcompositeguarantee). Considerafunctionf(w;x) = ℓ(w;x)+∆(w)wherew (cid:55)→ ℓ(w;x)
is convex, L Lipschitz, L smooth for all x, and ∆(w) is λ strongly convex, G Lipschitz and H smooth over a
|     | 0   |     | 1   |     |     |     |     |     |     |     | ∆   |     | ∆   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:16) (cid:0)L1+H∆ (cid:1)(cid:17) 64L2 K2(log(n))2log(1/δ),satisfies(ε,δ)-
| boundedsetW. |     | Forn | = Ω | K(L1+H∆)log |     |     | ,Algorithm6withσ2 |     |     | =   | 0      |     |     |
| ------------ | --- | ---- | --- | ----------- | --- | --- | ----------------- | --- | --- | --- | ------ | --- | --- |
|              |     |      |     | λ           |     | λ   |                   |     |     |     | λ2n2ε2 |     |     |
log(n),
DP. Furthermore, with input as function (w,x) (cid:55)→ f(w;x), a dataset S of n samples drawn i.i.d. from D, η =
λn
K =lnlnn,γ =(1−ηλ)−tandS({w }n )= 1 (cid:80)n γ w ,theexcesspopulationriskofoutputw isbounded
|     | t   |     |     |     | t t=1 |     | (cid:80)n | t=1 t | t   |     |     |     | K   |
| --- | --- | --- | --- | --- | ----- | --- | --------- | ----- | --- | --- | --- | --- | --- |
t=1 γt
as
|     |     |     |     |       |       |     |               |     | (cid:18) |       | (cid:19) |     |     |
| --- | --- | --- | --- | ----- | ----- | --- | ------------- | --- | -------- | ----- | -------- | --- | --- |
|     |     |     |     |       |       |     |               |     | L2       | dL2   |          |     |     |
|     |     |     |     | E[F(w | ;D)]− |     | min F(w;D)=O˜ |     | 0        | +     | 0        |     |     |
|     |     |     |     |       | K     |     |               |     | λn       | λn2ε2 |          |     |     |
w∈W
Proof. The privacy proof simply follows from parallel composition. For the utility proof, we repeat the arguments in
Theorem5.3in(Feldmanetal.,2020)substitutingthevariance-basedboundfromLemmaD.4. Notethatthevarianceofthe
| stochasticgradientsused,V2 |     |     |     | ≤L2,thisgivesus, |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
|     |     |     |     |       |       |     |               |     | (cid:18) |       | (cid:19) |     |     |
| --- | --- | --- | --- | ----- | ----- | --- | ------------- | --- | -------- | ----- | -------- | --- | --- |
|     |     |     |     |       |       |     |               |     | L2       | dL2   |          |     |     |
|     |     |     |     | E[F(w | ;D)]− |     | min F(w;D)=O˜ |     | 0        | +     | 0        |     |     |
|     |     |     |     |       | K     |     |               |     | λn       | λn2ε2 |          |     |     |
w∈W
E.MissingResultsforGeneralizedLinearModels
Wefirstgivethedefinitionofoblivioussubspaceembedding.
ArandommatrixΦ∈Rk×disan(r,τ,β)-oblivioussubspace
DefinitionE.1((r,τ,β)-oblivioussubspaceembedding).
embeddingifforanyrdimensionallinearsubspaceinRd,sayV,wehavethatwithprobabilityatleast1−β,forallx∈V,
|     |     |     |     |     | (1−τ)∥x∥2 |     | ≤∥Φx∥2 | ≤(1+τ)∥x∥2 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | --- | ------ | ---------- | --- | --- | --- | --- | --- |
29

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
(cid:16) (cid:17)
Itiswell-knownthatJLmatriceswithembeddingdimensionk =O rlog(2/β) are(r,τ,β)-oblivioussubspaceembeddings
τ2
andcanbeconstructedefficiently(Cohen,2016). AsimpleexampleisascaledGaussianrandommatrix,Φ= √1 Gwhere
k
entriesofGareindependentanddistributedasN(0,1).
ProofofTheorem6.1. Wefirstproveprivacy. LetG(S)andH(S)betheboundsontheLipschitzandsmoothnessconstants
ofthefamilyoflossfunctions{w (cid:55)→f(w;Φx)} . Withk =Ω(log(2n/δ)),fromtheJL-property,itfollowsthatwith
x∈S
probabilityatleast1−δ/2,G(S) ≤ 2L ∥X∥andH(S) ≤ 2L ∥X∥2. Hence,usingthefactthatAis(ε,δ/2)-DP,we
0 1
havethatAlgorithm4is(ε,δ)-DP.
We now proceed to the utility part. Let w˜ ∈ Rk be the output of the base algorithm in low dimensions. Note that the
final output is w¯ = Φ⊤w˜. The transpose of the JL matrix can only increase the norm by the polynomial factor of d
and n, hence ∥w¯∥ ≤ poly(n,d)∥w˜∥. By assumption, P(∥w˜∥>poly(n,d,L
0
,L
1
)) ≤ √1
n
. Hence we also have that
P(∥w¯∥>poly(n,d,L
0
,L
1
))≤ √1
n
. LetW ⊆Rddenotetheabovesetwithradiuspoly(n,d,L
0
,L
1
).
Wenowdecomposethepopulationstationarityas,
E∥∇F(w¯;D)∥≤E∥∇F(w¯;D)−∇F(w¯;S)∥+∥∇F(w¯;S)∥
L ∥X∥
≤E sup ∥∇F(w;D)−∇F(w;S)∥+ 0√ +E∥∇F(w¯;S)∥, (7)
n
w∈W
wherethelastinequalityfollowsfromtheabovereasoningthatthatP (w¯ ∈W)≥1− √1 . Thefirsttermisboundedfrom
n
uniformconvergenceguaranteeinLemmaE.2notingthatthedependenceon∥W∥intheLemmaisonlypoly-logarithmic.
(cid:18) (cid:19)
L ∥X∥
E sup ∥∇F(w;D)−∇F(w;S)∥=O˜ 0√ (8)
n
w∈W
Wenowproveaboundontheempiricalstationarity. Notethatitsufficestoproveahigh-probability(overtherandomJL
matrix)boundbecausethenormofgradientisboundedinworstcasebyL ∥X∥. Thustheexpectednormofgradientofthe
0
outputisboundedbythehighprobabilityboundbyconsideringasmallenoughfailureprobability.
FromtheassumptiononA,withprobabilityatleast1−δ/2,
(cid:13) (cid:13)
(cid:13)1 (cid:88) n (cid:13)
∥∇F(w˜;ΦS)∥=E(cid:13) ϕ′ (⟨w˜,Φx ⟩)Φx (cid:13)≤g(k,n,2L ∥X∥,2L ∥X∥,ε,δ/2)
(cid:13)n yi i i(cid:13) 0 0
(cid:13) (cid:13)
i=1
We now use the fact that if k = O(ranklog(2n/δ)), then the JL transform is an (rank,1/2,δ/2) oblivious subspace
embedding(seeDefinitionE.1). Thus,itapproximatesthenormofanyvectorinspan({x }n ),andhenceanygradient.
i i=1
Therefore,
(cid:13) (cid:13) (cid:32) 1 (cid:88) n (cid:33)(cid:13) (cid:13) (cid:32) (cid:114) rank (cid:33) (cid:13) (cid:13)1 (cid:88) n (cid:13) (cid:13)
E∥∇F(w˜;ΦS)∥=E(cid:13)Φ ϕ′ (⟨w˜,Φx ⟩)x (cid:13)≥ 1− E(cid:13) ϕ′ (⟨w˜,Φx ⟩)x (cid:13)
(cid:13) n yi i i (cid:13) k (cid:13)n yi i i(cid:13)
(cid:13) (cid:13) (cid:13) (cid:13)
i=1 i=1
(cid:13) (cid:13) (cid:13) (cid:13)
≥ 1 E (cid:13) (cid:13) 1 (cid:88) n ϕ′ (⟨w˜,Φx ⟩)x (cid:13) (cid:13)= 1 E (cid:13) (cid:13) 1 (cid:88) n ϕ′ ( (cid:10) Φ⊤w˜,x (cid:11) )x (cid:13) (cid:13)= 1 E∥∇F(w¯;S)∥
2 (cid:13)n yi i i(cid:13) 2 (cid:13)n yi i i(cid:13) 2
(cid:13) (cid:13) (cid:13) (cid:13)
i=1 i=1
Thuswithk =O(ranklog(2n/δ)),weget
E∥∇F(w¯;S)∥≤g(k,n,2L ∥X∥,2L ∥X∥2,ε,δ)=g(rank,n,2L ∥X∥,2L ∥X∥2,ε,δ)
0 1 0 1
Fortheotherbound,letI ∈Rd×k denotethematrixwithfirstkdiagonalentries,(I ) withj ∈[k],are1andthe
d−k d−k j,j
30

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
restofthematrixiszero. Wehave,
E∥∇F(w¯;S)∥
(cid:13) (cid:13)
=E (cid:13) (cid:13) 1 (cid:88) n ϕ′ ( (cid:10) Φ⊤w˜,x (cid:11) )x (cid:13) (cid:13)
(cid:13)n yi i i(cid:13)
(cid:13) (cid:13)
i=1
(cid:13) (cid:13)1 (cid:88) n (cid:13) (cid:13) (cid:34)(cid:13) (cid:13)1 (cid:88) n 1 (cid:88) n (cid:13) (cid:13) (cid:35)
≤E(cid:13) ϕ′ (⟨w˜,Φx ⟩)I Φx (cid:13)+E (cid:13) ϕ′ (⟨w˜,Φx ⟩)x − ϕ′ (⟨w˜,Φx ⟩)I Φx (cid:13)
(cid:13)n yi i d−k i(cid:13) (cid:13)n yi i i n yi i d−k i(cid:13)
(cid:13) (cid:13) (cid:13) (cid:13)
i=1 i=1 i=1
(cid:13) (cid:13)
≤E∥I
d−k
∥ (cid:13) (cid:13)
(cid:13)n
1 (cid:88) n ϕ′
yi
(⟨w˜,Φx
i
⟩)Φx
i
(cid:13) (cid:13)
(cid:13)
+
n
1 E (cid:88) n (cid:12) (cid:12)ϕ′
yi
(⟨w˜,Φx
i
⟩) (cid:12) (cid:12)|∥x
i
−I
d−k
Φx
i
∥|
(cid:13) (cid:13)
i=1 i=1
n
1 (cid:88)
≤E∥∇F(w˜;ΦS)∥+ E L ∥I−I Φ∥∥x ∥
n 0 d−k i
i=1
≤g(k,n,2L ∥X∥,2L ∥X∥2,ε,δ/2)+L ∥X∥E∥I−H∥
0 1 0
wherethesecondinequalityfollowsfromtriangleinequality,thethirdinequalityfollowsfromL -LipschitznessoftheGLM,
0
thethirdinequalityfollowsfromtheaccuracyguaranteeofthebasealgorithmandsubstitutingH = I Φ. Tobound
d−k
E∥I−H∥,weuseconcentrationpropertiesofdistributionusedintheconstructionofJLmatrices. Specifically,usingthe
scaledGaussianmatrixconstruction,fromconcentrationofextremeeignevaluesofsquareGaussianmatrices,wehavethat
(cid:16) (cid:17)
E∥I−H∥=O˜ √1 (Rudelson&Vershynin,2010). Thisgivesus,
k
(cid:18) (cid:19)
L ∥X∥
E∥∇F(w¯;S)∥≤g(k,n,2L ∥X∥,2L ∥X∥2,ε,δ/2)+O˜ 0√
0 1
k
(cid:16) (cid:17)
Choosing k to minimize the above yields the bound of O˜ L0√ ∥X∥ . Combining the two cases, yields the bound of
k
g(k,n,2L ∥X∥,2L ∥X∥2,ε,δ/2)ongradientnorm. PluggingthisandtheboundinEqn. (8)inInequality(7)givesthe
0 1
claimedbound.
LemmaE.2. LetDbeaprobabilitydistributionoverX suchthat∥x∥ ≤ ∥X∥forallx ∈ supp(D). Letf(w;(x,y)) =
ϕ (⟨w,x⟩)beanL -smoothL -LipschitzGLM.Then,withprobabilityatleast1−β,overadrawofni.i.d. samplesS
y 1 0
fromD,wehave
4L ∥X∥log (cid:0) 2n3/2∥W∥L ∥X∥/L (cid:1) 4L ∥X∥ (cid:112) log(1/β)
sup ∥∇F(w;D)−∇F(w;S)∥≤ 0 √ 1 0 + 0 √
n n
w∈W
Proof. Wefirstgiveaboundontheexpecteduniformdeviation,E sup ∥∇F(w;D)−∇F(w;S)∥. Thegradient
S∼Dn w∈W
ofthelossfunctionis∇f(w;x)=ϕ′ (⟨w,x⟩)x. Westartwiththestandardsymmetrizationtrick,
x
E sup ∥∇F(w;D)−∇F(w;S)∥
S∼Dn
w∈W
(cid:13) (cid:13)
(cid:13) 1 (cid:88) n (cid:13)
=E sup (cid:13)Eϕ′ (⟨w,x⟩)x− ϕ′ (⟨w,x ⟩)x (cid:13)
S∼Dn (cid:13) y n xi i i(cid:13)
w∈W(cid:13) (cid:13)
i=1
(cid:13) (cid:13)
(cid:13) 1 (cid:88) n 1 (cid:88) n (cid:13)
=E sup (cid:13)E ϕ′ (⟨w,x′⟩)x′ − ϕ′ (⟨w,x ⟩)x (cid:13)
S∼Dn w∈W (cid:13) (cid:13) {x′ i }∼Dnn y i ′ i i n xi i i(cid:13) (cid:13)
i=1 i=1
(cid:13) (cid:13)
(cid:13)1 (cid:88) n 1 (cid:88) n (cid:13)
≤E sup (cid:13) ϕ′ (⟨w,x′⟩)x′ − ϕ′ (⟨w,x ⟩)x (cid:13)
S,S′∼Dn w∈W (cid:13) (cid:13) n y i ′ i i n xi i i(cid:13) (cid:13)
i=1 i=1
(cid:13) (cid:13)
(cid:13)1 (cid:88) n (cid:16) (cid:17)(cid:13)
=E E sup (cid:13) σ ϕ′ (⟨w,x′⟩)x′ −ϕ′ (⟨w,x ⟩)x (cid:13)
S,S′∼Dn {σi} w∈W (cid:13) (cid:13) n i y i ′ i i xi i i (cid:13) (cid:13)
i=1
(cid:13) (cid:13)
(cid:13)1 (cid:88) n (cid:13)
≤2E E sup (cid:13) σ ϕ′ (⟨w,x ⟩)x (cid:13) (9)
S∼Dn {σi} (cid:13)n i yi i i(cid:13)
w∈W(cid:13) (cid:13)
i=1
31

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
whereσ arei.i.d. Rademacherrandomvariables. Forfixed{x }n ,considerasetW s.t. forallw ∈ W andi ∈ [n],
i i i=1 0
thereexistsw ∈W suchthat|⟨w,x ⟩−⟨w ,x ⟩|≤τ. Since∥w∥≤∥W∥and∥x ∥≤∥X∥,werequireonly 2n∥W∥∥X∥
0 0 i 0 i i τ
pointsinW tosatisfytheabovecoveringcondition. Therefore,
0
(cid:13) (cid:13)
(cid:13)1 (cid:88) n (cid:13)
E E sup (cid:13) σ ϕ′ (⟨w,x ⟩)x (cid:13)
S∼Dn {σi} (cid:13)n i yi i i(cid:13)
w∈W(cid:13) (cid:13)
i=1
(cid:13) (cid:13)
=E E sup (cid:13) (cid:13) 1 (cid:88) n σ (cid:0) ϕ′ (⟨w,x ⟩)−ϕ′ (⟨w ,x ⟩)+ϕ′ (⟨w ,x ⟩) (cid:1) x (cid:13) (cid:13)
S∼Dn {σi} (cid:13)n i yi i yi 0 i yi 0 i i(cid:13)
w∈W,w0∈W0(cid:13)
i=1
(cid:13)
(cid:13) (cid:13) (cid:13) (cid:13)
≤E E sup (cid:13) (cid:13) 1 (cid:88) n σ (cid:0) ϕ′ (⟨w,x ⟩)−ϕ′ (⟨w ,x ⟩) (cid:1) x (cid:13) (cid:13)+ (cid:13) (cid:13) 1 (cid:88) n σ ϕ′ (⟨w ,x ⟩)x (cid:13) (cid:13)
S∼Dn {σi} (cid:13)n i yi i yi 0 i i(cid:13) (cid:13)n i yi 0 i i(cid:13)
w∈W,w0∈W0(cid:13)
i=1
(cid:13) (cid:13)
i=1
(cid:13)
(cid:13) (cid:13)
(cid:13)1 (cid:88) n (cid:13)
≤E E sup L |⟨w,x ⟩−⟨w ,x ⟩|∥X∥+E E sup (cid:13) σ ϕ′ (⟨w ,x ⟩)x (cid:13)
S∼Dn {σi} 1 i 0 i S∼Dn {σi} (cid:13)n i yi 0 i i(cid:13)
w∈W,w0∈W0 w0∈W0(cid:13)
i=1
(cid:13)
(cid:13) (cid:13)
(cid:13)1 (cid:88) n (cid:13)
≤L τ∥X∥+E E sup (cid:13) σ ϕ′ (⟨w ,x ⟩)x (cid:13) (10)
1 S∼Dn {σi} (cid:13)n i yi 0 i i(cid:13)
w0∈W0(cid:13)
i=1
(cid:13)
wherethesecondlastinequalityfollowsfromsmoothnessandthelastfromthedefinitionofcoverW . Forfixedw ,from
0 0
standardmanipulations,wehave,
(cid:118)
(cid:13) (cid:13)1 (cid:88) n (cid:13) (cid:13) (cid:117) (cid:117) (cid:13) (cid:13)1 (cid:88) n (cid:13) (cid:13) 2
E (cid:13) σ ϕ′ (⟨w ,x ⟩)x (cid:13)≤(cid:116)E (cid:13) σ ϕ′ (⟨w ,x ⟩)x (cid:13)
{σi}(cid:13)n i yi 0 i i(cid:13) {σi}(cid:13)n i yi 0 i i(cid:13)
(cid:13) (cid:13) (cid:13) (cid:13)
i=1 i=1
(cid:118)
(cid:117) n
= (cid:117) (cid:116) n 1 2 E {σi} (cid:88)(cid:13) (cid:13)σ i ϕ′ yi (⟨w 0 ,x i ⟩)x i (cid:13) (cid:13) 2
i=1
L ∥X∥
≤ 0√
n
UsingMassart’sfiniteclasslemmatohandleallw ∈W ,andsubstitutingtheaboveinEqn. (10),weget,
0 0
(cid:13) (cid:13)
(cid:13)1 (cid:88) n (cid:13) G∥X∥log(2n∥W∥∥X∥/τ)
E E sup (cid:13) σ ϕ′ (⟨w,x ⟩)x (cid:13)≤L τ∥X∥+ √
S∼Dn {σi} (cid:13)n i yi i i(cid:13) 1 n
w∈W(cid:13) (cid:13)
i=1
Choosingτ = L√0 ,weget,
L1 n
E E sup (cid:13) (cid:13) (cid:13) 1 (cid:88) n σ ϕ′ (⟨w,x ⟩)x (cid:13) (cid:13) (cid:13)≤ 2L 0 ∥X∥log (cid:0) 2n3/ √ 2∥W∥L 1 ∥X∥/L 0 (cid:1)
S∼Dn {σi} (cid:13)n i yi i i(cid:13) n
w∈W(cid:13) (cid:13)
i=1
Finally,substitutingtheaboveinEqn. (9)givesusthefollowingin-expectationbound.
4L ∥X∥log (cid:0) 2n3/2∥W∥L ∥X∥/L (cid:1)
E sup ∥∇F(w;D)−∇F(w;S)∥≤ 0 √ 1 0
S∼Dn
n
w∈W
Forthehigh-probabilitybound,letψ(S)=sup ∥∇F(w;D)−∇F(w;S)∥andletw∗ ∈W achievesthesupremum.
w∈W
WecanboundtheincrementbetweenneighbouringdatasetsS andS′as,
|ψ(S)−ψ(S′)|≤|∥∇F(w∗;D)−∇F(w∗;S)∥−∥∇F(w∗;D)−∇F(w∗;S′)∥|
≤∥∇F(w∗;S)−∇F(w∗;S′)∥
2L ∥X∥
≤ 0
n
Finally,applyingMcDiarmid’sinequalitygivestheclaimedbound.
32

FasterRatesofConvergencetoStationaryPointsinDifferentiallyPrivateOptimization
ProofofCorollary6.2. TheresultsfollowfromTheorem6.1providedweshowthattheconditionsonthebasealgorithmin
theTheoremstatementaresatisfied. TheprivacyandaccuracyclaimsfollowfromTheorem3.2and5.1respectively. We
notethateventhoughwearegivenpopulationstationarityguaranteefortheconvexcase,thesameboundforempirical
stationarityguaranteesimplyfollowsfromthere-samplingargumentin(Bassilyetal.,2019). Theonlythinglefttoshowis
thehigh-probabilityboundonthetrajectoryofthealgorithm.
Non-convexsettingwithPrivateSpiderboost: FromtheupdateinAlgorithm2,wehavethatforanyt
|     |     |       | t        |               | (cid:13) t       | (cid:13)       |           | (cid:13) t (cid:13)       |     |     |     |
| --- | --- | ----- | -------- | ------------- | ---------------- | -------------- | --------- | ------------------------- | --- | --- | --- |
|     |     |       | (cid:88) |               | (cid:13)(cid:88) | (cid:13)       |           | (cid:13)(cid:88) (cid:13) |     |     |     |
|     |     | ∥∇ ∥≤ |          | ∥∆ ∥+(cid:13) |                  | g (cid:13)≤2tL | +(cid:13) | g (cid:13)                |     |     |     |
|     |     | t     |          | i             | (cid:13)         | t(cid:13)      | 0         | (cid:13) t(cid:13)        |     |     |     |
|     |     |       | i=1      |               | (cid:13) i=1     | (cid:13)       |           | (cid:13) i=1 (cid:13)     |     |     |     |
N(0,σ2I)
where the last inequality follows from the Lipschitzness assumption. Note that g ∼ where σ ≤
|     |     |     |     | (cid:13)          |     | (cid:13) |           |     | t   | t   | t   |
| --- | --- | --- | --- | ----------------- | --- | -------- | --------- | --- | --- | --- | --- |
|     |     |     |     | (cid:13)(cid:80)t |     |          | (cid:112) |     |     |     |     |
O(max(σ ,σ )) = O(poly(n,d,L ,L )). Hence g (cid:13) ≤ dlog(1/β′)O(pol y(n,d,L ,L )) with prob abil-
| 1 (cid:98)2 |     | 0   | 1   | (cid:13) | i=1 | t(cid:13) |     |     |     | 0 1 |     |
| ----------- | --- | --- | --- | -------- | --- | --------- | --- | --- | --- | --- | --- |
ity at least 1−β′. Taking a union bound over all t ∈ T gives us ∥w ∥ ≤ poly(n,d,L ,L ,log(poly(n,d)/β)) with
|     |     |     |     |     |     |     | t   |     | 0   | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
probabilityatleast1−β. Substitutingβ = √1 yieldstheguaranteeofTheorem6.1.
n
ConvexsettingwithRecursiveRegularization: Sincetheiteratesarerestrictedtotheconstraintset,thefinaloutput,
withprobabilityone,liesinthesetofradius
|     |     |     |     | (cid:32)(cid:114) |     | (cid:33) | (cid:32) |     | (cid:33) |     |     |
| --- | --- | --- | --- | ----------------- | --- | -------- | -------- | --- | -------- | --- | --- |
∥w∗∥3/2n
|     |               |     |     |     | L 1  |     | L   | 1   |     |     |     |
| --- | ------------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
|     | R =2T/2∥w∗∥=O |     |     |     | ∥w∗∥ |     | =O  |     |     |     |     |
|     | T             |     |     |     | λ    |     |     | L   |     |     |     |
0
whichcompletestheproof.
33