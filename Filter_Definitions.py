
import numpy as np
import pandas as pd

def Filter_Definitions():
    columnnames = ['Type','Order','Section','Real Part','Imaginary Part','Fo','alpha','Q','-3dB Frequency','Peaking Frequency','Peaking Level']
    filtertype = ["Butterworth" for x in range(19)]
    data = {'Type':filtertype,
            'Order':[2,3,3,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,8],
            'Section':[1,1,2,1,2,1,2,3,1,2,3,1,2,3,4,1,2,3,4],
            'Real Part':[.7071,.5,1,.9239,.3827,.809,.309,1,.9659,.7071,.2588,.901,.6235,.2225,1,.9808,.8315,.5556,.1951],
            'Imaginary Part':[.7071,.8660,np.nan,.3827,.9239,.5878,.9511,np.nan,.2588,.7071,.9659,.4339,.7818,.9749,np.nan,.1951,.5556,.8315,.9805],
            'Fo':[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            'alpha':[1.4142,1,np.nan,1.8478,.7654,1.618,.618,np.nan,1.9319,1.4142,.5176,1.8019,1.2470,.4450,np.nan,1.9616,1.6629,1.1112,.3902],
            'Q':[.7071,1,np.nan,.5412,1.3065,.618,1.6182,np.nan,.5176,.7071,1.9319,.5550,.8019,2.2471,np.nan,.5098,.6013,.9,2.5628],
            '-3dB Frequency':[1,np.nan,1,.7195,np.nan,.8588,np.nan,np.nan,.6758,1,np.nan,.7449,np.nan,np.nan,np.nan,.6615,.8295,np.nan,np.nan],
            'Peaking Frequency':[np.nan,.7071,np.nan,np.nan,.8409,np.nan,.8995,np.nan,np.nan,np.nan,.9306,np.nan,.4717,.9492,np.nan,np.nan,np.nan,.6186,.9612],
            'Peaking Level':[np.nan,1.2493,np.nan,np.nan,3.0102,np.nan,4.6163,np.nan,np.nan,np.nan,6.021,np.nan,.2204,7.2530,np.nan,np.nan,np.nan,.6876,8.3429]}

    df1 = pd.DataFrame(data,columns=columnnames)
    filtertype = ["0.1dB Chebyshev" for x in range(19)]
    data = {'Type':filtertype,
            'Order':[2,3,3,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,8],
            'Section':[1,1,2,1,2,1,2,3,1,2,3,1,2,3,4,1,2,3,4],
            'Real Part':[.6104,.3490,.6970,.2177,.5257,.3842,.1468,.4749,.3916,.2867,.1049,.3178,.2200,.0785,.3528,.3058,.2529,.1732,.0608],
            'Imaginary Part':[.7106,.8684,np.nan,.9254,.3833,.5884,.9521,np.nan,.2590,.7077,.9667,.4341,.7823,.9755,np.nan,.1952,.5558,.8319,.9812],
            'Fo':[.9368,.9359,.6970,.9507,.6506,.7027,.9634,.4749,.4695,.7636,.9724,.5380,.8126,.9787,.3528,.3628,.6106,.8497,.9831],
            'alpha':[1.3032,.7458,np.nan,.4580,1.6160,1.0935,.3048,np.nan,1.6682,.7509,.2158,1.1814,.5414,.1604,np.nan,1.6858,.8283,.4077,.1237],
            'Q':[.7673,1.3408,np.nan,2.1834,.6188,.9145,3.2812,np.nan,.5995,1.3316,4.6348,.8464,1.8469,6.2235,np.nan,.5932,1.2073,2.4534,8.0819],
            '-3dB Frequency':[np.nan,np.nan,.6970,np.nan,.5596,np.nan,np.nan,.4749,.3879,np.nan,np.nan,np.nan,np.nan,np.nan,.3528,.2956,np.nan,np.nan,np.nan],
            'Peaking Frequency':[.3638,.7952,np.nan,.8994,np.nan,.4457,.9407,np.nan,np.nan,.6470,.9610,.2957,.7507,.9723,np.nan,np.nan,.4949,.8137,.9793],
            'Peaking Level':[.099,3.1978,np.nan,7.0167,np.nan,.7662,10.4226,np.nan,np.nan,3.1478,13.3714,.4157,5.6595,15.9226,np.nan,np.nan,2.4532,7.9784,18.1669]}
    df2 = pd.DataFrame(data,columns=columnnames)

    filtertype = ["0.5dB Chebyshev" for x in range(19)]
    data = {'Type':filtertype,
            'Order':[2,3,3,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,8],
            'Section':[1,1,2,1,2,1,2,3,1,2,3,1,2,3,4,1,2,3,4],
            'Real Part':[0.5129,0.2683,0.5366,0.3872,0.1605,0.2767,0.1057,0.3420,0.2784,0.2037,0.0746,0.2241,0.1550,0.0553,0.2487,0.2144,0.1817,0.1214,0.0426],
            'Imaginary Part':[0.7225,0.8753,np.nan,0.3850,0.9297,0.5902,0.9550,np.nan,0.2596,0.7091,0.9687,0.4349,0.7836,0.9771,np.nan,0.1955,0.5565,0.8328,0.9824],
            'Fo':[1.2314,1.0688,.6265,.5949,1.0313,.6905,1.0178,.3623,.3963,.7680,1.0114,.5040,.8228,1.0081,.2562,.2968,.5989,.8610,1.0060],
            'alpha':[1.1577,.5861,np.nan,1.4182,.3402,.8490,.2200,np.nan,1.4627,.5522,.1536,.9161,.3881,.1130,np.nan,1.4779,.6208,.2885,.0867],
            'Q':[.8638,1.7061,np.nan,.7051,2.9391,1.1779,4.5451,np.nan,.6836,1.8109,6.5119,1.0916,2.5767,8.8487,np.nan,.6767,1.6109,3.4662,11.5305],
            '-3dB Frequency':[np.nan,np.nan,.6265,.5951,np.nan,np.nan,np.nan,.3623,.3827,np.nan,np.nan,np.nan,np.nan,np.nan,.2562,.2835,np.nan,np.nan,np.nan],
            'Peaking Frequency':[.7072,.9727,np.nan,np.nan,1.0010,.5522,1.0054,np.nan,np.nan,.7071,1.0055,.3839,.7912,1.0049,np.nan,np.nan,.5381,.8429,1.0041],
            'Peaking Level':[.5002,5.0301,np.nan,np.nan,9.4918,2.2849,13.2037,np.nan,np.nan,5.5025,16.2998,1.7838,8.388,18.9515,np.nan,np.nan,4.5815,10.8885,21.2452]}
    df3 = pd.DataFrame(data,columns=columnnames)

    filtertype = ["1.0dB Chebyshev" for x in range(19)]
    data = {'Type':filtertype,
            'Order':[2,3,3,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,8],
            'Section':[1,1,2,1,2,1,2,3,1,2,3,1,2,3,4,1,2,3,4],
            'Real Part':[.4508,.2257,.4513,.3199,.1325,.2265,.0865,.2800,.2268,.1550,.0608,.1819,.1259,.0449,.2019,.1737,.1473,.0984,.0346],
            'Imaginary Part':[.7351,.8822,np.nan,.3868,.9339,.5918,.9575,np.nan,.2601,.7106,.9707,.4354,.7846,.9785,np.nan,.1956,.5571,.8337,.9836],
            'Fo':[.8623,.9106,.4513,.5019,.9433,.6337,.9614,.2800,.3451,.7273,.9726,.4719,.7946,.9795,.2019,.2616,.5762,.8395,.9842],
            'alpha':[1.0456,.4957,np.nan,1.2746,.2809,.7149,.1800,np.nan,1.3144,.4262,.1249,.7710,.3169,.0918,np.nan,1.3280,.5112,.2344,.0702],
            'Q':[.9564,2.0173,np.nan,.7845,3.5594,1.3988,5.5559,np.nan,.7608,2.3462,8.0036,1.2971,3.1558,10.8982,np.nan,.7530,1.9560,4.2657,14.2391],
            '-3dB Frequency':[np.nan,np.nan,.6265,.5951,np.nan,np.nan,np.nan,.3623,.3827,np.nan,np.nan,np.nan,np.nan,np.nan,.2562,.2835,np.nan,np.nan,np.nan],
            'Peaking Frequency':[.5806,.8528,np.nan,.2174,.9245,.5467,.9536,np.nan,.1273,.6935,.9688,.3956,.7744,.9775,np.nan,.0899,.5373,.8279,.9830],
            'Peaking Level':[.9995,6.3708,np.nan,.1557,11.1142,3.5089,14.9305,np.nan,.0813,7.6090,18.0827,2.9579,10.0927,20.7563,np.nan,.0611,6.1210,12.6599,23.0750]}
    df4 = pd.DataFrame(data,columns=columnnames)

    df = pd.concat([df1,df2,df3,df4])

    return(df)