var ddd = db.veps.find( { "transcript_consequences.polyphen_prediction": { $in : ["probably_damaging",
                                                                                  "possibly_damaging"]},
                         "transcript_consequences.sift_prediction": "deleterious"} )


ddd.forEach(function(v) {
    for (var n in v['transcript_consequences']) {
        print( 
               v['transcript_consequences'][n]['id'],               
               v['transcript_consequences'][n]['impact'],
               v['transcript_consequences'][n]['polyphen_prediction'],
               v['transcript_consequences'][n]['sift_prediction'])
    }
} )
