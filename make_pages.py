import random
import datetime

template = open("template.html", "r").read()

birds = [
   {
    "name": "Alexandrine Parakeet",
    "scientific": "Psittacula eupatria",
    "description": "Recognising the Alexandrine Parakeet starts with a large green parakeet with a red bill, long tail and a dark neck collar in adult males. The species uses woodland, forest edges, farmland and gardens and takes seeds, fruits, flowers and grains as its principal food. It often travels in noisy flocks and feeds in trees. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "AlexandrineParakeet1.jpg",
    "quick_facts": {
        "family": "Psittaculidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "seeds, fruits, flowers and grains",
        "habitat": "woodland, forest edges, farmland and gardens",
        "behaviour": "often travels in noisy flocks and feeds in trees",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Alexandrine Parakeet is best separated from Rose-Ringed Parakeet by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Rose-Ringed Parakeet, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Plum-headed Parakeet can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "American Goldfinch",
    "scientific": "Spinus tristis",
    "description": "The American Goldfinch is a small North American finch whose breeding male has brilliant yellow plumage, black wings and a black forehead. Females and winter birds are much duller. It is strongly associated with seed-producing plants, especially thistles, and is often seen hanging acrobatically from seedheads.",
    "image": "AmericanGoldfinch1.jpg",
    "quick_facts": {
        "family": "Fringillidae",
        "size": "11-13 cm",
        "weight": "About 11-20 g",
        "wingspan": "About 19-22 cm",
        "diet": "seeds, especially those of composites, plus insects when feeding young",
        "habitat": "fields, meadows, scrub, gardens and woodland edges",
        "behaviour": "often travels in small flocks and clings to seed heads",
        "activity": "Diurnal",
        "nesting": "A small cup of plant fibres and down, usually placed in a shrub or low tree",
        "breeding_season": "June to August",
        "clutch_size": "Usually 4-6 eggs",
        "call": "Bright twittering calls and a distinctive flight call",
        "lifespan": "Up to about 11 years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Canada: southern provinces; United States: most states; Mexico: mainly northern and central regions"
    },
    "similar_birds": "American Goldfinch is best separated from Lesser Goldfinch by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Lesser Goldfinch, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Pine Siskin can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "Cornell Lab of Ornithology — All About Birds / eBird",
        "Audubon — North American bird identification and natural history",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "American Robin",
    "scientific": "Turdus migratorius",
    "description": "The American Robin is a familiar North American thrush with a grey-brown back, orange-red breast and yellowish bill. It is particularly well known for running across lawns and open ground while searching for earthworms. It also eats large quantities of berries and fruit and can be found in forests, gardens, parks and suburban neighbourhoods.",
    "image": "AmericanRobin1.jpg",
    "quick_facts": {
        "family": "Turdidae",
        "size": "23-28 cm",
        "weight": "About 77-85 g",
        "wingspan": "About 31-41 cm",
        "diet": "earthworms, insects, fruit and berries",
        "habitat": "lawns, gardens, woodland edges and open forest",
        "behaviour": "often forages on the ground and pauses upright between runs",
        "activity": "Diurnal",
        "nesting": "A cup-shaped nest made from grass, twigs and mud, usually placed in a tree or shrub",
        "breeding_season": "April to August",
        "clutch_size": "Usually 3-5 eggs",
        "call": "Clear musical phrases and sharp alarm calls",
        "lifespan": "Often 2-6 years, with much longer lifespans recorded",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Canada: most provinces and territories; United States: most states; Mexico: northern and mountainous regions"
    },
    "similar_birds": "American Robin is best separated from Varied Thrush by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Varied Thrush, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Eastern Bluebird can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "Cornell Lab of Ornithology — All About Birds / eBird",
        "Audubon — North American bird identification and natural history",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Ashy Drongo",
    "scientific": "Dicrurus leucophaeus",
    "description": "The Ashy Drongo is a slim grey drongo with a deeply forked tail and red or dark eyes depending on the form, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in open forest, woodland edges, plantations and clearings and feeds mainly on flying insects and other small invertebrates. It often sallies from an exposed perch to catch insects in the air. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "AshyDrongo1.jpg",
    "quick_facts": {
        "family": "Dicruridae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "flying insects and other small invertebrates",
        "habitat": "open forest, woodland edges, plantations and clearings",
        "behaviour": "often sallies from an exposed perch to catch insects in the air",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Ashy Drongo is best separated from Black Drongo by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Black Drongo, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Grey Drongo can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Ashy Prinia",
    "scientific": "Prinia socialis",
    "description": "The Ashy Prinia is a small upright-tailed warbler with grey upperparts and a fine pointed bill, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in grassland, scrub, fields, gardens and wetlands and feeds mainly on insects and other small arthropods. It keeps close to low vegetation and often flicks its long tail upward. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "AshyPrinia1.jpg",
    "quick_facts": {
        "family": "Cisticolidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects and other small arthropods",
        "habitat": "grassland, scrub, fields, gardens and wetlands",
        "behaviour": "keeps close to low vegetation and often flicks its long tail upward",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Ashy Prinia is best separated from Plain Prinia by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Plain Prinia, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Grey-breasted Prinia can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Asian Brown Flycatcher",
    "scientific": "Muscicapa dauurica",
    "description": "Recognising the Asian Brown Flycatcher starts with a small brown flycatcher with a pale underside and delicate bill. The species uses woodland, forest edges, gardens and shaded plantations and takes flying insects and other small invertebrates as its principal food. It perches quietly before making short flights after prey. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "AsianBrownFlycatcher1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "flying insects and other small invertebrates",
        "habitat": "woodland, forest edges, gardens and shaded plantations",
        "behaviour": "perches quietly before making short flights after prey",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Asian Brown Flycatcher is best separated from Dark-sided Flycatcher by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Dark-sided Flycatcher, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Grey-streaked Flycatcher can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Asian Fairy-bluebird",
    "scientific": "Irena puella",
    "description": "The Asian Fairy-bluebird is a beautiful Southeast Asian forest bird. Males are deep blue with a glossy black head, wings and tail, while females are generally duller blue-green. It is primarily a fruit-eater and usually moves through the forest canopy searching for berries and other food.",
    "image": "AsianFairy-Bluebird1.jpg",
    "quick_facts": {
        "family": "Irenidae",
        "size": "23-27 cm",
        "weight": "About 50-80 g",
        "wingspan": "About 35-40 cm",
        "diet": "fruit, berries and some insects",
        "habitat": "evergreen forest, woodland and mature gardens",
        "behaviour": "usually moves through the canopy in pairs or small groups",
        "activity": "Diurnal",
        "nesting": "A cup-shaped nest constructed in a tree",
        "breeding_season": "Varies geographically, generally during local wet or warmer seasons",
        "clutch_size": "Usually 2 eggs",
        "call": "Clear whistles and melodious notes",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "India: Himalayan foothills, northeastern states and parts of the Western Ghats; Bangladesh; Bhutan; Myanmar; Thailand; Malaysia; Indonesia and the Philippines"
    },
    "similar_birds": "Asian Fairy-bluebird is best separated from Asian Glossy Starling by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Asian Glossy Starling, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Black-naped Blue Flycatcher can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Asian Koel",
    "scientific": "Eudynamys scolopaceus",
    "description": "The Asian Koel is a long-tailed cuckoo in which males are glossy black and females are brown and spotted, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in woodland, gardens, orchards and towns with fruiting trees and feeds mainly on fruit, berries and some animal food. It is often heard before it is seen and uses other birds' nests for its eggs. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "AsianKoel1.jpg",
    "quick_facts": {
        "family": "Cuculidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fruit, berries and some animal food",
        "habitat": "woodland, gardens, orchards and towns with fruiting trees",
        "behaviour": "is often heard before it is seen and uses other birds' nests for its eggs",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Asian Koel is best separated from Greater Coucal by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Greater Coucal, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Common Hawk-Cuckoo can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Asian-Green Bee-eater",
    "scientific": "Merops orientalis",
    "description": "The Asian-Green Bee-eater is a slim green bee-eater with a dark eye stripe and elongated central tail feathers. It is found in open country, grassland, scrub, farmland and woodland edges, where it feeds mainly on bees, wasps, dragonflies and other flying insects. The species is often noticed because it perches conspicuously before making fast aerial feeding flights. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "Asian-GreenBee-Eater1.jpg",
    "quick_facts": {
        "family": "Meropidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "bees, wasps, dragonflies and other flying insects",
        "habitat": "open country, grassland, scrub, farmland and woodland edges",
        "behaviour": "perches conspicuously before making fast aerial feeding flights",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Asian-Green Bee-eater is best separated from Blue-tailed Bee-eater by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Blue-tailed Bee-eater, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Blue-throated Bee-eater can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — Birds of the World / eBird",
        "Handbook of the Birds of the World / BirdLife International",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Australian Brush-turkey",
    "scientific": "Alectura lathami",
    "description": "The Australian Brush-turkey is a large megapode with a mostly black body, a bare red head, a yellow throat wattle and a laterally flattened tail. Despite its name, it is not a true turkey. It belongs to the megapode family, a remarkable group of birds that incubate their eggs using heat generated by decomposing vegetation rather than sitting directly on the eggs. The male Australian Brush-turkey constructs a huge mound of leaves, soil and other organic material, sometimes several metres across. Females lay eggs in the mound, and the male monitors its temperature by adjusting the material. The chicks hatch fully feathered and can fly within hours.",
    "image": "AustralianBrush-Turkey1.jpg",
    "quick_facts": {
        "family": "Megapodiidae",
        "size": "60-75 cm",
        "weight": "About 2-2.5 kg",
        "wingspan": "About 80-90 cm",
        "diet": "invertebrates, seeds, fruit and other plant material",
        "habitat": "rainforest, wet forest, woodland, parks and gardens",
        "behaviour": "scratches through leaf litter while searching for food and builds large incubation mounds",
        "activity": "Diurnal",
        "nesting": "Eggs are buried in a large mound of decomposing vegetation; several females may lay in one mound",
        "breeding_season": "Mainly spring and summer, with breeding varying by region",
        "clutch_size": "Individual females lay multiple eggs over the breeding season",
        "call": "Deep booming and clucking calls",
        "lifespan": "Can live for many years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: eastern Queensland south to New South Wales, including Cape York Peninsula and the Illawarra region"
    },
    "similar_birds": "Australian Brush-turkey is best separated from Malleefowl by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Malleefowl, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Orange-footed Scrubfowl can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Australian Darter",
    "scientific": "Anhinga novaehollandiae",
    "description": "The Australian Darter is a long-necked waterbird that is exceptionally well adapted to hunting underwater. Its narrow body, long neck and pointed bill give it a snake-like appearance when only its neck and head are visible above the surface, which has earned it the nickname 'snakebird'. It swims with much of its body submerged and pursues fish underwater before spearing them with its sharp bill. After swimming, it often spreads its wings to dry its plumage because its feathers are less waterproof than those of many ducks. Australian Darters are commonly seen around freshwater wetlands, rivers, lakes and sheltered coastal waters.",
    "image": "AustralianDarter1.jpg",
    "quick_facts": {
        "family": "Anhingidae",
        "size": "80-90 cm",
        "weight": "About 1.1-1.5 kg",
        "wingspan": "About 115-125 cm",
        "diet": "fish and other aquatic animals",
        "habitat": "freshwater wetlands, rivers, lakes and sheltered coastal waters",
        "behaviour": "dives underwater and commonly spreads its wings to dry after swimming",
        "activity": "Diurnal",
        "nesting": "A stick nest built in trees or shrubs over or near water, often in colonies",
        "breeding_season": "Usually variable according to rainfall and water conditions",
        "clutch_size": "Usually 2-4 eggs",
        "call": "Generally quiet; produces low grunts and other calls around breeding colonies",
        "lifespan": "Usually several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: northern, eastern and southern Australia, including Tasmania; also New Guinea and nearby islands"
    },
    "similar_birds": "Australian Darter is best separated from Oriental Darter by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Oriental Darter, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Little Cormorant can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Australian Golden Whistler",
    "scientific": "Pachycephala pectoralis",
    "description": "The Australian Golden Whistler is a striking songbird whose male has bright yellow underparts, an olive-green back, a black head and a vivid yellow collar. Females are much duller, with grey and olive-brown plumage. The species is famous for its strong, musical voice and is one of Australia's most impressive songsters. Golden Whistlers inhabit dense woodland, rainforest, mallee and other wooded environments, where they search leaves and branches for insects and spiders. They may also eat berries. The species is closely related to other whistlers, but the male's bright golden underparts and black-and-yellow head pattern make it particularly distinctive.",
    "image": "AustralianGoldenWhistler1.jpg",
    "quick_facts": {
        "family": "Pachycephalidae",
        "size": "16-18 cm",
        "weight": "About 25-35 g",
        "wingspan": "About 25-30 cm",
        "diet": "insects, spiders and berries",
        "habitat": "rainforest, woodland, mallee, scrub and gardens",
        "behaviour": "usually forages quietly through foliage while giving strong musical whistles",
        "activity": "Diurnal",
        "nesting": "A shallow bowl of twigs, grass and bark bound with spider web, placed in a shrub or tree fork",
        "breeding_season": "September to January",
        "clutch_size": "2-3 eggs",
        "call": "Strong, musical whistles including repeated high notes",
        "lifespan": "Usually several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: eastern, southern and parts of southwestern Australia, including Tasmania; also New Guinea, Indonesia, Fiji and the Solomon Islands"
    },
    "similar_birds": "Australian Golden Whistler is best separated from Rufous Whistler by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Rufous Whistler, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Grey Shrike-thrush can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Australian Ibis",
    "scientific": "Threskiornis moluccus",
    "description": "The Australian Ibis, also known as the Australian White Ibis, is a large long-legged ibis with a mostly white body, black head and neck, and a long curved bill. It occurs naturally in wetlands, floodplains and grasslands but is also highly successful in parks and urban areas where it searches for food.",
    "image": "AustralianIbis1.jpg",
    "quick_facts": {
        "family": "Threskiornithidae",
        "size": "65-75 cm",
        "weight": "About 1.4-1.9 kg",
        "wingspan": "About 110-125 cm",
        "diet": "invertebrates, frogs, seeds, food scraps and other opportunistic items",
        "habitat": "wetlands, grasslands, farmland, parks and urban areas",
        "behaviour": "walks steadily while probing soil and shallow water",
        "activity": "Diurnal",
        "nesting": "A stick and vegetation nest usually built in trees or wetland vegetation, often in colonies",
        "breeding_season": "Varies with rainfall and locality",
        "clutch_size": "Usually 2-4 eggs",
        "call": "Generally quiet, with grunts and low calls around colonies",
        "lifespan": "Often lives for 10-15 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: all states and territories; New Guinea and nearby islands"
    },
    "similar_birds": "Australian Ibis is best separated from Straw-necked Ibis by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Straw-necked Ibis, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Glossy Ibis can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Australian King-Parrot",
    "scientific": "Alisterus scapularis",
    "description": "The Australian King-Parrot is a colourful eastern Australian parrot in which the sexes are strikingly different. Adult males have a completely red head and underparts with green wings and back, while females have a green head and breast but retain red underparts. The species is usually found in rainforest and wet forest but can also visit well-treed suburbs, where it feeds on seeds and fruit. Australian King-Parrots are generally encountered in pairs or family groups and are relatively quiet compared with many cockatoos. They nest deep inside tree hollows, sometimes with the entrance high above the ground while the eggs are laid much deeper inside the cavity.",
    "image": "AustralianKing-Parrot1.jpg",
    "quick_facts": {
        "family": "Psittaculidae",
        "size": "41-43 cm",
        "weight": "About 180-260 g",
        "wingspan": "About 50-60 cm",
        "diet": "seeds, fruit and flowers",
        "habitat": "rainforest, wet forest, woodland and well-treed suburbs",
        "behaviour": "usually travels in pairs or family groups and feeds high in trees",
        "activity": "Diurnal",
        "nesting": "A deep tree hollow containing decayed wood dust",
        "breeding_season": "September to January",
        "clutch_size": "Usually 5 eggs",
        "call": "Loud high-pitched whistles and rolling calls in flight",
        "lifespan": "Often lives for many years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: eastern coast and ranges from Queensland through New South Wales and Victoria to southeastern South Australia"
    },
    "similar_birds": "Australian King-Parrot is best separated from Crimson Rosella by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Crimson Rosella, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Eastern Rosella can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Australian Magpie",
    "scientific": "Gymnorhina tibicen",
    "description": "The Australian Magpie is a large black-and-white songbird found across much of Australia. Despite its common name, it is not closely related to the Eurasian Magpie. Its plumage varies geographically, but adults generally have striking black-and-white patterns and a chestnut-brown eye. It is particularly famous for its complex and musical calls, which can vary considerably in pitch. Australian Magpies usually live in permanent territorial groups and spend much of their time walking across open ground searching for food. During the breeding season, some birds become strongly defensive around their nesting areas.",
    "image": "AustralianMagpie1.jpg",
    "quick_facts": {
        "family": "Artamidae",
        "size": "36-44 cm",
        "weight": "About 220-350 g",
        "wingspan": "About 55-85 cm",
        "diet": "insects, larvae, small animals, carrion, seeds and fruit",
        "habitat": "open woodland, parks, playing fields and suburban areas",
        "behaviour": "walks across open ground while searching for food",
        "activity": "Diurnal",
        "nesting": "A platform of sticks and twigs with a bowl lined with grass and hair, usually placed in a tree",
        "breeding_season": "Mainly August to November",
        "clutch_size": "3-5 eggs",
        "call": "Complex, melodious warbling and a variety of alarm and contact calls",
        "lifespan": "Often more than 10 years, with some individuals living considerably longer",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: widespread across most states and territories except the densest forests and the most arid desert regions"
    },
    "similar_birds": "Australian Magpie is best separated from Pied Butcherbird by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Pied Butcherbird, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Pied Currawong can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Australian Pelican",
    "scientific": "Pelecanus conspicillatus",
    "description": "The Australian Pelican is a huge waterbird with an exceptionally long bill and an enormous throat pouch. It is widespread across Australia and can be found on freshwater lakes, rivers, estuaries, coastal waters and wetlands. Despite its size, it is an excellent glider and can use rising thermal air currents to travel long distances with relatively little effort. Australian Pelicans mainly eat fish but are opportunistic feeders and may take crustaceans, amphibians and other aquatic animals. They often feed cooperatively, working together to herd fish into shallow water. Their breeding colonies can become enormous when water and food conditions are favourable.",
    "image": "AustralianPelican1.jpg",
    "quick_facts": {
        "family": "Pelecanidae",
        "size": "160-180 cm",
        "weight": "About 4-6.8 kg",
        "wingspan": "230-250 cm",
        "diet": "fish and other aquatic animals",
        "habitat": "lakes, rivers, estuaries, coastal lagoons and sheltered seas",
        "behaviour": "often rests in groups and feeds by plunging or scooping prey from water",
        "activity": "Diurnal",
        "nesting": "A shallow scrape on the ground lined with small amounts of vegetation or feathers",
        "breeding_season": "Can breed at any time of year depending on rainfall and water conditions",
        "clutch_size": "1-3 eggs",
        "call": "Generally quiet away from breeding colonies; adults use various visual and low vocal signals",
        "lifespan": "About 10-25 years or more",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: widespread throughout the continent; also Papua New Guinea and western Indonesia"
    },
    "similar_birds": "Australian Pelican is best separated from Australian Gannet by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Australian Gannet, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Brown Pelican can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Australian Raven",
    "scientific": "Corvus coronoides",
    "description": "The Australian Raven is a large Australian corvid with almost entirely black plumage that can show a glossy sheen in good light. Adults have pale or white irises, shaggy throat feathers and a relatively long tail. It is highly adaptable and can be found in woodland, open country, farmland and urban areas.",
    "image": "AustralianRaven1.jpg",
    "quick_facts": {
        "family": "Corvidae",
        "size": "46-53 cm",
        "weight": "About 650-1,000 g",
        "wingspan": "About 90-100 cm",
        "diet": "insects, carrion, seeds, fruit and small animals",
        "habitat": "woodland, farmland, open country, parks and suburbs",
        "behaviour": "forages on the ground and often calls from exposed perches",
        "activity": "Diurnal",
        "nesting": "A large stick nest usually placed high in a tree",
        "breeding_season": "July to December",
        "clutch_size": "Usually 3-6 eggs",
        "call": "Deep, resonant calls often described as a drawn-out 'ah-ah-ah'",
        "lifespan": "Can live for more than 20 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: Western Australia, South Australia, Victoria, New South Wales and southern Queensland"
    },
    "similar_birds": "Australian Raven is best separated from Little Raven by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Little Raven, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Forest Raven can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Australian Wood Duck",
    "scientific": "Chenonetta jubata",
    "description": "The Australian Wood Duck, also called the Maned Duck, is a medium-sized, goose-like duck that spends surprisingly little time on open water compared with many other ducks. Males have a dark brown head and small crest-like mane, a pale grey body and a darker belly, while females have a paler head with distinctive white facial stripes. The species commonly walks and feeds on land, particularly in grasslands, farmland and flooded pastures. It also uses wetlands, parks and urban ponds. Australian Wood Ducks usually forage on grasses and herbs and may take insects. Their preference for land distinguishes them from many other Australian ducks.",
    "image": "AustralianWoodDuck1.jpg",
    "quick_facts": {
        "family": "Anatidae",
        "size": "44-50 cm",
        "weight": "About 700-900 g",
        "wingspan": "About 75-85 cm",
        "diet": "grass, aquatic plants, seeds and small invertebrates",
        "habitat": "grassland, wetlands, farm dams and open woodland",
        "behaviour": "often grazes on land rather than remaining on water",
        "activity": "Diurnal",
        "nesting": "Uses tree hollows, nest boxes and other cavities, often some distance from water",
        "breeding_season": "Mainly during the wetter and cooler parts of the year, varying by region",
        "clutch_size": "Usually 8-12 eggs",
        "call": "Females give a loud rising call while males have shorter, higher-pitched calls",
        "lifespan": "Usually several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: widespread, including Tasmania"
    },
    "similar_birds": "Australian Wood Duck is best separated from Pacific Black Duck by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Pacific Black Duck, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Chestnut Teal can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Azure-winged Magpie",
    "scientific": "Cyanopica cyanus",
    "description": "The Azure-winged Magpie is a distinctive Iberian corvid with a black cap, pale body, blue wings and a blue tail. It is highly social and often travels in noisy groups through open woodland and Mediterranean landscapes. It feeds on a wide variety of plant and animal foods.",
    "image": "Azure-WingedMagpie1.jpg",
    "quick_facts": {
        "family": "Corvidae",
        "size": "31-35 cm",
        "weight": "About 70-100 g",
        "wingspan": "About 40-45 cm",
        "diet": "insects, fruit, seeds and small animals",
        "habitat": "open woodland, scrub, farmland and oak country",
        "behaviour": "is strongly social and often moves in noisy groups",
        "activity": "Diurnal",
        "nesting": "An open cup of twigs and plant material placed in a tree",
        "breeding_season": "April to June",
        "clutch_size": "Usually 5-7 eggs",
        "call": "Loud high-pitched chattering calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Spain: Castilla y León, Castilla-La Mancha, Extremadura, Andalusia, Madrid and other central and western regions; Portugal: central and southern regions"
    },
    "similar_birds": "Azure-winged Magpie is best separated from Eurasian Magpie by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Eurasian Magpie, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Iberian Magpie can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Baltimore Oriole",
    "scientific": "Icterus galbula",
    "description": "The Baltimore Oriole is a colourful North American blackbird. Adult males have bright orange underparts with black upperparts and wings, while females are generally more yellow-orange and brown. It spends much of its time in mature trees, searching among leaves for insects and feeding on fruit and nectar.",
    "image": "BaltimoreOriole1.jpg",
    "quick_facts": {
        "family": "Icteridae",
        "size": "17-19 cm",
        "weight": "About 30-40 g",
        "wingspan": "About 23-30 cm",
        "diet": "insects, fruit and nectar",
        "habitat": "deciduous woodland, woodland edges, parks and gardens",
        "behaviour": "forages high in trees and often searches blossoms for food",
        "activity": "Diurnal",
        "nesting": "A deep hanging pouch woven from plant fibres and suspended from a tree branch",
        "breeding_season": "April to August",
        "clutch_size": "Usually 3-7 eggs",
        "call": "Rich whistled song and sharp chattering calls",
        "lifespan": "Often several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Canada: southern provinces; United States: eastern and central states; Mexico and Central America during winter"
    },
    "similar_birds": "Baltimore Oriole is best separated from Orchard Oriole by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Orchard Oriole, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Scarlet Tanager can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "Cornell Lab of Ornithology — All About Birds / eBird",
        "Audubon — North American bird identification and natural history",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Barn Owl",
    "scientific": "Tyto alba",
    "description": "Recognising the Barn Owl starts with a pale owl with a heart-shaped facial disk, long wings and a ghostly appearance in flight. The species uses farmland, grassland, open woodland, barns and other open habitats and takes mainly small mammals, especially rodents as its principal food. It hunts mostly at night with slow, silent flights close to the ground. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "BarnOwl1.jpg",
    "quick_facts": {
        "family": "Tytonidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "mainly small mammals, especially rodents",
        "habitat": "farmland, grassland, open woodland, barns and other open habitats",
        "behaviour": "hunts mostly at night with slow, silent flights close to the ground",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Barn Owl is best separated from Short-eared Owl by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Short-eared Owl, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Little Owl can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — Birds of the World / eBird",
        "IUCN Red List of Threatened Species",
        "Raptors of the World / regional raptor references"
    ]
},

{
    "name": "Bay-Backed Shrike",
    "scientific": "Lanius vittatus",
    "description": "The Bay-Backed Shrike is a compact shrike with a chestnut back, black mask and hooked bill. It is found in thorn scrub, open woodland, farmland and dry country, where it feeds mainly on large insects, small reptiles and occasionally small birds. The species is often noticed because it perches conspicuously and scans for prey before dropping onto it. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "Bay-BackedShrike1.jpg",
    "quick_facts": {
        "family": "Laniidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "large insects, small reptiles and occasionally small birds",
        "habitat": "thorn scrub, open woodland, farmland and dry country",
        "behaviour": "perches conspicuously and scans for prey before dropping onto it",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Bay-Backed Shrike is best separated from Long-tailed Shrike by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Long-tailed Shrike, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Brown Shrike can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Black Bulbul",
    "scientific": "Hypsipetes leucocephalus",
    "description": "The Black Bulbul is a dark bulbul with a crest, pale bill and variable grey or black plumage, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in forest, woodland, plantations and wooded gardens and feeds mainly on fruit, berries and insects. It moves actively through foliage and often joins small feeding groups. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "BlackBulbul1.jpg",
    "quick_facts": {
        "family": "Pycnonotidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fruit, berries and insects",
        "habitat": "forest, woodland, plantations and wooded gardens",
        "behaviour": "moves actively through foliage and often joins small feeding groups",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Black Bulbul is best separated from Red-vented Bulbul by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Red-vented Bulbul, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Black-crested Bulbul can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Black Drongo",
    "scientific": "Dicrurus macrocercus",
    "description": "The Black Drongo is a glossy black drongo with a deeply forked tail and strong straight bill, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in open woodland, farmland, grassland and roadside trees and feeds mainly on flying insects and other small invertebrates. It uses prominent perches and makes quick aerial attacks on insects. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "BlackDrongo1.jpg",
    "quick_facts": {
        "family": "Dicruridae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "flying insects and other small invertebrates",
        "habitat": "open woodland, farmland, grassland and roadside trees",
        "behaviour": "uses prominent perches and makes quick aerial attacks on insects",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Black Drongo is best separated from Ashy Drongo by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Ashy Drongo, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. White-bellied Drongo can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Black Kite",
    "scientific": "Milvus migrans",
    "description": "The Black Kite is a medium-sized brown raptor with long wings and a forked tail. It is found in open country, farmland, wetlands, cities and woodland edges, where it feeds mainly on carrion, small animals, insects and discarded food. The species is often noticed because it soars and glides for long periods while searching widely for food. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "BlackKite1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "carrion, small animals, insects and discarded food",
        "habitat": "open country, farmland, wetlands, cities and woodland edges",
        "behaviour": "soars and glides for long periods while searching widely for food",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Black Kite is best separated from Brahminy Kite by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Brahminy Kite, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Black-winged Kite can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Black Redstart",
    "scientific": "Phoenicurus ochruros",
    "description": "The Black Redstart is a dark red-tailed chat with a charcoal body and constantly flicking tail. It is found in rocky areas, cliffs, buildings, towns and open scrub, where it feeds mainly on insects and other small invertebrates. The species is often noticed because it perches on exposed surfaces and repeatedly dips its tail. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "BlackRedstart1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects and other small invertebrates",
        "habitat": "rocky areas, cliffs, buildings, towns and open scrub",
        "behaviour": "perches on exposed surfaces and repeatedly dips its tail",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Black Redstart is best separated from Common Redstart by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Common Redstart, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Black-throated Thrush can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "British Trust for Ornithology — European bird ecology and monitoring",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Black-breasted Weaver",
    "scientific": "Ploceus benghalensis",
    "description": "The Black-breasted Weaver is a small Indian weaver associated with grassland, reedbeds and agricultural landscapes. Breeding males have a distinctive dark breast, while females and non-breeding birds are much duller. Like other weavers, it constructs its nest by weaving grass and other plant fibres together.",
    "image": "Black-BreastedWeaver1.jpg",
    "quick_facts": {
        "family": "Ploceidae",
        "size": "12-14 cm",
        "weight": "About 18-25 g",
        "wingspan": "About 20-23 cm",
        "diet": "seeds and insects",
        "habitat": "grassland, river plains, reeds and agricultural areas",
        "behaviour": "forages in groups and males construct woven nests",
        "activity": "Diurnal",
        "nesting": "A woven hanging nest made from grass and plant fibres, usually attached to tall vegetation",
        "breeding_season": "Usually during the monsoon and wet season",
        "clutch_size": "Usually 2-4 eggs",
        "call": "Short chattering and buzzing calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "India: northern and northeastern states including Rajasthan, Gujarat, Punjab, Haryana, Uttar Pradesh, Bihar, West Bengal and Assam; Nepal; Bangladesh"
    },
    "similar_birds": "Black-breasted Weaver is best separated from Baya Weaver by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Baya Weaver, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Streaked Weaver can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Black-Crowned Night Heron",
    "scientific": "Nycticorax nycticorax",
    "description": "The Black-Crowned Night Heron is a stocky heron with a black crown and back, pale body and red eyes in adults. It is found in marshes, lakes, rivers, mangroves and other wetlands, where it feeds mainly on fish, frogs, crustaceans and aquatic insects. The species is often noticed because it often stands motionless at the water's edge and is most active around dusk and night. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "Black-CrownedNightHeron1.jpg",
    "quick_facts": {
        "family": "Ardeidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fish, frogs, crustaceans and aquatic insects",
        "habitat": "marshes, lakes, rivers, mangroves and other wetlands",
        "behaviour": "often stands motionless at the water's edge and is most active around dusk and night",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Black-Crowned Night Heron is best separated from Indian Pond Heron by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Indian Pond Heron, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Grey Heron can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Black-faced Cuckooshrike",
    "scientific": "Coracina novaehollandiae",
    "description": "The Black-faced Cuckooshrike is a medium-sized Australian bird with grey plumage, a distinctive black face and a broad dark bill. Despite its name, it is neither a cuckoo nor a shrike, but belongs to the cuckooshrike family. It is commonly encountered in open woodland, farmland, parks and suburban areas, where it moves through trees searching for insects and other food. Black-faced Cuckooshrikes are often seen singly, in pairs or in small family groups and have a characteristic habit of sitting upright on exposed branches. Their flight is strong and direct, with steady wingbeats.",
    "image": "Black-FacedCuckooshrike1.jpg",
    "quick_facts": {
        "family": "Campephagidae",
        "size": "31-36 cm",
        "weight": "About 90-120 g",
        "wingspan": "About 45-50 cm",
        "diet": "insects, fruit and small invertebrates",
        "habitat": "woodland, open forest, scrub and gardens",
        "behaviour": "moves methodically through foliage and often occurs in small groups",
        "activity": "Diurnal",
        "nesting": "A small, shallow nest constructed from plant material and spider web",
        "breeding_season": "Usually spring and summer",
        "clutch_size": "Usually 2-4 eggs",
        "call": "Soft, musical and chattering calls",
        "lifespan": "Often several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: widespread across Queensland, New South Wales, Victoria, South Australia, Western Australia, the Northern Territory and Tasmania"
    },
    "similar_birds": "Black-faced Cuckooshrike is best separated from White-bellied Cuckooshrike by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with White-bellied Cuckooshrike, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Black-winged Cuckooshrike can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Black-Headed Ibis",
    "scientific": "Threskiornis melanocephalus",
    "description": "The Black-Headed Ibis is a large ibis with a dark bare head, pale body and long down-curved bill, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in marshes, flooded fields, wetlands and grassland and feeds mainly on invertebrates, frogs, fish and other small animals. It probes soft ground and shallow water while walking steadily. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "Black-HeadedIbis1.jpg",
    "quick_facts": {
        "family": "Threskiornithidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "invertebrates, frogs, fish and other small animals",
        "habitat": "marshes, flooded fields, wetlands and grassland",
        "behaviour": "probes soft ground and shallow water while walking steadily",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟡 Near Threatened (NT)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Black-Headed Ibis is best separated from Black-faced Ibis by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Black-faced Ibis, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Red-naped Ibis can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Black-Hooded Oriole",
    "scientific": "Oriolus xanthornus",
    "description": "The Black-Hooded Oriole is a bright yellow oriole with a contrasting black hood and wings. It is found in open woodland, gardens, plantations and cultivated country, where it feeds mainly on fruit and insects. The species is often noticed because it usually forages high in trees among leaves and flowers. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "Black-HoodedOriole1.jpg",
    "quick_facts": {
        "family": "Oriolidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fruit and insects",
        "habitat": "open woodland, gardens, plantations and cultivated country",
        "behaviour": "usually forages high in trees among leaves and flowers",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Black-Hooded Oriole is best separated from Black-naped Oriole by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Black-naped Oriole, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Indian Golden Oriole can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Black-naped Monarch",
    "scientific": "Hypothymis azurea",
    "description": "The Black-naped Monarch is a small and elegant Asian flycatcher. Males are bright blue with a distinctive black patch across the nape and black throat, while females are generally duller. It is an active insect hunter that often makes short aerial sallies from perches in forest vegetation.",
    "image": "Black-NapedMonarch1.jpg",
    "quick_facts": {
        "family": "Monarchidae",
        "size": "15-17 cm",
        "weight": "About 8-12 g",
        "wingspan": "About 20-25 cm",
        "diet": "flying insects and other arthropods",
        "habitat": "forest, woodland, plantations and shaded gardens",
        "behaviour": "makes short sallies from low or middle perches",
        "activity": "Diurnal",
        "nesting": "A small cup-shaped nest attached to a branch or fork, often held together with spider web",
        "breeding_season": "Generally spring and summer, varying by region",
        "clutch_size": "Usually 2-3 eggs",
        "call": "Clear high-pitched whistles and short calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "India: most wooded regions including Kerala, Karnataka, Tamil Nadu, Maharashtra, Odisha, West Bengal and northeastern states; Sri Lanka; Bangladesh; Nepal; Bhutan; Myanmar; Thailand; Malaysia; Indonesia and the Philippines"
    },
    "similar_birds": "Black-naped Monarch is best separated from Indian Paradise Flycatcher by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Indian Paradise Flycatcher, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Black-naped Blue Flycatcher can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Black-Naped Oriole",
    "scientific": "Oriolus chinensis",
    "description": "The Black-Naped Oriole is a yellow and black oriole with a dark eye stripe and pointed bill, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in woodland, forest edges, gardens and plantations and feeds mainly on fruit, nectar and insects. It feeds actively in the canopy and gives clear whistled calls. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "Black-NapedOriole1.jpg",
    "quick_facts": {
        "family": "Oriolidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fruit, nectar and insects",
        "habitat": "woodland, forest edges, gardens and plantations",
        "behaviour": "feeds actively in the canopy and gives clear whistled calls",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Black-Naped Oriole is best separated from Black-hooded Oriole by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Black-hooded Oriole, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Indian Golden Oriole can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Black-Rumped Flameback",
    "scientific": "Dinopium benghalense",
    "description": "The Black-Rumped Flameback is a striking golden-backed woodpecker with a black rump, red crest in males and strong bill. It is found in woodland, forest edges, plantations and gardens with mature trees, where it feeds mainly on ants, beetle larvae and other insects. The species is often noticed because it climbs trunks and branches while probing or hammering wood. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "Black-RumpedFlameback1.jpg",
    "quick_facts": {
        "family": "Picidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "ants, beetle larvae and other insects",
        "habitat": "woodland, forest edges, plantations and gardens with mature trees",
        "behaviour": "climbs trunks and branches while probing or hammering wood",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Black-Rumped Flameback is best separated from Lesser Goldenback by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Lesser Goldenback, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Greater Flameback can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Black-Winged Kite",
    "scientific": "Elanus caeruleus",
    "description": "The Black-Winged Kite is a small pale raptor with black shoulder and wing markings and a hovering hunting style. It is found in grassland, farmland, scrub and open country, where it feeds mainly on rodents, lizards, insects and small birds. The species is often noticed because it hovers almost in place while scanning the ground. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "Black-WingedKite1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "rodents, lizards, insects and small birds",
        "habitat": "grassland, farmland, scrub and open country",
        "behaviour": "hovers almost in place while scanning the ground",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Black-Winged Kite is best separated from Black Kite by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Black Kite, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Brahminy Kite can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — Birds of the World / eBird",
        "IUCN Red List of Threatened Species",
        "Raptors of the World / regional raptor references"
    ]
},

{
    "name": "Black-winged Stilt",
    "scientific": "Himantopus himantopus",
    "description": "The Black-winged Stilt is a very long-legged wader with a thin straight bill and sharply contrasting black-and-white plumage, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in shallow wetlands, lagoons, rice fields and mudflats and feeds mainly on aquatic insects, crustaceans, molluscs and small aquatic animals. It wades through shallow water and often calls loudly when disturbed. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "Black-WingedStilt1.jpg",
    "quick_facts": {
        "family": "Recurvirostridae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "aquatic insects, crustaceans, molluscs and small aquatic animals",
        "habitat": "shallow wetlands, lagoons, rice fields and mudflats",
        "behaviour": "wades through shallow water and often calls loudly when disturbed",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Black-winged Stilt is best separated from Pied Stilt by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Pied Stilt, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Avocet can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Blue Jay",
    "scientific": "Cyanocitta cristata",
    "description": "The Blue Jay is a striking North American corvid with bright blue, black and white plumage, a prominent crest and a long tail. It is an intelligent and adaptable bird found in forests, woodland edges, parks and suburban areas. Blue Jays are especially associated with acorns and other nuts, which they often carry away and cache for later use. They are social birds and have a wide variety of calls.",
    "image": "BlueJay1.jpg",
    "quick_facts": {
        "family": "Corvidae",
        "size": "25-30 cm",
        "weight": "About 70-100 g",
        "wingspan": "About 34-43 cm",
        "diet": "acorns, nuts, seeds, fruit and insects",
        "habitat": "woodland, woodland edges, parks and suburbs",
        "behaviour": "caches food and often travels in family groups",
        "activity": "Diurnal",
        "nesting": "An open cup of twigs, roots, grass and other plant material placed in a tree or shrub",
        "breeding_season": "April to July",
        "clutch_size": "Usually 3-7 eggs",
        "call": "Loud jay calls, harsh jeers, whistles and other varied vocalisations",
        "lifespan": "Often 7-10 years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Canada: southern and central provinces; United States: most eastern, central and northern states; Mexico: northern and eastern regions"
    },
    "similar_birds": "Blue Jay is best separated from Steller's Jay by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Steller's Jay, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Canada Jay can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "Cornell Lab of Ornithology — All About Birds / eBird",
        "Audubon — North American bird identification and natural history",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Blue-eared Kingfisher",
    "scientific": "Alcedo meninting",
    "description": "The Blue-eared Kingfisher is a small forest kingfisher with deep blue upperparts and rich orange underparts. It is found in shaded forest streams, wetlands and dense woodland, where it feeds mainly on small fish, crustaceans and aquatic insects. The species is often noticed because it perches quietly near water before making short hunting dives. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "Blue-EaredKingfisher1.jpg",
    "quick_facts": {
        "family": "Alcedinidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "small fish, crustaceans and aquatic insects",
        "habitat": "shaded forest streams, wetlands and dense woodland",
        "behaviour": "perches quietly near water before making short hunting dives",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Blue-eared Kingfisher is best separated from Common Kingfisher by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Common Kingfisher, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. White-throated Kingfisher can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Blue-faced Honeyeater",
    "scientific": "Entomyzon cyanotis",
    "description": "The Blue-faced Honeyeater is a large and conspicuous Australian honeyeater named for the brilliant blue skin surrounding its eyes. Adults have black heads and necks, golden olive-green upperparts and pale underparts, giving them a distinctive combination of colours. Juveniles have less strongly coloured facial skin. It is a noisy and social species, usually seen in pairs or small flocks. Blue-faced Honeyeaters feed on nectar and fruit but also take insects and other small food items. They are especially associated with open woodland and areas near water, but they have adapted well to orchards, plantations, parks and gardens. In tropical regions they are sometimes called Banana-birds because they readily visit banana plants.",
    "image": "Blue-FacedHoneyeater1.jpg",
    "quick_facts": {
        "family": "Meliphagidae",
        "size": "26-32 cm",
        "weight": "About 60-80 g",
        "wingspan": "About 40-45 cm",
        "diet": "nectar, fruit and insects",
        "habitat": "woodland, open forest, mangroves, orchards and gardens",
        "behaviour": "moves noisily through trees and often gathers in social groups",
        "activity": "Diurnal",
        "nesting": "A cup-shaped nest made from grass, bark and other plant fibres, usually placed in a tree or shrub",
        "breeding_season": "Usually August to January, varying with location",
        "clutch_size": "Usually 2-3 eggs",
        "call": "Loud, varied and chattering calls",
        "lifespan": "Usually several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: Queensland, New South Wales, northern Victoria and parts of the Northern Territory and Western Australia; also New Guinea and nearby islands"
    },
    "similar_birds": "Blue-faced Honeyeater is best separated from Noisy Miner by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Noisy Miner, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Little Wattlebird can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Blue-Tailed Bee-Eater",
    "scientific": "Merops philippinus",
    "description": "Recognising the Blue-Tailed Bee-Eater starts with a slender bee-eater with green plumage, a blue tail and dark facial markings. The species uses open country, wetlands, riverbanks and forest clearings and takes bees, wasps, dragonflies and other flying insects as its principal food. It hunts from exposed perches and returns to the same perch after aerial sallies. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "Blue-TailedBee-Eater1.jpg",
    "quick_facts": {
        "family": "Meropidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "bees, wasps, dragonflies and other flying insects",
        "habitat": "open country, wetlands, riverbanks and forest clearings",
        "behaviour": "hunts from exposed perches and returns to the same perch after aerial sallies",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Blue-Tailed Bee-Eater is best separated from Asian Green Bee-eater by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Asian Green Bee-eater, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Blue-throated Bee-eater can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Blue-throated Bee-eater",
    "scientific": "Merops viridis",
    "description": "The Blue-throated Bee-eater is a colourful Southeast Asian bee-eater with a green body, blue throat, dark eye stripe and long pointed wings. Like other bee-eaters, it catches flying insects from exposed perches and often returns to the same perch after each aerial pursuit.",
    "image": "Blue-ThroatedBee-Eater1.jpg",
    "quick_facts": {
        "family": "Meropidae",
        "size": "24-27 cm",
        "weight": "About 30-45 g",
        "wingspan": "About 35-40 cm",
        "diet": "flying insects, especially bees and wasps",
        "habitat": "forest edges, open woodland, plantations and riverine habitats",
        "behaviour": "makes rapid aerial feeding flights from perches",
        "activity": "Diurnal",
        "nesting": "Excavates a tunnel in a sandy bank or other soft substrate",
        "breeding_season": "Varies geographically",
        "clutch_size": "Usually 2-5 eggs",
        "call": "High-pitched rapid chattering calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "India: mainly northeastern regions; Bangladesh; Myanmar; Thailand; Cambodia; Vietnam; Malaysia; Indonesia and the Philippines"
    },
    "similar_birds": "Blue-throated Bee-eater is best separated from Blue-tailed Bee-eater by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Blue-tailed Bee-eater, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Asian Green Bee-eater can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Brahminy Kite",
    "scientific": "Haliastur indus",
    "description": "The Brahminy Kite is a chestnut-and-white raptor with a white head and chestnut body, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in coasts, rivers, wetlands, estuaries and open woodland and feeds mainly on fish, carrion, crustaceans and small animals. It soars low over water and often scavenges around shorelines. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "BrahminyKite1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fish, carrion, crustaceans and small animals",
        "habitat": "coasts, rivers, wetlands, estuaries and open woodland",
        "behaviour": "soars low over water and often scavenges around shorelines",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Brahminy Kite is best separated from Black Kite by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Black Kite, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. White-bellied Sea-Eagle can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — Birds of the World / eBird",
        "IUCN Red List of Threatened Species",
        "Raptors of the World / regional raptor references"
    ]
},

{
    "name": "Brahminy Starling",
    "scientific": "Sturnia pagodarum",
    "description": "Recognising the Brahminy Starling starts with a crested starling with a pale body, dark head and warm orange-brown mantle. The species uses open woodland, farmland, gardens and dry country and takes fruit, insects and seeds as its principal food. It usually occurs in pairs or small groups and feeds both on the ground and in trees. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "BrahminyStarling1.jpg",
    "quick_facts": {
        "family": "Sturnidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fruit, insects and seeds",
        "habitat": "open woodland, farmland, gardens and dry country",
        "behaviour": "usually occurs in pairs or small groups and feeds both on the ground and in trees",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Brahminy Starling is best separated from Common Myna by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Common Myna, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Indian Pied Starling can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Brolga",
    "scientific": "Antigone rubicunda",
    "description": "The Brolga is a large Australian crane with long legs, a long neck, grey plumage and a distinctive red patch of bare skin on the head. It is particularly associated with wetlands and open grasslands in northern and eastern Australia. Brolgas feed on roots, tubers, seeds and small animals and may forage in shallow water or on dry ground. They are famous for their elaborate courtship displays, during which pairs may bow, leap, spread their wings and toss vegetation into the air. Brolgas can form large groups outside the breeding season and are one of Australia's most recognizable native cranes.",
    "image": "Brolga1.jpg",
    "quick_facts": {
        "family": "Gruidae",
        "size": "95-125 cm",
        "weight": "About 3.6-8.7 kg",
        "wingspan": "About 170-240 cm",
        "diet": "roots, tubers, seeds, grasses and small animals",
        "habitat": "wetlands, floodplains, grassland and open woodland",
        "behaviour": "performs spectacular jumping and bowing courtship displays",
        "activity": "Diurnal",
        "nesting": "A platform of vegetation built on a shallow wetland or nearby ground",
        "breeding_season": "Usually during the wet season, varying geographically",
        "clutch_size": "Usually 2 eggs",
        "call": "Loud trumpeting calls that carry over long distances",
        "lifespan": "Often many years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: mainly Queensland, New South Wales, Victoria, the Northern Territory and northern Western Australia"
    },
    "similar_birds": "Brolga is best separated from Sarus Crane by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Sarus Crane, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Common Crane can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Brown Fish Owl",
    "scientific": "Ketupa zeylonensis",
    "description": "The Brown Fish Owl is a large Asian owl strongly associated with water. It has warm brown plumage, prominent ear tufts, a heavily streaked body and powerful talons suited to catching fish and other aquatic prey. It often sits quietly on a waterside perch before suddenly dropping down to seize prey.",
    "image": "BrownFishOwl1.jpg",
    "quick_facts": {
        "family": "Strigidae",
        "size": "48-57 cm",
        "weight": "About 1.1-2.5 kg",
        "wingspan": "About 125-140 cm",
        "diet": "fish, frogs, crustaceans and small vertebrates",
        "habitat": "wooded rivers, streams, lakes and forest near water",
        "behaviour": "often hunts from a waterside perch, especially around dusk and night",
        "activity": "Mostly nocturnal and crepuscular",
        "nesting": "Uses tree hollows, rock ledges, cavities or abandoned nests",
        "breeding_season": "November to April",
        "clutch_size": "Usually 1-3 eggs",
        "call": "Deep hoots, grunts and harsh calls",
        "lifespan": "Often lives for many years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "India: northern, central, western, southern and northeastern regions; Sri Lanka; Nepal; Bangladesh; Pakistan and parts of Southeast Asia"
    },
    "similar_birds": "Brown Fish Owl is best separated from Spot-bellied Eagle-Owl by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Spot-bellied Eagle-Owl, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Brown Boobook can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Brown Pelican",
    "scientific": "Pelecanus occidentalis",
    "description": "The Brown Pelican is a large coastal pelican with a long bill and an enormous expandable throat pouch. It is famous for plunge-diving from the air to catch fish, sometimes dropping from considerable height before entering the water. It is commonly seen along coasts, bays and estuaries.",
    "image": "BrownPelican1.jpg",
    "quick_facts": {
        "family": "Pelecanidae",
        "size": "106-137 cm",
        "weight": "About 2.7-5.9 kg",
        "wingspan": "About 183-228 cm",
        "diet": "fish and other marine animals",
        "habitat": "coasts, estuaries, bays, lagoons and islands",
        "behaviour": "often plunge-dives from the air to catch fish",
        "activity": "Diurnal",
        "nesting": "Colonial nests made from sticks and vegetation, usually in trees, bushes or on islands",
        "breeding_season": "Varies geographically",
        "clutch_size": "Usually 2-4 eggs",
        "call": "Adults are generally quiet; young produce begging calls",
        "lifespan": "Can live for more than 30 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "United States: Atlantic, Gulf and Pacific coastal states; Mexico: Pacific and Gulf coasts; Central America, northern South America and Caribbean islands"
    },
    "similar_birds": "Brown Pelican is best separated from American White Pelican by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with American White Pelican, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Australian Pelican can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Brown Rock Chat",
    "scientific": "Oenanthe fusca",
    "description": "Recognising the Brown Rock Chat starts with a warm brown chat with a pale throat and upright posture, often found around rocks and buildings. The species uses rocky slopes, cliffs, ruins, villages and dry open country and takes insects and other small invertebrates as its principal food. It runs and hops over open ground and frequently perches on rocks or walls. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "BrownRockChat1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects and other small invertebrates",
        "habitat": "rocky slopes, cliffs, ruins, villages and dry open country",
        "behaviour": "runs and hops over open ground and frequently perches on rocks or walls",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Brown Rock Chat is best separated from Indian Robin by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Indian Robin, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Black Redstart can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Brown-Headed Barbet",
    "scientific": "Psilopogon zeylanicus",
    "description": "Recognising the Brown-Headed Barbet starts with a stocky green barbet with a brown head and heavy pale bill. The species uses woodland, gardens, orchards and forest edges and takes fruit, berries, flowers and insects as its principal food. It clings to branches while feeding and often calls repeatedly from the canopy. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "Brown-HeadedBarbet1.jpg",
    "quick_facts": {
        "family": "Megalaimidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fruit, berries, flowers and insects",
        "habitat": "woodland, gardens, orchards and forest edges",
        "behaviour": "clings to branches while feeding and often calls repeatedly from the canopy",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Brown-Headed Barbet is best separated from Coppersmith Barbet by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Coppersmith Barbet, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Lineated Barbet can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — Birds of the World / eBird",
        "Handbook of the Birds of the World / BirdLife International",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Budgerigar",
    "scientific": "Melopsittacus undulatus",
    "description": "The Budgerigar is a small, slender Australian parrot famous worldwide as a popular cage bird but naturally occurring in large numbers across the Australian interior. Wild Budgerigars are predominantly green and yellow with black barring on the head, back and wings. They are highly social and can form enormous flocks, particularly after rainfall when temporary water sources and fresh grass seeds become available. They feed mainly on seeds on the ground and may travel long distances in search of food and water. Their ability to survive in Australia's dry interior makes them one of the country's most successful small parrots.",
    "image": "Budgerigar1.jpg",
    "quick_facts": {
        "family": "Psittaculidae",
        "size": "18 cm",
        "weight": "About 30-40 g",
        "wingspan": "About 30 cm",
        "diet": "grass seeds and other plant material",
        "habitat": "open woodland, grassland, scrub and dry inland country",
        "behaviour": "forms large nomadic flocks and travels widely in search of water and seed",
        "activity": "Diurnal",
        "nesting": "A natural tree hollow or similar cavity",
        "breeding_season": "Mainly after rainfall when food is plentiful",
        "clutch_size": "Usually 4-6 eggs",
        "call": "Continuous cheerful chirping and chattering calls in flight and around feeding areas",
        "lifespan": "Often 5-10 years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: widespread across Queensland, New South Wales, Victoria, South Australia, Western Australia and the Northern Territory, particularly across the interior"
    },
    "similar_birds": "Budgerigar is best separated from Elegant Parrot by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Elegant Parrot, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Bourke's Parrot can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Cattle Egret",
    "scientific": "Bubulcus ibis",
    "description": "The Cattle Egret is a compact white egret that often develops orange-buff breeding plumage on the head, neck and back. It is found in pastures, farmland, wetlands and grassland, where it feeds mainly on insects, frogs, small reptiles and other animals disturbed by grazing livestock. The species is often noticed because it often walks beside cattle and other large animals to catch flushed prey. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "CattleEgret1.jpg",
    "quick_facts": {
        "family": "Ardeidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects, frogs, small reptiles and other animals disturbed by grazing livestock",
        "habitat": "pastures, farmland, wetlands and grassland",
        "behaviour": "often walks beside cattle and other large animals to catch flushed prey",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Cattle Egret is best separated from Little Egret by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Little Egret, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Indian Pond Heron can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Cedar Waxwing",
    "scientific": "Bombycilla cedrorum",
    "description": "The Cedar Waxwing is a sleek North American songbird with silky brown and grey plumage, a black facial mask, a yellow-tipped tail and small red wax-like tips on some wing feathers. It is highly social and often travels in flocks while searching for berries and fruit.",
    "image": "CedarWaxwing1.jpg",
    "quick_facts": {
        "family": "Bombycillidae",
        "size": "14-17 cm",
        "weight": "About 32 g",
        "wingspan": "About 22-30 cm",
        "diet": "berries and fruit, plus insects during breeding",
        "habitat": "woodland, orchards, gardens and suburban areas with fruiting trees",
        "behaviour": "moves in flocks and passes food between individuals",
        "activity": "Diurnal",
        "nesting": "A loose cup of twigs, grass and plant fibres placed in a tree or shrub",
        "breeding_season": "June to August",
        "clutch_size": "Usually 2-6 eggs",
        "call": "High, thin and lisping whistles",
        "lifespan": "Up to about 8 years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Canada: southern and central provinces; United States: most states; Mexico and Central America during winter"
    },
    "similar_birds": "Cedar Waxwing is best separated from Bohemian Waxwing by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Bohemian Waxwing, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. European Starling can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "Cornell Lab of Ornithology — All About Birds / eBird",
        "Audubon — North American bird identification and natural history",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Chestnut-bellied Sandgrouse",
    "scientific": "Pterocles exustus",
    "description": "The Chestnut-bellied Sandgrouse is a compact desert sandgrouse with cryptic sandy plumage and a rich chestnut belly, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in arid plains, scrub, desert and semi-desert country and feeds mainly on seeds and other plant material. It travels in flocks between feeding areas and water sources. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "Chestnut-BelliedSandgrouse1.jpg",
    "quick_facts": {
        "family": "Pteroclidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "seeds and other plant material",
        "habitat": "arid plains, scrub, desert and semi-desert country",
        "behaviour": "travels in flocks between feeding areas and water sources",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Chestnut-bellied Sandgrouse is best separated from Painted Sandgrouse by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Painted Sandgrouse, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Black-bellied Sandgrouse can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Cockatiel",
    "scientific": "Nymphicus hollandicus",
    "description": "The Cockatiel is a slender Australian cockatoo with a long tail, prominent erectile crest and distinctive orange cheek patches. Wild Cockatiels are predominantly grey, with males developing brighter yellow facial colouring as they mature. They are highly social and are often seen in pairs or flocks, particularly around water sources and areas with abundant grass seeds. The species is well adapted to Australia's inland environments and can travel considerable distances in search of food and water. Wild Cockatiels usually feed on the ground and spend the hottest part of the day resting in trees or shrubs.",
    "image": "Cockatiel1.jpg",
    "quick_facts": {
        "family": "Cacatuidae",
        "size": "30-33 cm",
        "weight": "About 80-100 g",
        "wingspan": "About 45-50 cm",
        "diet": "grass seeds, grains, fruits and other plant material",
        "habitat": "open woodland, grassland, scrubland and dry inland areas",
        "behaviour": "travels in pairs or flocks and may gather in large numbers around water",
        "activity": "Diurnal",
        "nesting": "A tree hollow containing little or no nesting material",
        "breeding_season": "Usually after rainfall when food is abundant",
        "clutch_size": "Usually 4-7 eggs",
        "call": "Loud whistles, contact calls and chattering",
        "lifespan": "Often several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: widespread across Queensland, New South Wales, South Australia, Western Australia and the Northern Territory, especially in inland regions"
    },
    "similar_birds": "Cockatiel is best separated from Galah by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Galah, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Budgerigar can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Common Chaffinch",
    "scientific": "Fringilla coelebs",
    "description": "The Common Chaffinch is one of Europe's most familiar finches and is especially common in woodland, gardens, parks, farmland, and villages. Adult males have a blue-grey crown, pinkish-red underparts, chestnut back, and conspicuous white wing bars, while females and juveniles are more subdued brown and olive. Chaffinches feed mainly on seeds and other plant material, with insects becoming particularly important when adults feed their young. Their distinctive descending song is one of the characteristic sounds of spring in many parts of Europe.",
    "image": "CommonChaffinch1.jpg",
    "quick_facts": {
        "family": "Fringillidae",
        "size": "14–16 cm",
        "weight": "Approximately 22 g",
        "wingspan": "24.5–28.5 cm",
        "diet": "seeds, insects and other small invertebrates",
        "habitat": "woodland, farmland, hedgerows, parks and gardens",
        "behaviour": "forages mostly on the ground and often sings from a conspicuous perch",
        "activity": "Diurnal",
        "nesting": "Deep cup-shaped nest decorated with moss and lichen, usually built in a fork of a tree or shrub",
        "breeding_season": "Generally April to July",
        "clutch_size": "Usually 4–5 eggs",
        "call": "Distinctive descending song ending in a flourish, with several short contact and alarm calls",
        "lifespan": "Typical life expectancy after reaching breeding age is around 3 years; maximum recorded age is almost 14 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "United Kingdom: England, Scotland, Wales, and Northern Ireland; Ireland; France: Brittany, Normandy, Île-de-France, and other regions; Germany: Bavaria, Hesse, Saxony, and other regions; Spain: Galicia, Catalonia, Andalusia, and other regions; Italy: Lombardy, Tuscany, Lazio, and other regions; Poland: Masovia, Lesser Poland, and other regions; Sweden: Götaland, Svealand, and Norrland; widespread across Europe, North Africa, and western Asia."
    },
    "similar_birds": "Common Chaffinch is best separated from European Greenfinch by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with European Greenfinch, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. European Goldfinch can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "British Trust for Ornithology — European bird ecology and monitoring",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Common Hawk-Cuckoo",
    "scientific": "Hierococcyx varius",
    "description": "The Common Hawk-Cuckoo is a medium-sized cuckoo with barred underparts and a hawk-like appearance in flight. It is found in woodland, forest edges, gardens and cultivated country, where it feeds mainly on caterpillars and other insects. The species is often noticed because it is often heard rather than seen and is a brood parasite. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "CommonHawk-Cuckoo1.jpg",
    "quick_facts": {
        "family": "Cuculidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "caterpillars and other insects",
        "habitat": "woodland, forest edges, gardens and cultivated country",
        "behaviour": "is often heard rather than seen and is a brood parasite",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Common Hawk-Cuckoo is best separated from Asian Koel by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Asian Koel, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Eurasian Cuckoo can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — Birds of the World / eBird",
        "IUCN Red List of Threatened Species",
        "Raptors of the World / regional raptor references"
    ]
},

{
    "name": "Common Hoopoe",
    "scientific": "Upupa epops",
    "description": "The Common Hoopoe is a striking bird with a long curved bill, orange crest, black-and-white wings and barred tail, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in open woodland, farmland, orchards and dry grassland and feeds mainly on insects and their larvae, especially beetles and grubs. It forages on the ground by probing soil with its long bill. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "CommonHoopoe1.jpg",
    "quick_facts": {
        "family": "Upupidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects and their larvae, especially beetles and grubs",
        "habitat": "open woodland, farmland, orchards and dry grassland",
        "behaviour": "forages on the ground by probing soil with its long bill",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Common Hoopoe is best separated from Eurasian Hoopoe by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Eurasian Hoopoe, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Indian Roller can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Common Iora",
    "scientific": "Aegithina tiphia",
    "description": "The Common Iora is a small active bird with rounded wings and contrasting yellow and dark plumage. It is found in woodland, scrub, gardens and forest edges, where it feeds mainly on insects, spiders and other arthropods. The species is often noticed because it moves rapidly through foliage and often performs short display flights. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "CommonIora1.jpg",
    "quick_facts": {
        "family": "Aegithinidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects, spiders and other arthropods",
        "habitat": "woodland, scrub, gardens and forest edges",
        "behaviour": "moves rapidly through foliage and often performs short display flights",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Common Iora is best separated from Common Leafbird by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Common Leafbird, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Golden-fronted Leafbird can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Common Kestrel",
    "scientific": "Falco tinnunculus",
    "description": "The Common Kestrel is a small falcon famous for hovering almost motionless while searching the ground for prey. It has long, pointed wings and a long tail, with males generally showing a grey head and tail while females have more extensively barred brown plumage. Kestrels mainly hunt small mammals such as voles but also take insects, reptiles, and small birds. They occur in open habitats including farmland, grassland, scrub, cliffs, and urban areas where suitable hunting grounds and nesting sites are available.",
    "image": "CommonKestrel1.jpg",
    "quick_facts": {
        "family": "Falconidae",
        "size": "32–39 cm",
        "weight": "Approximately 160–290 g",
        "wingspan": "65–82 cm",
        "diet": "seeds, insects, fruit and other suitable foods",
        "habitat": "woodland and open habitats",
        "behaviour": "forages actively and uses a range of vocal calls",
        "activity": "Diurnal",
        "nesting": "Usually nests in cavities, buildings, cliffs, nest boxes, or abandoned nests of other birds rather than building its own nest",
        "breeding_season": "Generally April to July",
        "clutch_size": "Usually 4–5 eggs",
        "call": "Repeated sharp 'kee-kee-kee' calls, particularly around the nest",
        "lifespan": "Typical life expectancy after reaching breeding age is around 4 years; maximum recorded age is almost 16 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "United Kingdom: England, Scotland, Wales, and Northern Ireland; France: Normandy, Brittany, Provence, and other regions; Germany: Bavaria, Saxony, Hesse, and other regions; Spain: Catalonia, Andalusia, Castile, and other open regions; Italy: Lombardy, Tuscany, Sicily, and other regions; Poland: Masovia, Lesser Poland, and other regions; Sweden: Götaland, Svealand, and Norrland; Greece: Attica, Central Macedonia, and other regions; widespread across Europe, Africa, and much of Asia."
    },
    "similar_birds": "Common Kestrel is best separated from Merlin by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Merlin, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Peregrine Falcon can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — Birds of the World / eBird",
        "IUCN Red List of Threatened Species",
        "Raptors of the World / regional raptor references"
    ]
},

{
    "name": "Common Kingfisher",
    "scientific": "Alcedo atthis",
    "description": "The Common Kingfisher is a compact blue-and-orange kingfisher with a long dagger-like bill. It is found in rivers, streams, lakes, ponds, canals and wetlands, where it feeds mainly on small fish and aquatic insects. The species is often noticed because it perches quietly above water before diving sharply for prey. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "CommonKingfisher1.jpg",
    "quick_facts": {
        "family": "Alcedinidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "small fish and aquatic insects",
        "habitat": "rivers, streams, lakes, ponds, canals and wetlands",
        "behaviour": "perches quietly above water before diving sharply for prey",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Common Kingfisher is best separated from White-throated Kingfisher by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with White-throated Kingfisher, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Blue-eared Kingfisher can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — Birds of the World / eBird",
        "Handbook of the Birds of the World / BirdLife International",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Common Myna",
    "scientific": "Acridotheres tristis",
    "description": "The Common Myna is a brown starling with a black head, yellow bill and bright yellow bare skin around the eye, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in towns, farmland, gardens, parks and open woodland and feeds mainly on insects, fruit, seeds, scraps and many other foods. It walks confidently on the ground and often forages around people. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "CommonMyna1.jpg",
    "quick_facts": {
        "family": "Sturnidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects, fruit, seeds, scraps and many other foods",
        "habitat": "towns, farmland, gardens, parks and open woodland",
        "behaviour": "walks confidently on the ground and often forages around people",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Common Myna is best separated from Brahminy Starling by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Brahminy Starling, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Indian Pied Starling can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Common Nightingale",
    "scientific": "Luscinia megarhynchos",
    "description": "The Common Nightingale is a relatively plain brown songbird whose extraordinary vocal ability has made it one of Europe's most famous songbirds. It has warm brown upperparts, a reddish-brown tail, and pale underparts, with little of the bright plumage associated with many other European songbirds. Nightingales prefer dense scrub, woodland edges, hedgerows, river valleys, and other habitats with thick vegetation close to the ground. Males are famous for singing both during the day and at night during the breeding season, often from concealed positions.",
    "image": "CommonNightingale1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "15–16.5 cm",
        "weight": "Approximately 21 g",
        "wingspan": "Approximately 23–26 cm",
        "diet": "seeds, insects, fruit and other suitable foods",
        "habitat": "woodland and open habitats",
        "behaviour": "forages actively and uses a range of vocal calls",
        "activity": "Diurnal and nocturnal during the breeding season",
        "nesting": "Open cup nest built low to the ground among dense vegetation and leaf litter",
        "breeding_season": "Generally April to July",
        "clutch_size": "Usually 4–5 eggs",
        "call": "A powerful, varied song containing whistles, trills, repeated phrases, and rich musical notes",
        "lifespan": "Typically around 2 years after reaching breeding age; maximum recorded age is over 8 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "United Kingdom: mainly southern and eastern England; France: Île-de-France, Nouvelle-Aquitaine, Occitanie, and other suitable regions; Spain: Galicia, Castile, Andalusia, and other regions; Portugal: Lisbon, Alentejo, and other regions; Italy: Tuscany, Lazio, Lombardy, and other regions; Germany: Brandenburg, Saxony, and other suitable areas; Poland: Masovia, Lesser Poland, and other regions; migrates to sub-Saharan Africa during the non-breeding season."
    },
    "similar_birds": "Common Nightingale is best separated from European Robin by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with European Robin, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Bluethroat can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "British Trust for Ornithology — European bird ecology and monitoring",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Common Rosefinch",
    "scientific": "Carpodacus erythrinus",
    "description": "The Common Rosefinch is a distinctive bird with characteristic plumage and structure. It is found in woodland, open country and other suitable habitats, where it feeds mainly on a varied diet appropriate to its habitat. The species is often noticed because it forages in characteristic ways and uses a range of calls. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "CommonRosefinch1.jpg",
    "quick_facts": {
        "family": "Fringillidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "seeds, insects, fruit and other suitable foods",
        "habitat": "woodland and open habitats",
        "behaviour": "forages actively and uses a range of vocal calls",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Common Rosefinch is best separated from Scarlet Finch by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Scarlet Finch, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. House Finch can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "British Trust for Ornithology — European bird ecology and monitoring",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Common Sandpiper",
    "scientific": "Actitis hypoleucos",
    "description": "Recognising the Common Sandpiper starts with a small brown-and-white wader with a white eye-stripe and characteristic bobbing movement. The species uses riverbanks, ponds, lakes, mudflats and sheltered coasts and takes insects, worms, crustaceans and other small invertebrates as its principal food. It feeds along the water's edge with a constant teetering motion. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "CommonSandpiper1.jpg",
    "quick_facts": {
        "family": "Scolopacidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects, worms, crustaceans and other small invertebrates",
        "habitat": "riverbanks, ponds, lakes, mudflats and sheltered coasts",
        "behaviour": "feeds along the water's edge with a constant teetering motion",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Common Sandpiper is best separated from Green Sandpiper by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Green Sandpiper, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Wood Sandpiper can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "British Trust for Ornithology — European bird ecology and monitoring",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Common Stonechat",
    "scientific": "Saxicola torquatus",
    "description": "Recognising the Common Stonechat starts with a compact chat with a dark head, orange breast and pale collar, especially vivid in breeding males. The species uses heathland, grassland, scrub, farmland and coastal slopes and takes insects, spiders and other small invertebrates as its principal food. It perches upright on bushes, fences and posts while scanning for prey. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "CommonStonechat1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects, spiders and other small invertebrates",
        "habitat": "heathland, grassland, scrub, farmland and coastal slopes",
        "behaviour": "perches upright on bushes, fences and posts while scanning for prey",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Common Stonechat is best separated from European Stonechat by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with European Stonechat, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Whinchat can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "British Trust for Ornithology — European bird ecology and monitoring",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Common Tailorbird",
    "scientific": "Orthotomus sutorius",
    "description": "Recognising the Common Tailorbird starts with a tiny greenish warbler with a long upright tail and rusty crown in many adults. The species uses gardens, scrub, plantations and forest edges and takes insects, spiders and other small arthropods as its principal food. It keeps low in vegetation and stitches or binds leaves when building its nest. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "CommonTailorbird1.jpg",
    "quick_facts": {
        "family": "Cisticolidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects, spiders and other small arthropods",
        "habitat": "gardens, scrub, plantations and forest edges",
        "behaviour": "keeps low in vegetation and stitches or binds leaves when building its nest",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Common Tailorbird is best separated from Ashy Prinia by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Ashy Prinia, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Plain Prinia can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Coppersmith Barbet",
    "scientific": "Psilopogon haemacephalus",
    "description": "Recognising the Coppersmith Barbet starts with a compact green barbet with a red-and-yellow face and thick pale bill. The species uses woodland, orchards, gardens and urban trees and takes fruit, berries and insects as its principal food. It often remains hidden in foliage while giving its repetitive metallic call. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "CoppersmithBarbet1.jpg",
    "quick_facts": {
        "family": "Megalaimidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fruit, berries and insects",
        "habitat": "woodland, orchards, gardens and urban trees",
        "behaviour": "often remains hidden in foliage while giving its repetitive metallic call",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Coppersmith Barbet is best separated from Brown-headed Barbet by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Brown-headed Barbet, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. White-cheeked Barbet can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — Birds of the World / eBird",
        "Handbook of the Birds of the World / BirdLife International",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Crested Bunting",
    "scientific": "Emberiza lathami",
    "description": "The Crested Bunting is a distinctive Asian bunting with a prominent crest. Breeding males have rich chestnut and black plumage with contrasting markings, while females are duller. It is generally associated with open scrub, grassland, agricultural areas and woodland edges.",
    "image": "CrestedBunting1.jpg",
    "quick_facts": {
        "family": "Emberizidae",
        "size": "17-18 cm",
        "weight": "About 20-30 g",
        "wingspan": "About 25-29 cm",
        "diet": "seeds and insects",
        "habitat": "dry grassland, scrub and open woodland",
        "behaviour": "forages on the ground and sings from low perches",
        "activity": "Diurnal",
        "nesting": "A cup-shaped nest placed on or close to the ground in vegetation",
        "breeding_season": "April to July",
        "clutch_size": "Usually 3-5 eggs",
        "call": "Short metallic notes and a simple song",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "India: northern and northeastern regions including Himachal Pradesh, Uttarakhand, Rajasthan, Gujarat, Madhya Pradesh and Uttar Pradesh; Nepal; Bhutan; Bangladesh; Myanmar"
    },
    "similar_birds": "Crested Bunting is best separated from Black-headed Bunting by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Black-headed Bunting, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Grey-necked Bunting can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Crested Pigeon",
    "scientific": "Ocyphaps lophotes",
    "description": "The Crested Pigeon is a slender Australian pigeon with a long pointed crest, a grey-brown body and striking dark wing markings. It is commonly found in open country, grasslands, farmland, parks and urban areas, where it often walks along the ground searching for food. When disturbed, it takes off with rapid wingbeats that produce a distinctive whistling sound. Crested Pigeons usually feed on the ground and are often seen singly, in pairs or in small groups. They drink regularly and may gather in large numbers around water sources in dry regions.",
    "image": "CrestedPigeon1.jpg",
    "quick_facts": {
        "family": "Columbidae",
        "size": "30-34 cm",
        "weight": "About 180-220 g",
        "wingspan": "About 45-50 cm",
        "diet": "seeds and grains",
        "habitat": "open woodland, grassland, farmland and urban areas",
        "behaviour": "often feeds on the ground and flies with a distinctive whistling wing sound",
        "activity": "Diurnal",
        "nesting": "A small platform of twigs placed in a tree or shrub",
        "breeding_season": "Usually throughout much of the year when conditions are favourable",
        "clutch_size": "Usually 2 eggs",
        "call": "Soft cooing calls and a distinctive whistling wing sound during flight",
        "lifespan": "Often several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: widespread across most mainland states and territories, including Queensland, New South Wales, Victoria, South Australia, Western Australia and the Northern Territory"
    },
    "similar_birds": "Crested Pigeon is best separated from Spotted Dove by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Spotted Dove, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Common Bronzewing can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Crested Serpent Eagle",
    "scientific": "Spilornis cheela",
    "description": "The Crested Serpent Eagle is a broad-winged dark eagle with a large crest and striking yellow facial skin, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in forest, woodland, plantations and wooded hills and feeds mainly on snakes, lizards, frogs and other small animals. It often perches quietly before making short hunting flights. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "CrestedSerpentEagle1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "snakes, lizards, frogs and other small animals",
        "habitat": "forest, woodland, plantations and wooded hills",
        "behaviour": "often perches quietly before making short hunting flights",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Crested Serpent Eagle is best separated from Crested Hawk-Eagle by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Crested Hawk-Eagle, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Changeable Hawk-Eagle can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — Birds of the World / eBird",
        "IUCN Red List of Threatened Species",
        "Raptors of the World / regional raptor references"
    ]
},

{
    "name": "Crimson Rosella",
    "scientific": "Platycercus elegans",
    "description": "The Crimson Rosella is a colourful eastern Australian parrot with brilliant crimson plumage, blue patches on the cheeks and wings, and a long blue tail in the typical form. Several geographical colour forms occur across its range. It feeds on seeds, fruit and flowers and can occur in forests as well as well-treed urban areas.",
    "image": "CrimsonRosella1.jpg",
    "quick_facts": {
        "family": "Psittaculidae",
        "size": "32-36 cm",
        "weight": "About 90-170 g",
        "wingspan": "About 50-55 cm",
        "diet": "seeds, fruit, flowers and insects",
        "habitat": "woodland, forest, gardens and montane habitats",
        "behaviour": "feeds in trees and on the ground and often travels in small groups",
        "activity": "Diurnal",
        "nesting": "A tree hollow containing decayed wood material",
        "breeding_season": "September to January",
        "clutch_size": "Usually 3-8 eggs",
        "call": "Loud whistles and harsh chattering calls",
        "lifespan": "Often lives for 10-15 years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: Queensland, New South Wales, Victoria, South Australia, Western Australia and Australian Capital Territory"
    },
    "similar_birds": "Crimson Rosella is best separated from Eastern Rosella by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Eastern Rosella, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Australian King-Parrot can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Crimson Sunbird",
    "scientific": "Aethopyga siparaja",
    "description": "Recognising the Crimson Sunbird starts with a tiny nectar-feeding bird whose breeding male has brilliant crimson plumage and a dark blue hood. The species uses forest, gardens, plantations and flowering woodland and takes nectar and small insects as its principal food. It moves rapidly between flowers and often hovers briefly. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "CrimsonSunbird1.jpg",
    "quick_facts": {
        "family": "Nectariniidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "nectar and small insects",
        "habitat": "forest, gardens, plantations and flowering woodland",
        "behaviour": "moves rapidly between flowers and often hovers briefly",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Crimson Sunbird is best separated from Purple Sunbird by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Purple Sunbird, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Purple-rumped Sunbird can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Eastern Rosella",
    "scientific": "Platycercus eximius",
    "description": "The Eastern Rosella is a colourful parrot of southeastern Australia, easily recognised by its red head and breast, white cheek patches, yellow-green body and bright blue shoulders. Its striking plumage makes it one of the most recognisable rosellas. Eastern Rosellas are often seen feeding on the ground, where they use their strong bills to collect seeds, grasses and other plant material. They can also climb through trees and feed on fruits, buds and flowers. The species has adapted well to human-modified environments and is commonly seen in farmland, parks, gardens and golf courses. It is somewhat similar to the Pale-headed Rosella, but the Eastern Rosella has a strongly red head and distinctive white cheek patches.",
    "image": "EasternRosella1.jpg",
    "quick_facts": {
        "family": "Psittaculidae",
        "size": "28-32 cm",
        "weight": "About 90-125 g",
        "wingspan": "About 42-48 cm",
        "diet": "seeds, fruit, flowers and insects",
        "habitat": "woodland, farmland, parks and gardens",
        "behaviour": "feeds on the ground and in trees, often in pairs or small groups",
        "activity": "Diurnal",
        "nesting": "A natural tree hollow, usually containing a bed of decayed wood",
        "breeding_season": "August to January",
        "clutch_size": "Usually 4-6 eggs",
        "call": "Clear, repeated whistles and chattering calls",
        "lifespan": "Often several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: southeastern Queensland, New South Wales, Victoria and southeastern South Australia"
    },
    "similar_birds": "Eastern Rosella is best separated from Crimson Rosella by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Crimson Rosella, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Pale-headed Rosella can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Eastern Spinebill",
    "scientific": "Acanthorhynchus tenuirostris",
    "description": "The Eastern Spinebill is a small Australian honeyeater with a very long, slender, down-curved bill. It is an energetic nectar feeder that often hovers around flowering plants. It also catches insects and can be found in forests, heathlands, woodlands and gardens.",
    "image": "EasternSpinebill1.jpg",
    "quick_facts": {
        "family": "Meliphagidae",
        "size": "15-19 cm",
        "weight": "About 10-17 g",
        "wingspan": "About 18-22 cm",
        "diet": "nectar and insects",
        "habitat": "heathland, woodland, forest edges and gardens with tubular flowers",
        "behaviour": "hovers at flowers and moves quickly between blossoms",
        "activity": "Diurnal",
        "nesting": "A small cup of twigs, grass, bark and spider web placed in a tree or shrub",
        "breeding_season": "August to January",
        "clutch_size": "Usually 2 eggs",
        "call": "Short high-pitched piping notes and other soft calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: Queensland, New South Wales, Victoria, South Australia, Tasmania and Australian Capital Territory"
    },
    "similar_birds": "Eastern Spinebill is best separated from Eastern Yellow Robin by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Eastern Yellow Robin, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. New Holland Honeyeater can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Eastern Yellow Robin",
    "scientific": "Eopsaltria australis",
    "description": "The Eastern Yellow Robin is a small Australian songbird with a grey head and back and bright yellow underparts. It belongs to the Australasian robin family, which is unrelated to the European Robin despite the shared common name. Eastern Yellow Robins are often remarkably approachable and may sit quietly on low branches while watching for prey. They feed mainly on insects and spiders, usually dropping from a low perch to catch food on the ground. The species occurs in woodland and rainforest as well as parks and gardens. Northern and southern populations differ somewhat in plumage intensity, but the yellow underparts remain a defining feature.",
    "image": "EasternYellowRobin1.jpg",
    "quick_facts": {
        "family": "Petroicidae",
        "size": "15-17 cm",
        "weight": "About 18-22 g",
        "wingspan": "About 25-30 cm",
        "diet": "insects and spiders",
        "habitat": "woodland, rainforest, forest edges and gardens",
        "behaviour": "often sits low and pounces onto prey on the ground",
        "activity": "Diurnal",
        "nesting": "A woven cup of bark, grass and spider web placed in a tree fork",
        "breeding_season": "July to January",
        "clutch_size": "Usually 2 eggs, with up to three clutches possible",
        "call": "High bell-like piping notes and repeated calls",
        "lifespan": "Usually several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: eastern and southeastern mainland, especially coastal and adjacent inland regions from Queensland through New South Wales to Victoria and South Australia"
    },
    "similar_birds": "Eastern Yellow Robin is best separated from Scarlet Robin by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Scarlet Robin, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. White-browed Robin can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Emu",
    "scientific": "Dromaius novaehollandiae",
    "description": "The Emu is Australia's tallest native bird and one of the world's largest living birds. It is flightless, with greatly reduced wings but extremely powerful legs adapted for running. Adults have shaggy grey-brown feathers, a long neck and a partly bare bluish-black head and neck. Emus are generally solitary outside the breeding period and can travel considerable distances when food or water becomes scarce. Their diet is varied and includes fruits, seeds, shoots, insects and other small animals. One of the most unusual aspects of their reproduction is that the male takes responsibility for incubating the eggs and caring for the young after the female leaves.",
    "image": "Emu1.jpg",
    "quick_facts": {
        "family": "Casuariidae",
        "size": "160-200 cm tall",
        "weight": "Up to about 60 kg",
        "wingspan": "Flightless; wings are greatly reduced",
        "diet": "plants, fruit, seeds, insects and other small animals",
        "habitat": "savanna woodland, grassland, scrub and open country",
        "behaviour": "walks long distances and may travel widely when food or water is scarce",
        "activity": "Diurnal",
        "nesting": "A thick platform of grass and vegetation built on the ground",
        "breeding_season": "April to June",
        "clutch_size": "5-15 eggs",
        "call": "Deep booming, drumming and grunting sounds",
        "lifespan": "Usually around 10-20 years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: widespread across much of the mainland, from coastal regions to inland areas and the Snowy Mountains"
    },
    "similar_birds": "Emu is best separated from Southern Cassowary by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Southern Cassowary, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Australian Bustard can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Eurasian Coot",
    "scientific": "Fulica atra",
    "description": "The Eurasian Coot is a dark waterbird with a white bill and frontal shield and large lobed toes, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in lakes, marshes, rivers and slow-moving waters and feeds mainly on aquatic plants, algae, invertebrates and some small animals. It swims actively and often dives for food. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "EurasianCoot1.jpg",
    "quick_facts": {
        "family": "Rallidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "aquatic plants, algae, invertebrates and some small animals",
        "habitat": "lakes, marshes, rivers and slow-moving waters",
        "behaviour": "swims actively and often dives for food",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Eurasian Coot is best separated from Common Moorhen by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Common Moorhen, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Black Coot can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Eurasian Jay",
    "scientific": "Garrulus glandarius",
    "description": "The Eurasian Jay is a colorful member of the crow family, with pinkish-brown plumage, a black-and-white face, a pale rump, and a striking blue-and-black barred patch on the wings. It is primarily a woodland bird but also occurs in parks, large gardens, farmland, and other areas containing mature trees. Jays are intelligent and adaptable birds with a varied diet that includes acorns, insects, fruits, seeds, eggs, and small animals. They are particularly important in the dispersal of oak trees because they carry acorns away from parent trees and bury them for later use.",
    "image": "EurasianJay1.jpg",
    "quick_facts": {
        "family": "Corvidae",
        "size": "32–35 cm",
        "weight": "Approximately 167 g",
        "wingspan": "52–58 cm",
        "diet": "seeds, insects, fruit and other suitable foods",
        "habitat": "woodland and open habitats",
        "behaviour": "forages actively and uses a range of vocal calls",
        "activity": "Diurnal",
        "nesting": "Cup-shaped nest built from twigs and lined with finer plant material, usually placed in a tree",
        "breeding_season": "Generally March to July",
        "clutch_size": "4–5 eggs",
        "call": "Loud, harsh, rasping alarm calls; also produces quieter calls and vocal imitations",
        "lifespan": "Typically around 4 years after reaching breeding age; maximum recorded age is over 16 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "United Kingdom: England, Scotland, Wales, and Northern Ireland; Ireland; France: Normandy, Brittany, Île-de-France, and other wooded regions; Germany: Bavaria, Saxony, Hesse, and other forested areas; Spain: Catalonia, Galicia, and other wooded regions; Italy: Lombardy, Tuscany, Lazio, and other regions; Poland: Masovia, Lesser Poland, and other forested areas; Sweden: Götaland, Svealand, and southern Norrland; widespread across much of Europe and parts of western Asia and North Africa."
    },
    "similar_birds": "Eurasian Jay is best separated from Eurasian Magpie by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Eurasian Magpie, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Western Jackdaw can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Eurasian Magpie",
    "scientific": "Pica pica",
    "description": "The Eurasian Magpie is a highly recognizable member of the crow family, with contrasting black-and-white plumage, a very long graduated tail, and glossy blue-green iridescence on its wings and tail. It is highly adaptable and occurs in farmland, woodland edges, grassland, parks, gardens, villages, and cities. Magpies are omnivorous and eat insects, seeds, fruits, small animals, eggs, carrion, and food around human settlements. Their intelligence and curiosity have made them prominent in European folklore and culture.",
    "image": "EurasianMagpie1.jpg",
    "quick_facts": {
        "family": "Corvidae",
        "size": "40–51 cm",
        "weight": "Approximately 213 g",
        "wingspan": "52–60 cm",
        "diet": "seeds, insects, fruit and other suitable foods",
        "habitat": "woodland and open habitats",
        "behaviour": "forages actively and uses a range of vocal calls",
        "activity": "Diurnal",
        "nesting": "Large domed nest constructed from twigs, usually with a mud-lined cup and a roof of branches",
        "breeding_season": "Generally March to July",
        "clutch_size": "Usually 5–6 eggs",
        "call": "Loud repetitive 'chac-chac-chac' calls and other harsh vocalizations",
        "lifespan": "Typical life expectancy after reaching breeding age is around 5 years; maximum recorded age is over 21 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "United Kingdom: England, Scotland, Wales, and Northern Ireland; Ireland; France: Île-de-France, Normandy, Occitanie, and other regions; Germany: Bavaria, Saxony, Hesse, and other regions; Spain: Catalonia, Madrid, Castile, and other regions; Italy: Lombardy, Piedmont, Veneto, and other regions; Poland: Masovia, Lesser Poland, and other regions; Sweden: Götaland, Svealand, and southern Norrland; widespread across much of Europe, North Africa, and Asia."
    },
    "similar_birds": "Eurasian Magpie is best separated from Eurasian Jay by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Eurasian Jay, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Azure-winged Magpie can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "European Bee-eater",
    "scientific": "Merops apiaster",
    "description": "The European Bee-eater is one of Europe's most vividly coloured birds, with a turquoise-blue underside, golden-yellow throat, chestnut crown and back, green wings and a black eye stripe. It is a highly aerial insect hunter that catches bees, wasps, dragonflies and other flying insects while in flight. Despite its name, bees make up only part of its diet. After catching a stinging insect, the bird may return to a perch and manipulate the prey before swallowing it. European Bee-eaters are strongly migratory across much of their range, breeding mainly in southern and central Europe before travelling to Africa for winter. They often nest colonially by digging tunnels into sandy or vertical banks.",
    "image": "EuropeanBee-eater1.jpg",
    "quick_facts": {
        "family": "Meropidae",
        "size": "27-30 cm",
        "weight": "44-78 g",
        "wingspan": "44-49 cm",
        "diet": "bees, wasps, dragonflies and other flying insects",
        "habitat": "open woodland, riverbanks, grassland and sandy areas",
        "behaviour": "hunts from exposed perches and returns to the same perch after each flight",
        "activity": "Diurnal",
        "nesting": "Digs a long tunnel into sandy banks, cliffs or similar exposed ground; often nests in colonies",
        "breeding_season": "May to August",
        "clutch_size": "Usually 6-7 eggs",
        "call": "A lively, rolling and frequently repeated 'pruu-pruu' type call",
        "lifespan": "Around 6 years is a commonly reported figure, though individuals can live longer",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Europe: mainly southern and central Europe; also parts of western Asia and northern Africa. Migrates to sub-Saharan Africa for winter"
    },
    "similar_birds": "European Bee-eater is best separated from Asian Green Bee-eater by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Asian Green Bee-eater, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. European Roller can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "British Trust for Ornithology — European bird ecology and monitoring",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "European Goldfinch",
    "scientific": "Carduelis carduelis",
    "description": "The European Goldfinch is a small and colorful finch distinguished by its bright red face, black-and-white head, brown body, and vivid yellow wing panels. It is commonly associated with lightly wooded landscapes, farmland, gardens, parks, scrub, and areas containing tall seed-producing plants. Its long, pointed bill is particularly well suited to extracting seeds from thistles, teasels, burdocks, and similar plants. Goldfinches often form flocks outside the breeding season and may gather in large numbers where abundant food is available.",
    "image": "EuropeanGoldfinch1.jpg",
    "quick_facts": {
        "family": "Fringillidae",
        "size": "12–13.5 cm",
        "weight": "Approximately 16 g",
        "wingspan": "21–25.5 cm",
        "diet": "seeds, insects, fruit and other suitable foods",
        "habitat": "woodland and open habitats",
        "behaviour": "forages actively and uses a range of vocal calls",
        "activity": "Diurnal",
        "nesting": "Small cup-shaped nest built in trees or shrubs and usually concealed among foliage",
        "breeding_season": "Generally April to August, varying by region",
        "clutch_size": "Usually 5 eggs",
        "call": "Tinkling and twittering calls; song is a rapid, musical series of notes",
        "lifespan": "Typically around 2 years after reaching breeding age; maximum recorded age is over 10 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "United Kingdom: England, Scotland, Wales, and Northern Ireland; Ireland; France: Brittany, Normandy, Île-de-France, Provence, and other suitable regions; Germany: Bavaria, Hesse, Saxony, and other regions; Spain: Catalonia, Galicia, Andalusia, and other suitable areas; Italy: Lombardy, Tuscany, Sicily, and other regions; Poland: Masovia, Lesser Poland, and other regions; Sweden: Götaland, Svealand, and southern Sweden; widespread across much of Europe, western Asia, and parts of North Africa."
    },
    "similar_birds": "European Goldfinch is best separated from European Greenfinch by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with European Greenfinch, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Common Chaffinch can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "British Trust for Ornithology — European bird ecology and monitoring",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "European Greenfinch",
    "scientific": "Chloris chloris",
    "description": "The European Greenfinch is a stocky finch with predominantly green and yellow plumage, a stout pale bill, and bright yellow markings on the wings and tail. It is a familiar bird of gardens, farmland, hedgerows, parks, villages, and open woodland. Greenfinches feed mainly on seeds and plant material, using their powerful bills to handle relatively large seeds. They may gather in flocks outside the breeding season and frequently visit garden feeders.",
    "image": "EuropeanGreenfinch1.jpg",
    "quick_facts": {
        "family": "Fringillidae",
        "size": "14–15 cm",
        "weight": "Approximately 24–34 g",
        "wingspan": "24–28 cm",
        "diet": "seeds, insects, fruit and other suitable foods",
        "habitat": "woodland and open habitats",
        "behaviour": "forages actively and uses a range of vocal calls",
        "activity": "Diurnal",
        "nesting": "Cup-shaped nest made from grass, moss, roots, and other plant material, usually placed in shrubs or trees",
        "breeding_season": "Generally April to August",
        "clutch_size": "Usually 4–5 eggs",
        "call": "Twittering calls and a characteristic long, wheezing note",
        "lifespan": "Typically several years; survival can be reduced by disease in some populations",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "United Kingdom: England, Scotland, Wales, and Northern Ireland; Ireland; France: Brittany, Normandy, Provence, and other regions; Germany: Bavaria, Hesse, Saxony, and other regions; Spain: Galicia, Catalonia, Andalusia, and other regions; Italy: Lombardy, Tuscany, Sicily, and other regions; Poland: Masovia, Lesser Poland, and other regions; Sweden: Götaland and Svealand; widespread across much of Europe, North Africa, and western Asia."
    },
    "similar_birds": "European Greenfinch is best separated from European Goldfinch by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with European Goldfinch, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Common Chaffinch can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "British Trust for Ornithology — European bird ecology and monitoring",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "European Robin",
    "scientific": "Erithacus rubecula",
    "description": "The European Robin is a small, familiar songbird recognized by its bright orange-red breast, brown upperparts, and pale underside. It occurs in woodland, gardens, parks, hedgerows, scrub, and other habitats with dense vegetation and suitable ground for foraging. In Britain and Ireland it is especially familiar around gardens and human settlements, while elsewhere in Europe it is strongly associated with cool, damp woodland and thick undergrowth. It feeds mainly on insects, worms, spiders, and other small invertebrates during the warmer months, while seeds and berries become more important during winter. European Robins are highly territorial and can be surprisingly aggressive toward other robins despite their small size.",
    "image": "EuropeanRobin1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "12.5–14 cm",
        "weight": "Approximately 19 g",
        "wingspan": "20–22 cm",
        "diet": "seeds, insects, fruit and other suitable foods",
        "habitat": "woodland and open habitats",
        "behaviour": "forages actively and uses a range of vocal calls",
        "activity": "Diurnal",
        "nesting": "Cup-shaped nest built by the female in cavities, banks, recesses, roots, or other sheltered locations",
        "breeding_season": "Generally March to July, varying by region",
        "clutch_size": "4–5 eggs",
        "call": "A varied, clear, and melodious song with sharp alarm calls",
        "lifespan": "Typically around 2 years after reaching breeding age; maximum recorded age in ringing data is over 8 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "United Kingdom: England, Scotland, Wales, and Northern Ireland; Ireland; France: Brittany, Normandy, Île-de-France, Occitanie, and other suitable regions; Germany: Bavaria, Saxony, Hesse, and North Rhine-Westphalia; Spain: Galicia, Catalonia, Andalusia, and other wooded regions; Italy: Lombardy, Tuscany, Lazio, and other suitable areas; Poland: Masovia, Lesser Poland, and other wooded regions; Sweden: Götaland, Svealand, and southern Norrland; widespread across much of Europe and parts of western Asia and North Africa."
    },
    "similar_birds": "European Robin is best separated from Common Nightingale by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Common Nightingale, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Bluethroat can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "British Trust for Ornithology — European bird ecology and monitoring",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "European Roller",
    "scientific": "Coracias garrulus",
    "description": "The European Roller is a brightly coloured migratory bird with vivid blue to turquoise plumage, a brownish back, a dark head, and striking blue and black wings. It is associated mainly with warm open landscapes such as grasslands, agricultural areas, open woodland, steppes, and forest edges, where it hunts large insects from exposed perches. The species breeds across parts of southern, central, and eastern Europe and western Asia before migrating south to sub-Saharan Africa for the non-breeding season.",
    "image": "EuropeanRoller1.jpg",
    "quick_facts": {
        "family": "Coraciidae",
        "size": "Approximately 29–32 cm",
        "weight": "Approximately 140–190 g",
        "wingspan": "Approximately 52–58 cm",
        "diet": "seeds, insects, fruit and other suitable foods",
        "habitat": "woodland and open habitats",
        "behaviour": "forages actively and uses a range of vocal calls",
        "activity": "Diurnal",
        "nesting": "Uses natural or artificial cavities in trees, cliffs, banks, or buildings; usually does not construct a substantial nest",
        "breeding_season": "Generally April to July, with egg-laying often occurring from late May to mid-June",
        "clutch_size": "Usually 4–5 eggs",
        "call": "Harsh, crow-like calls and repeated rasping or grating notes",
        "lifespan": "Several years; generation time is estimated at around 5.6 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Spain: Extremadura, Andalusia, Castilla y León, and other suitable regions; Portugal; France: southern regions and Mediterranean areas; Italy: Tuscany, Lazio, Sicily, and other regions; Croatia; Hungary; Romania; Bulgaria; Greece; Ukraine; Russia: southern and western regions; Turkey; Kazakhstan and other parts of western and central Asia; migrates to sub-Saharan Africa during the non-breeding season. In India it occurs mainly as a passage migrant and localized summer migrant, with records from regions including Punjab, Gujarat, Rajasthan, Maharashtra, Karnataka, Tamil Nadu, Kerala, and other suitable areas."
    },
    "similar_birds": "European Roller is best separated from European Bee-eater by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with European Bee-eater, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Indian Roller can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "British Trust for Ornithology — European bird ecology and monitoring",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "European Serin",
    "scientific": "Serinus serinus",
    "description": "The European Serin is a tiny finch with a short, conical bill and predominantly yellow-green plumage. Males are especially bright on the face, breast and rump, while females and juveniles are duller and more heavily streaked. It is a lively bird that often feeds among grasses, weeds and shrubs and can also be found around orchards, gardens and open woodland. The species is widespread across much of southern and central Europe and has expanded northward in parts of its range. Its rapid, high-pitched song is often delivered from a prominent perch or while the bird is perched in vegetation. It is smaller and more compact than the European Greenfinch, with more heavily streaked plumage and a noticeably shorter bill.",
    "image": "EuropeanSerin1.jpg",
    "quick_facts": {
        "family": "Fringillidae",
        "size": "About 11-12 cm",
        "weight": "About 11 g",
        "wingspan": "About 18-20 cm",
        "diet": "seeds, buds and small invertebrates",
        "habitat": "open woodland, orchards, farmland, parks and gardens",
        "behaviour": "often forages in small groups and sings from exposed perches",
        "activity": "Diurnal",
        "nesting": "A small cup nest built in shrubs or trees, usually concealed among dense vegetation",
        "breeding_season": "Usually spring and summer, with two broods commonly possible",
        "clutch_size": "3-4 eggs",
        "call": "High, rapid and somewhat buzzing notes; males produce a fast, continuous song",
        "lifespan": "Typical life expectancy around 3 years after reaching breeding age",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Europe: especially southern and central Europe; also parts of western Asia and North Africa"
    },
    "similar_birds": "European Serin is best separated from European Goldfinch by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with European Goldfinch, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. European Greenfinch can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "British Trust for Ornithology — European bird ecology and monitoring",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "European Stonechat",
    "scientific": "Saxicola rubicola",
    "description": "The European Stonechat is a small, upright songbird usually seen perched prominently on bushes, fences or other exposed points. The male has a black head, white neck patch, orange-red breast and dark back, while the female is browner and less strongly marked. It is especially associated with heathland, rough grassland, coastal areas and scrub. Stonechats are active hunters that watch from a perch before dropping down to catch insects and other small prey. Many populations are resident or only partly migratory, while some birds move south in winter. It can be confused with the Whinchat, but the European Stonechat has a darker head and lacks the Whinchat's strong pale eyebrow.",
    "image": "EuropeanStonechat1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "About 11.5-13 cm",
        "weight": "About 15.8 g",
        "wingspan": "About 18-21 cm",
        "diet": "insects and other small invertebrates",
        "habitat": "heathland, grassland, scrub and open coastal country",
        "behaviour": "perches upright on shrubs and fences and flicks its tail",
        "activity": "Diurnal",
        "nesting": "A small cup nest hidden low in vegetation, often close to the ground",
        "breeding_season": "Mainly March to June, with later broods possible",
        "clutch_size": "5-6 eggs",
        "call": "Short, sharp calls; the song is a rapid series of clicking and musical notes",
        "lifespan": "Usually a few years after reaching breeding age",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Europe: widespread across western, central and southern Europe; also North Africa and western Asia"
    },
    "similar_birds": "European Stonechat is best separated from Common Stonechat by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Common Stonechat, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Whinchat can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "British Trust for Ornithology — European bird ecology and monitoring",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Galah",
    "scientific": "Eolophus roseicapilla",
    "description": "The Galah is a striking pink-and-grey cockatoo and one of Australia's most familiar parrots. Its head, neck and underparts are rose-pink, while its back, wings and undertail are grey. Galahs are highly social and are often seen in noisy flocks feeding on the ground or gathering in trees. They eat seeds, grains, roots and other plant material and have benefited in some regions from agricultural landscapes. Their strong social behaviour and adaptability have also allowed them to thrive around towns and cities. Galahs can sometimes form mixed groups with other cockatoos. Their bright plumage and energetic personalities make them particularly easy to recognise.",
    "image": "Galah1.jpg",
    "quick_facts": {
        "family": "Cacatuidae",
        "size": "35-36 cm",
        "weight": "About 270-350 g",
        "wingspan": "About 70-80 cm",
        "diet": "seeds, roots, fruit and other plant material",
        "habitat": "open woodland, farmland, grassland and urban areas",
        "behaviour": "forms large noisy flocks and feeds mainly on the ground",
        "activity": "Diurnal",
        "nesting": "A tree hollow lined with leaves or other material",
        "breeding_season": "Usually July to December",
        "clutch_size": "Usually 2-5 eggs",
        "call": "Loud, harsh screeches and repeated contact calls",
        "lifespan": "Can live for several decades",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: widespread across much of the continent, including all mainland states and territories"
    },
    "similar_birds": "Galah is best separated from Sulphur-crested Cockatoo by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Sulphur-crested Cockatoo, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Little Corella can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Golden Eagle",
    "scientific": "Aquila chrysaetos",
    "description": "The Golden Eagle is a huge and powerful eagle with dark brown plumage and golden-brown feathers around the head and neck. It is an adaptable mountain and open-country predator that uses its excellent eyesight to locate mammals and birds before pursuing them in powerful flight.",
    "image": "GoldenEagle1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "75-88 cm",
        "weight": "About 2.8-6.6 kg",
        "wingspan": "About 190-234 cm",
        "diet": "mammals, birds and carrion",
        "habitat": "mountains, moorland, open country and remote woodland",
        "behaviour": "soars over large territories and attacks prey with powerful feet",
        "activity": "Diurnal",
        "nesting": "A large stick nest often built on cliffs or in tall trees and reused for many years",
        "breeding_season": "February to July",
        "clutch_size": "Usually 1-4 eggs",
        "call": "Usually quiet; produces high whistles and other calls around the nest",
        "lifespan": "Can live for more than 20 years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Spain: Pyrenees, Cantabria, Castilla y León, Aragón, Catalonia, Andalusia and other mountainous regions; much of Europe, Asia and North America"
    },
    "similar_birds": "Golden Eagle is best separated from White-tailed Eagle by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with White-tailed Eagle, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Steppe Eagle can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — Birds of the World / eBird",
        "IUCN Red List of Threatened Species",
        "Raptors of the World / regional raptor references"
    ]
},

{
    "name": "Golden Pheasant",
    "scientific": "Chrysolophus pictus",
    "description": "The Golden Pheasant is a spectacular pheasant native to western China. The male has a brilliant golden crest, red body, orange-and-black neck ruff and a long barred tail, while the female is much more cryptically coloured. It is mainly terrestrial and spends much of its time searching through vegetation and leaf litter for food.",
    "image": "GoldenPheasant1.jpg",
    "quick_facts": {
        "family": "Phasianidae",
        "size": "90-105 cm including the tail",
        "weight": "About 450-700 g",
        "wingspan": "About 65-75 cm",
        "diet": "seeds, shoots, berries and invertebrates",
        "habitat": "temperate forest, woodland edges and dense vegetation",
        "behaviour": "forages mainly on the ground and males display their ornate plumage",
        "activity": "Diurnal",
        "nesting": "A ground nest hidden among dense vegetation",
        "breeding_season": "April to June",
        "clutch_size": "Usually 8-12 eggs",
        "call": "Short whistles and harsh alarm calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "China: Sichuan, Gansu, Shaanxi, Hubei and other central and western provinces; introduced populations occur in parts of the United Kingdom and elsewhere"
    },
    "similar_birds": "Golden Pheasant is best separated from Lady Amherst's Pheasant by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Lady Amherst's Pheasant, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Silver Pheasant can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Golden-Fronted Leafbird",
    "scientific": "Chloropsis aurifrons",
    "description": "The Golden-Fronted Leafbird is a green canopy bird with a yellow forehead and throat and a slender slightly curved bill. It is found in forest, woodland, plantations and mature gardens, where it feeds mainly on fruit, nectar and insects. The species is often noticed because it moves actively through foliage and often feeds high in trees. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "Golden-FrontedLeafbird1.jpg",
    "quick_facts": {
        "family": "Chloropseidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fruit, nectar and insects",
        "habitat": "forest, woodland, plantations and mature gardens",
        "behaviour": "moves actively through foliage and often feeds high in trees",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Golden-Fronted Leafbird is best separated from Common Iora by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Common Iora, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Blue-winged Leafbird can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Great Hornbill",
    "scientific": "Buceros bicornis",
    "description": "The Great Hornbill is a very large forest hornbill with a huge yellow-and-black bill and prominent casque, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in tropical forest, especially mature lowland and hill forest and feeds mainly on fruit, small animals and large insects. It spends much of its time in the canopy and nests in tree cavities. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "GreatHornbill1.jpg",
    "quick_facts": {
        "family": "Bucerotidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fruit, small animals and large insects",
        "habitat": "tropical forest, especially mature lowland and hill forest",
        "behaviour": "spends much of its time in the canopy and nests in tree cavities",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟠 Vulnerable (VU)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Great Hornbill is best separated from Malabar Pied Hornbill by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Malabar Pied Hornbill, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Indian Grey Hornbill can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — Birds of the World / eBird",
        "Handbook of the Birds of the World / BirdLife International",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Great Spotted Woodpecker",
    "scientific": "Dendrocopos major",
    "description": "The Great Spotted Woodpecker is a striking black-and-white woodpecker with bold red markings and a strong, chisel-shaped bill. Adults have a black back, white shoulder patches, white underparts, and red markings around the lower belly, while juveniles have a prominent red crown. It is most strongly associated with mature deciduous and mixed woodland, particularly areas containing dead or decaying trees where insects are abundant. It also eats tree seeds, nuts, and occasionally eggs or young birds. Its loud drumming is an important territorial and breeding signal and can often be heard before the bird is seen.",
    "image": "GreatSpottedWoodpecker1.jpg",
    "quick_facts": {
        "family": "Picidae",
        "size": "23–26 cm",
        "weight": "Approximately 79 g",
        "wingspan": "38–44 cm",
        "diet": "seeds, insects, fruit and other suitable foods",
        "habitat": "woodland and open habitats",
        "behaviour": "forages actively and uses a range of vocal calls",
        "activity": "Diurnal",
        "nesting": "Cavity excavated in a tree, usually in dead or softened wood",
        "breeding_season": "Generally April to June",
        "clutch_size": "4–6 eggs",
        "call": "Sharp calls and rapid, loud drumming",
        "lifespan": "Several years; maximum recorded age in ringing data is almost 12 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "United Kingdom: England, Scotland, Wales, and Northern Ireland; Ireland; France: Brittany, Normandy, Île-de-France, and other wooded regions; Germany: Bavaria, Saxony, Hesse, and other forested areas; Spain: Galicia, Catalonia, Asturias, and other wooded regions; Italy: Lombardy, Tuscany, Veneto, and other regions; Poland: Masovia, Lesser Poland, and other forested areas; Sweden: Götaland, Svealand, and Norrland; widespread across much of Europe, North Africa, and northern Asia."
    },
    "similar_birds": "Great Spotted Woodpecker is best separated from Lesser Spotted Woodpecker by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Lesser Spotted Woodpecker, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Middle Spotted Woodpecker can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — Birds of the World / eBird",
        "Handbook of the Birds of the World / BirdLife International",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Greater Coucal",
    "scientific": "Centropus sinensis",
    "description": "The Greater Coucal is a large dark cuckoo with chestnut wings, a long tail and a heavy bill, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in scrub, grassland, wetlands, gardens and woodland edges and feeds mainly on insects, frogs, lizards, small mammals, birds and fruit. It walks or clambers through dense vegetation rather than flying often. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "GreaterCoucal1.jpg",
    "quick_facts": {
        "family": "Cuculidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects, frogs, lizards, small mammals, birds and fruit",
        "habitat": "scrub, grassland, wetlands, gardens and woodland edges",
        "behaviour": "walks or clambers through dense vegetation rather than flying often",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Greater Coucal is best separated from Asian Koel by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Asian Koel, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Greater Racket-tailed Drongo can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Greater Flamingo",
    "scientific": "Phoenicopterus roseus",
    "description": "Recognising the Greater Flamingo starts with a tall pale pink flamingo with a long neck, long legs and a large pink-and-black bill. The species uses shallow lakes, lagoons, estuaries and saline wetlands and takes algae, small aquatic organisms and invertebrates as its principal food. It feeds by sweeping its bill through shallow water and mud. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "GreaterFlamingo1.jpg",
    "quick_facts": {
        "family": "Phoenicopteridae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "algae, small aquatic organisms and invertebrates",
        "habitat": "shallow lakes, lagoons, estuaries and saline wetlands",
        "behaviour": "feeds by sweeping its bill through shallow water and mud",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Greater Flamingo is best separated from Lesser Flamingo by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Lesser Flamingo, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Chilean Flamingo can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Greater Racket-Tailed Drongo",
    "scientific": "Dicrurus paradiseus",
    "description": "The Greater Racket-Tailed Drongo is a large glossy drongo with elongated outer tail feathers ending in racket-like tips. It is found in forest, woodland and plantations, where it feeds mainly on insects and other small animals. The species is often noticed because it hunts from perches and is an accomplished vocal mimic. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "GreaterRacket-TailedDrongo1.jpg",
    "quick_facts": {
        "family": "Dicruridae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects and other small animals",
        "habitat": "forest, woodland and plantations",
        "behaviour": "hunts from perches and is an accomplished vocal mimic",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Greater Racket-Tailed Drongo is best separated from Lesser Racket-tailed Drongo by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Lesser Racket-tailed Drongo, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Black Drongo can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Grey Butcherbird",
    "scientific": "Cracticus torquatus",
    "description": "The Grey Butcherbird is a stocky Australian songbird with a strong hooked bill, grey back, black head and white markings. It occurs in a wide range of habitats, including woodland, farmland, parks and suburban gardens. Grey Butcherbirds are active hunters and search from exposed perches for insects, small reptiles and other prey, which they may carry back to a favourite perch. They are also accomplished singers and can produce a surprisingly varied collection of whistles, notes and melodic phrases. Pairs are territorial and often remain in the same area for long periods.",
    "image": "GreyButcherbird1.jpg",
    "quick_facts": {
        "family": "Artamidae",
        "size": "27-30 cm",
        "weight": "About 80-100 g",
        "wingspan": "About 40-45 cm",
        "diet": "insects, small reptiles, birds and other small animals",
        "habitat": "woodland, open forest, farmland, parks and suburbs",
        "behaviour": "perches upright and watches for prey before dropping onto it",
        "activity": "Diurnal",
        "nesting": "A cup-shaped nest made from twigs, grass and other plant material",
        "breeding_season": "Usually July to January",
        "clutch_size": "Usually 2-4 eggs",
        "call": "Rich whistles, warbling notes and varied musical calls",
        "lifespan": "Often several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: widespread across Queensland, New South Wales, Victoria, South Australia and Western Australia, with additional populations in Tasmania"
    },
    "similar_birds": "Grey Butcherbird is best separated from Pied Butcherbird by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Pied Butcherbird, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Australian Magpie can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Grey Francolin",
    "scientific": "Ortygornis pondicerianus",
    "description": "The Grey Francolin is a medium-sized partridge with finely barred grey-brown plumage and a chestnut neck pattern, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in dry grassland, farmland, scrub and open woodland and feeds mainly on seeds, shoots, grains and insects. It runs quickly through cover and often forages in small groups. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "GreyFrancolin1.jpg",
    "quick_facts": {
        "family": "Phasianidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "seeds, shoots, grains and insects",
        "habitat": "dry grassland, farmland, scrub and open woodland",
        "behaviour": "runs quickly through cover and often forages in small groups",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Grey Francolin is best separated from Black Francolin by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Black Francolin, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Red-legged Partridge can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Grey Heron",
    "scientific": "Ardea cinerea",
    "description": "Recognising the Grey Heron starts with a large grey heron with long legs, long neck and dagger-like bill. The species uses rivers, lakes, marshes, estuaries and coastal wetlands and takes fish, amphibians, small mammals and other aquatic animals as its principal food. It stands motionless before striking rapidly at prey. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "GreyHeron1.jpg",
    "quick_facts": {
        "family": "Ardeidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fish, amphibians, small mammals and other aquatic animals",
        "habitat": "rivers, lakes, marshes, estuaries and coastal wetlands",
        "behaviour": "stands motionless before striking rapidly at prey",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Grey Heron is best separated from Purple Heron by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Purple Heron, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Great Egret can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Grey-Breasted Prinia",
    "scientific": "Prinia hodgsonii",
    "description": "The Grey-Breasted Prinia is a distinctive bird with characteristic plumage and structure. It is found in woodland, open country and other suitable habitats, where it feeds mainly on a varied diet appropriate to its habitat. The species is often noticed because it forages in characteristic ways and uses a range of calls. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "Grey-BreastedPrinia1.jpg",
    "quick_facts": {
        "family": "Cisticolidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "seeds, insects, fruit and other suitable foods",
        "habitat": "woodland and open habitats",
        "behaviour": "forages actively and uses a range of vocal calls",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Grey-Breasted Prinia is best separated from Ashy Prinia by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Ashy Prinia, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Plain Prinia can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Grey-Headed Fish Eagle",
    "scientific": "Icthyophaga ichthyaetus",
    "description": "The Grey-Headed Fish Eagle is a distinctive bird with characteristic plumage and structure. It is found in woodland, open country and other suitable habitats, where it feeds mainly on a varied diet appropriate to its habitat. The species is often noticed because it forages in characteristic ways and uses a range of calls. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "Grey-HeadedFishEagle1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "seeds, insects, fruit and other suitable foods",
        "habitat": "woodland and open habitats",
        "behaviour": "forages actively and uses a range of vocal calls",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟡 Near Threatened (NT)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Grey-Headed Fish Eagle is best separated from Lesser Fish Eagle by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Lesser Fish Eagle, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Pallas's Fish Eagle can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — Birds of the World / eBird",
        "IUCN Red List of Threatened Species",
        "Raptors of the World / regional raptor references"
    ]
},

{
    "name": "Griffon Vulture",
    "scientific": "Gyps fulvus",
    "description": "The Griffon Vulture is a huge Old World vulture with broad wings, a pale head and neck, and contrasting dark flight feathers. It is a specialist scavenger that searches for carcasses while soaring over mountains and open countryside. Large groups can gather rapidly when a carcass is discovered.",
    "image": "GriffonVulture1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "95-110 cm",
        "weight": "About 6-11 kg",
        "wingspan": "About 230-265 cm",
        "diet": "mainly carrion from medium and large mammals",
        "habitat": "mountains, cliffs, open country and dry landscapes",
        "behaviour": "soars for long periods and gathers at carcasses",
        "activity": "Diurnal",
        "nesting": "A large stick nest placed on cliffs, usually in colonies",
        "breeding_season": "December to July",
        "clutch_size": "Usually 1 egg",
        "call": "Generally quiet away from colonies; produces hisses and grunts around nesting sites",
        "lifespan": "Can live for more than 30 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Spain: Andalusia, Extremadura, Castilla y León, Castilla-La Mancha, Aragón and Catalonia; Portugal; France; Italy; Balkans; Turkey; Middle East and North Africa"
    },
    "similar_birds": "Griffon Vulture is best separated from Cinereous Vulture by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Cinereous Vulture, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Himalayan Vulture can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — Birds of the World / eBird",
        "IUCN Red List of Threatened Species",
        "Raptors of the World / regional raptor references"
    ]
},

{
    "name": "Himalayan Monal",
    "scientific": "Lophophorus impejanus",
    "description": "The Himalayan Monal is one of the most spectacular pheasants of the Himalayan region. Adult males have an extraordinary metallic mixture of green, blue, purple and copper plumage with a prominent crest, while females are mostly brown with pale markings. It generally forages on the ground by digging through soil and leaf litter.",
    "image": "HimalayanMonal1.jpg",
    "quick_facts": {
        "family": "Phasianidae",
        "size": "61-72 cm",
        "weight": "About 1.8-2.4 kg",
        "wingspan": "About 85-90 cm",
        "diet": "roots, tubers, seeds, berries and invertebrates",
        "habitat": "mountain forest, rhododendron woodland and alpine slopes",
        "behaviour": "forages mostly on the ground and moves into higher elevations in summer",
        "activity": "Diurnal",
        "nesting": "A simple ground nest concealed among vegetation",
        "breeding_season": "April to August",
        "clutch_size": "Usually 4-6 eggs",
        "call": "Loud whistles and harsh alarm calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "India: Jammu and Kashmir, Himachal Pradesh, Uttarakhand, Sikkim and Arunachal Pradesh; Nepal; Bhutan; northern Myanmar; Pakistan"
    },
    "similar_birds": "Himalayan Monal is best separated from Kalij Pheasant by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Kalij Pheasant, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Satyr Tragopan can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "House Crow",
    "scientific": "Corvus splendens",
    "description": "Recognising the House Crow starts with a slender grey-and-black crow with a grey neck and chest contrasting with darker wings. The species uses cities, villages, farmland, ports and coastal settlements and takes food scraps, insects, fruit, seeds, carrion and many other foods as its principal food. It highly adaptable and often forages around people. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "HouseCrow1.jpg",
    "quick_facts": {
        "family": "Corvidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "food scraps, insects, fruit, seeds, carrion and many other foods",
        "habitat": "cities, villages, farmland, ports and coastal settlements",
        "behaviour": "highly adaptable and often forages around people",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "House Crow is best separated from Large-billed Crow by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Large-billed Crow, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Jungle Crow can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "House Sparrow",
    "scientific": "Passer domesticus",
    "description": "Recognising the House Sparrow starts with a small familiar sparrow with a stout bill, brown back and pale underparts. The species uses towns, villages, farms, gardens and buildings and takes seeds, grains, scraps and insects as its principal food. It usually lives in social groups around human settlements. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "HouseSparrow1.jpg",
    "quick_facts": {
        "family": "Passeridae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "seeds, grains, scraps and insects",
        "habitat": "towns, villages, farms, gardens and buildings",
        "behaviour": "usually lives in social groups around human settlements",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "House Sparrow is best separated from Italian Sparrow by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Italian Sparrow, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Tree Sparrow can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Indian Bush Lark",
    "scientific": "Mirafra erythroptera",
    "description": "The Indian Bush Lark is a sandy-brown lark with streaked upperparts and a strong, melodious flight song. It is found in dry grassland, scrub, open woodland and cultivated areas, where it feeds mainly on seeds and insects. The species is often noticed because it forages on the ground and sings during display flights. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "IndianBushLark1.jpg",
    "quick_facts": {
        "family": "Alaudidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "seeds and insects",
        "habitat": "dry grassland, scrub, open woodland and cultivated areas",
        "behaviour": "forages on the ground and sings during display flights",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Indian Bush Lark is best separated from Jerdon's Bush Lark by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Jerdon's Bush Lark, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Rufous-tailed Lark can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Indian Cormorant",
    "scientific": "Microcarbo fuscicollis",
    "description": "The Indian Cormorant is a dark medium-sized cormorant with a long neck and hooked bill, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in rivers, lakes, reservoirs, wetlands and sheltered coastal waters and feeds mainly on fish and aquatic animals. It dives underwater and often rests with wings spread to dry. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "IndianCormorant1.jpg",
    "quick_facts": {
        "family": "Phalacrocoracidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fish and aquatic animals",
        "habitat": "rivers, lakes, reservoirs, wetlands and sheltered coastal waters",
        "behaviour": "dives underwater and often rests with wings spread to dry",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Indian Cormorant is best separated from Little Cormorant by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Little Cormorant, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Great Cormorant can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Indian Courser",
    "scientific": "Cursorius coromandelicus",
    "description": "The Indian Courser is a slender long-legged shorebird with sandy plumage and a dark eye stripe, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in dry open plains, sandy flats, scrub and riverbeds and feeds mainly on insects and other small invertebrates. It runs rapidly over open ground and pauses upright to scan for prey. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "IndianCourser1.jpg",
    "quick_facts": {
        "family": "Glareolidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects and other small invertebrates",
        "habitat": "dry open plains, sandy flats, scrub and riverbeds",
        "behaviour": "runs rapidly over open ground and pauses upright to scan for prey",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Indian Courser is best separated from Small Pratincole by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Small Pratincole, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Oriental Pratincole can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Indian Golden Oriole",
    "scientific": "Oriolus kundoo",
    "description": "The Indian Golden Oriole is a bright yellow oriole with black wings and a dark eye stripe. It is found in woodland, gardens, plantations and forest edges, where it feeds mainly on fruit, nectar and insects. The species is often noticed because it feeds high in trees and is often detected by its fluting calls. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "IndianGoldenOriole1.jpg",
    "quick_facts": {
        "family": "Oriolidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fruit, nectar and insects",
        "habitat": "woodland, gardens, plantations and forest edges",
        "behaviour": "feeds high in trees and is often detected by its fluting calls",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Indian Golden Oriole is best separated from Black-naped Oriole by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Black-naped Oriole, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Black-hooded Oriole can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Indian Grey Hornbill",
    "scientific": "Ocyceros birostris",
    "description": "Recognising the Indian Grey Hornbill starts with a medium-sized grey hornbill with a dark bill and long tail. The species uses dry woodland, farmland, gardens and urban tree cover and takes fruit, insects and small vertebrates as its principal food. It moves through trees in pairs and nests in tree cavities. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "IndianGreyHornbill1.jpg",
    "quick_facts": {
        "family": "Bucerotidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fruit, insects and small vertebrates",
        "habitat": "dry woodland, farmland, gardens and urban tree cover",
        "behaviour": "moves through trees in pairs and nests in tree cavities",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Indian Grey Hornbill is best separated from Malabar Pied Hornbill by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Malabar Pied Hornbill, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Indian Scimitar Babbler can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Indian Openbill",
    "scientific": "Anastomus oscitans",
    "description": "Recognising the Indian Openbill starts with a medium-sized stork with a distinctive gap between the upper and lower bill tips. The species uses wetlands, rice fields, marshes and flooded grassland and takes snails, aquatic invertebrates, fish and frogs as its principal food. It walks through shallow water and mud while probing for prey. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "IndianOpenbill1.jpg",
    "quick_facts": {
        "family": "Ciconiidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "snails, aquatic invertebrates, fish and frogs",
        "habitat": "wetlands, rice fields, marshes and flooded grassland",
        "behaviour": "walks through shallow water and mud while probing for prey",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Indian Openbill is best separated from Asian Woollyneck by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Asian Woollyneck, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Painted Stork can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Indian Paradise Flycatcher",
    "scientific": "Terpsiphone paradisi",
    "description": "The Indian Paradise Flycatcher is a graceful flycatcher with a crest and very long tail streamers in adult males, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in forest, woodland, gardens and shaded plantations and feeds mainly on flying insects and other small arthropods. It makes quick aerial sallies from perches and can appear very acrobatic. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "IndianParadiseFlycatcher1.jpg",
    "quick_facts": {
        "family": "Monarchidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "flying insects and other small arthropods",
        "habitat": "forest, woodland, gardens and shaded plantations",
        "behaviour": "makes quick aerial sallies from perches and can appear very acrobatic",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Indian Paradise Flycatcher is best separated from Black-naped Monarch by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Black-naped Monarch, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Asian Paradise Flycatcher can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Indian Peafowl",
    "scientific": "Pavo cristatus",
    "description": "The Indian Peafowl is a large pheasant whose male has an enormous iridescent train and blue-green neck, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in woodland edges, scrub, farmland and villages and feeds mainly on seeds, fruit, insects, reptiles and other small animals. It forages on the ground and males display their train during courtship. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "IndianPeafowl1.jpg",
    "quick_facts": {
        "family": "Phasianidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "seeds, fruit, insects, reptiles and other small animals",
        "habitat": "woodland edges, scrub, farmland and villages",
        "behaviour": "forages on the ground and males display their train during courtship",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Indian Peafowl is best separated from Green Peafowl by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Green Peafowl, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Golden Pheasant can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Indian Pied Starling",
    "scientific": "Gracupica contra",
    "description": "The Indian Pied Starling is a black-and-white starling with a pale bill and contrasting facial pattern. It is found in open woodland, farmland, towns and cultivated areas, where it feeds mainly on fruit, insects, seeds and scraps. The species is often noticed because it forages on the ground in pairs or small groups. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "IndianPiedStarling1.jpg",
    "quick_facts": {
        "family": "Sturnidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fruit, insects, seeds and scraps",
        "habitat": "open woodland, farmland, towns and cultivated areas",
        "behaviour": "forages on the ground in pairs or small groups",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Indian Pied Starling is best separated from Common Myna by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Common Myna, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Brahminy Starling can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Indian Pitta",
    "scientific": "Pitta brachyura",
    "description": "The Indian Pitta is a stocky, short-tailed forest bird with vivid green, blue, buff and red plumage, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in forest floor, woodland, plantations and dense undergrowth and feeds mainly on insects, worms and other small invertebrates. It hops through leaf litter and is often heard before being seen. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "IndianPitta1.jpg",
    "quick_facts": {
        "family": "Pittidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects, worms and other small invertebrates",
        "habitat": "forest floor, woodland, plantations and dense undergrowth",
        "behaviour": "hops through leaf litter and is often heard before being seen",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Indian Pitta is best separated from Hooded Pitta by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Hooded Pitta, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Blue-winged Pitta can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Indian Pond Heron",
    "scientific": "Ardeola grayii",
    "description": "Recognising the Indian Pond Heron starts with a small brown-and-white heron that looks heavily streaked on the ground but becomes strikingly white in flight. The species uses ponds, marshes, rice fields, canals and shallow wetlands and takes fish, frogs, insects and small aquatic animals as its principal food. It stands quietly at the edge of water before striking at prey. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "IndianPondHeron1.jpg",
    "quick_facts": {
        "family": "Ardeidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fish, frogs, insects and small aquatic animals",
        "habitat": "ponds, marshes, rice fields, canals and shallow wetlands",
        "behaviour": "stands quietly at the edge of water before striking at prey",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Indian Pond Heron is best separated from Chinese Pond Heron by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Chinese Pond Heron, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Cattle Egret can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Indian Robin",
    "scientific": "Copsychus fulicatus",
    "description": "Recognising the Indian Robin starts with a small dark robin with an upright tail and rusty undertail area, especially obvious in males. The species uses dry scrub, open woodland, gardens, rocky ground and villages and takes insects and other small invertebrates as its principal food. It forages on the ground and flicks its tail while moving between perches. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "IndianRobin1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects and other small invertebrates",
        "habitat": "dry scrub, open woodland, gardens, rocky ground and villages",
        "behaviour": "forages on the ground and flicks its tail while moving between perches",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Indian Robin is best separated from Brown Rock Chat by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Brown Rock Chat, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Pied Bushchat can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Indian Roller",
    "scientific": "Coracias benghalensis",
    "description": "The Indian Roller is a stocky roller with a brown back, blue wings and turquoise flight feathers. It is found in open woodland, farmland, grassland and roadside trees, where it feeds mainly on insects, reptiles, frogs and small animals. The species is often noticed because it hunts from exposed perches and performs dramatic rolling display flights. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "IndianRoller1.jpg",
    "quick_facts": {
        "family": "Coraciidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects, reptiles, frogs and small animals",
        "habitat": "open woodland, farmland, grassland and roadside trees",
        "behaviour": "hunts from exposed perches and performs dramatic rolling display flights",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Indian Roller is best separated from European Roller by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with European Roller, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. White-throated Kingfisher can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Indian Silverbill",
    "scientific": "Euodice malabarica",
    "description": "The Indian Silverbill is a tiny finch with a pale conical bill, brown back and whitish underparts, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in dry grassland, scrub, farmland and open woodland and feeds mainly on grass seeds and other small seeds. It travels in flocks and often feeds close to the ground. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "IndianSilverbill1.jpg",
    "quick_facts": {
        "family": "Estrildidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "grass seeds and other small seeds",
        "habitat": "dry grassland, scrub, farmland and open woodland",
        "behaviour": "travels in flocks and often feeds close to the ground",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Indian Silverbill is best separated from White-rumped Munia by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with White-rumped Munia, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Scaly-breasted Munia can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Indian Spot-billed Duck",
    "scientific": "Anas poecilorhyncha",
    "description": "The Indian Spot-billed Duck is a large brown duck with a yellow-tipped dark bill and pale facial markings, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in lakes, rivers, marshes, rice fields and ponds and feeds mainly on aquatic plants, seeds, grains and invertebrates. It swims and feeds in shallow water, often in pairs or groups. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "IndianSpot-BilledDuck1.jpg",
    "quick_facts": {
        "family": "Anatidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "aquatic plants, seeds, grains and invertebrates",
        "habitat": "lakes, rivers, marshes, rice fields and ponds",
        "behaviour": "swims and feeds in shallow water, often in pairs or groups",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Indian Spot-billed Duck is best separated from Pacific Black Duck by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Pacific Black Duck, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Gadwall can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Indian Thick-knee",
    "scientific": "Burhinus indicus",
    "description": "The Indian Thick-knee is a large ground-dwelling Indian bird with long legs, enormous yellow eyes, a strong bill and cryptic brown plumage. Despite its name, it is not a true plover. It relies heavily on camouflage and is most active during the evening, night and early morning.",
    "image": "IndianThick-Knee1.jpg",
    "quick_facts": {
        "family": "Burhinidae",
        "size": "41-44 cm",
        "weight": "About 450-700 g",
        "wingspan": "About 80-90 cm",
        "diet": "insects, small reptiles and other small animals",
        "habitat": "dry grassland, scrub, rocky plains and cultivated country",
        "behaviour": "walks slowly and freezes when disturbed, relying on camouflage",
        "activity": "Crepuscular and nocturnal",
        "nesting": "A simple scrape on bare ground",
        "breeding_season": "March to July",
        "clutch_size": "Usually 2 eggs",
        "call": "Loud repeated nocturnal calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "India: Rajasthan, Gujarat, Maharashtra, Madhya Pradesh, Uttar Pradesh, Bihar, Odisha, Telangana, Andhra Pradesh, Karnataka, Kerala and Tamil Nadu; Nepal; Sri Lanka"
    },
    "similar_birds": "Indian Thick-knee is best separated from Great Thick-knee by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Great Thick-knee, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Stone-curlew can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Italian Sparrow",
    "scientific": "Passer italiae",
    "description": "The Italian Sparrow is a distinctive sparrow of Italy and nearby Mediterranean regions. It has characteristics intermediate between the House Sparrow and Spanish Sparrow, making it an interesting example of closely related sparrows meeting and interbreeding. The male generally has a dark chestnut crown and black markings on the throat and chest, while the overall plumage combines features associated with both related species. It is strongly associated with human settlements but can also occur in farmland and open countryside. It usually nests in cavities and other sheltered spaces around buildings. Although it remains familiar in many Italian towns and villages, populations have declined in some areas, partly because modern buildings provide fewer suitable nesting sites and changing agricultural practices affect food availability.",
    "image": "ItalianSparrow1.jpg",
    "quick_facts": {
        "family": "Passeridae",
        "size": "About 14-16 cm",
        "weight": "About 25-30 g",
        "wingspan": "About 22-25 cm",
        "diet": "seeds, grains, insects and scraps",
        "habitat": "towns, villages, farmland, parks and gardens",
        "behaviour": "lives closely with people and commonly nests in buildings",
        "activity": "Diurnal",
        "nesting": "Uses cavities and sheltered recesses in buildings, walls, roof spaces, posts and occasionally tree cavities",
        "breeding_season": "Usually begins in March and may continue through several successive clutches",
        "clutch_size": "3-6 eggs",
        "call": "A series of chirps and chattering contact calls typical of sparrows",
        "lifespan": "Usually a few years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Italy: widespread, especially northern, central and southern Italy and Sicily; also parts of neighbouring Mediterranean regions including Malta and nearby islands"
    },
    "similar_birds": "Italian Sparrow is best separated from House Sparrow by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with House Sparrow, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Spanish Sparrow can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Jungle Babbler",
    "scientific": "Argya striata",
    "description": "The Jungle Babbler is a social grey-brown babbler with a pale eye and short rounded wings, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in woodland, scrub, gardens and cultivated areas and feeds mainly on insects, fruit, seeds and other small food. It moves in noisy family groups and forages together on the ground. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "JungleBabbler1.jpg",
    "quick_facts": {
        "family": "Leiothrichidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects, fruit, seeds and other small food",
        "habitat": "woodland, scrub, gardens and cultivated areas",
        "behaviour": "moves in noisy family groups and forages together on the ground",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Jungle Babbler is best separated from Common Babbler by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Common Babbler, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Large Grey Babbler can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Jungle Owlet",
    "scientific": "Glaucidium radiatum",
    "description": "The Jungle Owlet is a small barred brown-and-white owl with a rounded head and bright eyes, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in woodland, forest edges, plantations and wooded country and feeds mainly on insects, small reptiles, birds and rodents. It hunts from low perches and is mainly active around dawn, dusk and night. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "JungleOwlet1.jpg",
    "quick_facts": {
        "family": "Strigidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects, small reptiles, birds and rodents",
        "habitat": "woodland, forest edges, plantations and wooded country",
        "behaviour": "hunts from low perches and is mainly active around dawn, dusk and night",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Jungle Owlet is best separated from Spotted Owlet by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Spotted Owlet, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Brown Fish Owl can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Laughing Dove",
    "scientific": "Spilopelia senegalensis",
    "description": "The Laughing Dove is a small slender dove with a long tail and delicate barred-and-spotted neck pattern. It is found in dry woodland, scrub, farmland, gardens and towns, where it feeds mainly on seeds and grains. The species is often noticed because it forages mostly on the ground and often occurs in pairs. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "LaughingDove1.jpg",
    "quick_facts": {
        "family": "Columbidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "seeds and grains",
        "habitat": "dry woodland, scrub, farmland, gardens and towns",
        "behaviour": "forages mostly on the ground and often occurs in pairs",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Laughing Dove is best separated from Spotted Dove by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Spotted Dove, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Eurasian Collared Dove can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Laughing Kookaburra",
    "scientific": "Dacelo novaeguineae",
    "description": "The Laughing Kookaburra is one of Australia's most recognisable birds, famous for its loud call that sounds remarkably like human laughter. It is a large member of the kingfisher family, with a large pale bill, brown-and-white body, blue-green wings and a rufous tail. Despite belonging to the kingfisher family, it does not depend primarily on fish. Instead, it sits quietly on a perch and watches for prey before dropping down to seize it. Its diet can include insects, reptiles, amphibians, rodents and other small animals. Unlike many solitary kingfishers, Laughing Kookaburras live in family groups and may have older offspring helping the breeding pair raise young.",
    "image": "LaughingKookaburra1.jpg",
    "quick_facts": {
        "family": "Alcedinidae",
        "size": "About 40-47 cm",
        "weight": "About 300-350 g",
        "wingspan": "About 55-65 cm",
        "diet": "insects, reptiles, frogs, small mammals and birds",
        "habitat": "woodland, open forest, parks and gardens",
        "behaviour": "perches quietly before dropping onto prey and often lives in family groups",
        "activity": "Diurnal",
        "nesting": "A bare chamber in a natural tree hollow or occasionally an arboreal termite mound",
        "breeding_season": "August to January",
        "clutch_size": "Usually 2-3 eggs",
        "call": "The famous loud, rolling 'laughing' call, along with shorter calls used for communication",
        "lifespan": "Can live for many years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: Queensland, New South Wales, Victoria, South Australia and eastern Tasmania; introduced populations also occur in parts of Western Australia and Tasmania"
    },
    "similar_birds": "Laughing Kookaburra is best separated from Blue-winged Kookaburra by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Blue-winged Kookaburra, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Sacred Kingfisher can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Lesser Adjutant",
    "scientific": "Leptoptilos javanicus",
    "description": "Recognising the Lesser Adjutant starts with a very large stork with a bare head and neck, heavy bill and long legs. The species uses wetlands, grassland, mangroves and open woodland and takes fish, frogs, reptiles, insects and carrion as its principal food. It walks slowly through shallow water and open ground while searching for prey. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "LesserAdjutant1.jpg",
    "quick_facts": {
        "family": "Ciconiidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fish, frogs, reptiles, insects and carrion",
        "habitat": "wetlands, grassland, mangroves and open woodland",
        "behaviour": "walks slowly through shallow water and open ground while searching for prey",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟠 Vulnerable (VU)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Lesser Adjutant is best separated from Greater Adjutant by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Greater Adjutant, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Asian Woollyneck can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Lesser Whistling Duck",
    "scientific": "Dendrocygna javanica",
    "description": "Recognising the Lesser Whistling Duck starts with a small brown whistling duck with a rounded head and warm buff body. The species uses freshwater lakes, marshes, rice fields and ponds and takes aquatic vegetation, seeds and small invertebrates as its principal food. It often rests in large groups and feeds by dabbling. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "LesserWhistlingDuck1.jpg",
    "quick_facts": {
        "family": "Anatidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "aquatic vegetation, seeds and small invertebrates",
        "habitat": "freshwater lakes, marshes, rice fields and ponds",
        "behaviour": "often rests in large groups and feeds by dabbling",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Lesser Whistling Duck is best separated from Lesser Whistling Duck by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Lesser Whistling Duck, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Indian Spot-billed Duck can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Little Cormorant",
    "scientific": "Microcarbo niger",
    "description": "The Little Cormorant is a small dark cormorant with a short head and neck and a relatively compact bill, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in rivers, lakes, reservoirs, wetlands and coastal waters and feeds mainly on fish, crustaceans and aquatic animals. It dives underwater and frequently perches with wings spread to dry. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "LittleCormorant1.jpg",
    "quick_facts": {
        "family": "Phalacrocoracidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fish, crustaceans and aquatic animals",
        "habitat": "rivers, lakes, reservoirs, wetlands and coastal waters",
        "behaviour": "dives underwater and frequently perches with wings spread to dry",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Little Cormorant is best separated from Indian Cormorant by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Indian Cormorant, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Great Cormorant can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Little Egret",
    "scientific": "Egretta garzetta",
    "description": "Recognising the Little Egret starts with a slim white egret with black legs, a black bill and yellow feet. The species uses marshes, rivers, lagoons, rice fields and shallow coasts and takes fish, frogs, insects and crustaceans as its principal food. It walks through shallow water while stirring prey with its feet. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "LittleEgret1.jpg",
    "quick_facts": {
        "family": "Ardeidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fish, frogs, insects and crustaceans",
        "habitat": "marshes, rivers, lagoons, rice fields and shallow coasts",
        "behaviour": "walks through shallow water while stirring prey with its feet",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Little Egret is best separated from Cattle Egret by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Cattle Egret, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Great Egret can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Little Grebe",
    "scientific": "Tachybaptus ruficollis",
    "description": "Recognising the Little Grebe starts with a tiny dark waterbird with a rounded body and short bill, often showing a rich chestnut face in breeding plumage. The species uses ponds, marshes, slow rivers and vegetated lakes and takes small fish, aquatic insects and crustaceans as its principal food. It dives quickly and can disappear beneath vegetation when alarmed. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "LittleGrebe1.jpg",
    "quick_facts": {
        "family": "Podicipedidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "small fish, aquatic insects and crustaceans",
        "habitat": "ponds, marshes, slow rivers and vegetated lakes",
        "behaviour": "dives quickly and can disappear beneath vegetation when alarmed",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Little Grebe is best separated from Eurasian Coot by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Eurasian Coot, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Australasian Grebe can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Little Ringed Plover",
    "scientific": "Charadrius dubius",
    "description": "Recognising the Little Ringed Plover starts with a small sandy plover with a complete black breast band and yellow eye-ring in adults. The species uses mudflats, riverbeds, gravel pits, reservoirs and bare wet ground and takes insects, worms and other small invertebrates as its principal food. It runs in short bursts and stops abruptly while feeding. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "LittleRingedPlover1.jpg",
    "quick_facts": {
        "family": "Charadriidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects, worms and other small invertebrates",
        "habitat": "mudflats, riverbeds, gravel pits, reservoirs and bare wet ground",
        "behaviour": "runs in short bursts and stops abruptly while feeding",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Little Ringed Plover is best separated from Kentish Plover by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Kentish Plover, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Common Ringed Plover can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Long-Tailed Shrike",
    "scientific": "Lanius schach",
    "description": "The Long-Tailed Shrike is a grey-and-brown shrike with a black facial mask and long tail. It is found in open woodland, scrub, farmland and grassland, where it feeds mainly on large insects, lizards, small birds and rodents. The species is often noticed because it hunts from exposed perches and may impale prey on thorns. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "Long-TailedShrike1.jpg",
    "quick_facts": {
        "family": "Laniidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "large insects, lizards, small birds and rodents",
        "habitat": "open woodland, scrub, farmland and grassland",
        "behaviour": "hunts from exposed perches and may impale prey on thorns",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Long-Tailed Shrike is best separated from Bay-backed Shrike by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Bay-backed Shrike, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Brown Shrike can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Magpie-lark",
    "scientific": "Grallina cyanoleuca",
    "description": "The Magpie-lark is a familiar black-and-white Australian bird that is often seen around wetlands, gardens, farmland and open woodland. Males and females both have bold black-and-white plumage, although their facial patterns differ. The species spends much of its time on the ground searching for insects and other small invertebrates, often walking across lawns and muddy ground. Magpie-larks are territorial and can be particularly vocal, producing a series of clear calls that are sometimes described as a conversational exchange between pairs. They build distinctive mud nests in trees, often close to water.",
    "image": "Magpie-Lark1.jpg",
    "quick_facts": {
        "family": "Grallinidae",
        "size": "26-30 cm",
        "weight": "About 90-100 g",
        "wingspan": "About 40-45 cm",
        "diet": "insects, worms and other small invertebrates",
        "habitat": "open woodland, wetlands, parks, farmland and suburbs",
        "behaviour": "forages on the ground and often works in pairs",
        "activity": "Diurnal",
        "nesting": "A distinctive bowl-shaped mud nest built on a tree branch",
        "breeding_season": "Usually throughout much of the year, depending on conditions",
        "clutch_size": "Usually 3-5 eggs",
        "call": "Clear, ringing calls often given by both members of a pair",
        "lifespan": "Often several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: widespread across Queensland, New South Wales, Victoria, South Australia, Western Australia and the Northern Territory; also found in Tasmania"
    },
    "similar_birds": "Magpie-lark is best separated from Australian Magpie by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Australian Magpie, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Willie Wagtail can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Malabar Pied Hornbill",
    "scientific": "Anthracoceros coronatus",
    "description": "Recognising the Malabar Pied Hornbill starts with a medium-sized black-and-white hornbill with a large pale bill and casque. The species uses forest, woodland, plantations and large trees and takes fruit, insects and small vertebrates as its principal food. It feeds in the canopy and nests in tree cavities. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "MalabarPiedHornbill1.jpg",
    "quick_facts": {
        "family": "Bucerotidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fruit, insects and small vertebrates",
        "habitat": "forest, woodland, plantations and large trees",
        "behaviour": "feeds in the canopy and nests in tree cavities",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Malabar Pied Hornbill is best separated from Great Hornbill by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Great Hornbill, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Indian Grey Hornbill can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Malabar Whistling Thrush",
    "scientific": "Myophonus horsfieldii",
    "description": "The Malabar Whistling Thrush is a dark blue-black forest thrush of the Indian subcontinent, especially associated with the Western Ghats. It is famous for its beautiful flute-like song and is often heard before it is seen. It commonly forages around streams and shaded forest floors.",
    "image": "MalabarWhistlingThrush1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "25-29 cm",
        "weight": "About 110-160 g",
        "wingspan": "About 38-42 cm",
        "diet": "insects, snails, frogs and other small animals",
        "habitat": "shaded forest streams, wet valleys and dense woodland",
        "behaviour": "forages near streams and often sings from hidden perches",
        "activity": "Diurnal, especially active around dawn and dusk",
        "nesting": "A cup-shaped nest built in rock crevices, tree hollows, banks or other sheltered sites",
        "breeding_season": "March to August",
        "clutch_size": "Usually 2 eggs",
        "call": "Beautiful clear whistles and flute-like phrases",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "India: Maharashtra, Goa, Karnataka, Kerala and Tamil Nadu, especially the Western Ghats"
    },
    "similar_birds": "Malabar Whistling Thrush is best separated from Blue Whistling Thrush by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Blue Whistling Thrush, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Orange-headed Thrush can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Masked Lapwing",
    "scientific": "Vanellus miles",
    "description": "The Masked Lapwing is a large ground-dwelling wader with a conspicuous yellow facial mask, long legs and a distinctive spur on the wing. It is commonly seen in grasslands, wetlands, farmland, parks and even suburban areas. Unlike many waders that nest beside water, Masked Lapwings often lay their eggs in exposed open ground. Adults become extremely defensive around nests and chicks and may dive at perceived threats. They may also perform a broken-wing display, pretending to be injured to draw a predator away from the nest. Their loud calls and bold behaviour make them one of the most noticeable Australian waders.",
    "image": "MaskedLapwing1.jpg",
    "quick_facts": {
        "family": "Charadriidae",
        "size": "33-38 cm",
        "weight": "About 350-450 g",
        "wingspan": "About 70-85 cm",
        "diet": "insects, worms and other invertebrates",
        "habitat": "grassland, wetlands, farmland, parks and urban areas",
        "behaviour": "walks across open ground and aggressively defends its nest",
        "activity": "Diurnal, with some nocturnal activity",
        "nesting": "A shallow scrape on open ground, sometimes with little or no nest lining",
        "breeding_season": "Throughout much of the year, depending on rainfall and local conditions",
        "clutch_size": "Usually 3-4 eggs",
        "call": "Loud repeated calls, especially when alarmed or defending a nest",
        "lifespan": "Usually several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: widespread, including Tasmania and many offshore islands; also New Guinea and nearby islands"
    },
    "similar_birds": "Masked Lapwing is best separated from Red-wattled Lapwing by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Red-wattled Lapwing, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Northern Lapwing can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Noisy Miner",
    "scientific": "Manorina melanocephala",
    "description": "The Noisy Miner is a bold, highly social Australian honeyeater with a mostly grey body, black crown and cheeks, and a bright yellow bill and legs. Its name is extremely appropriate because colonies can produce a constant stream of loud calls. Noisy Miners are unusually aggressive toward other birds and may collectively mob much larger species such as hawks and kookaburras. They prefer open woodland and forests with relatively open understorey and have become common in parks, gardens and suburban areas. Despite the similar name, the Noisy Miner is completely unrelated to the introduced Common Myna, which belongs to the starling family.",
    "image": "NoisyMiner1.jpg",
    "quick_facts": {
        "family": "Meliphagidae",
        "size": "About 28 cm",
        "weight": "About 60-70 g",
        "wingspan": "About 35-40 cm",
        "diet": "nectar, fruit and insects",
        "habitat": "open woodland, parks, gardens and suburbs",
        "behaviour": "lives in noisy colonies and often mobs larger birds",
        "activity": "Diurnal",
        "nesting": "A small cup-shaped nest built from grass, bark and spider web in a tree or shrub",
        "breeding_season": "Usually August to January, with breeding influenced by local conditions",
        "clutch_size": "Usually 2-4 eggs",
        "call": "Loud, varied and repeated chattering calls",
        "lifespan": "Usually several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: mainly eastern and southeastern Australia, including Queensland, New South Wales, Victoria and South Australia"
    },
    "similar_birds": "Noisy Miner is best separated from Common Myna by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Common Myna, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Blue-faced Honeyeater can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Northern Cardinal",
    "scientific": "Cardinalis cardinalis",
    "description": "The Northern Cardinal is a familiar North American songbird with a prominent crest and strong red-orange bill. Adult males are brilliant red with a black face, while females are mostly warm brown with reddish highlights. Cardinals are common around woodland edges, gardens and suburban areas and are often seen feeding on seeds on or near the ground.",
    "image": "NorthernCardinal1.jpg",
    "quick_facts": {
        "family": "Cardinalidae",
        "size": "21-23 cm",
        "weight": "About 33-65 g",
        "wingspan": "About 25-31 cm",
        "diet": "seeds, fruit and insects",
        "habitat": "woodland edges, thickets, gardens, parks and suburbs",
        "behaviour": "often feeds on the ground and sings from conspicuous perches",
        "activity": "Diurnal",
        "nesting": "An open cup of twigs, bark, grass and plant fibres placed in dense shrubs or low trees",
        "breeding_season": "March to September",
        "clutch_size": "Usually 2-5 eggs",
        "call": "Clear whistles and sharp metallic chip calls",
        "lifespan": "Often lives 10 years or more in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Canada: southern provinces; United States: eastern, central and parts of southwestern states; Mexico: northern and eastern regions"
    },
    "similar_birds": "Northern Cardinal is best separated from Pyrrhuloxia by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Pyrrhuloxia, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Summer Tanager can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "Cornell Lab of Ornithology — All About Birds / eBird",
        "Audubon — North American bird identification and natural history",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Northern Hawk-Owl",
    "scientific": "Surnia ulula",
    "description": "The Northern Hawk-Owl is an unusual owl of the northern boreal forests that combines the appearance and behaviour of an owl with several characteristics more typical of hawks. It has a long tail, pointed wings and a relatively small facial disk, giving it a distinctly hawk-like silhouette. Unlike most owls, it is primarily active during the day and often hunts from the top of an exposed tree. It watches for small mammals and birds before making rapid, low flights to capture prey. The species breeds across northern North America and Eurasia and may move southward in some winters when food becomes scarce. Its daytime habits make it particularly distinctive among northern owls.",
    "image": "NorthernHawk-Owl1.jpg",
    "quick_facts": {
        "family": "Strigidae",
        "size": "36-43 cm",
        "weight": "About 300-350 g",
        "wingspan": "About 79-89 cm",
        "diet": "small mammals and birds",
        "habitat": "boreal forest, forest edges, clearings and open woodland",
        "behaviour": "hunts from exposed perches and makes fast low flights after prey",
        "activity": "Primarily diurnal",
        "nesting": "Uses tree cavities, dead tree stubs and abandoned woodpecker holes",
        "breeding_season": "March to June",
        "clutch_size": "Usually 3-13 eggs",
        "call": "Rapid whistles and sharp repeated calls; males give prolonged series during courtship",
        "lifespan": "About 10 years is a reported average",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Canada: most northern regions; United States: Alaska and occasionally northern states; Europe: Scandinavia and northern Russia; Asia: Siberia and adjacent northern regions"
    },
    "similar_birds": "Northern Hawk-Owl is best separated from Short-eared Owl by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Short-eared Owl, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Northern Pygmy-Owl can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — Birds of the World / eBird",
        "IUCN Red List of Threatened Species",
        "Raptors of the World / regional raptor references"
    ]
},

{
    "name": "Northern Lapwing",
    "scientific": "Vanellus vanellus",
    "description": "The Northern Lapwing is a distinctive plover with glossy dark green-black upperparts, white underparts, broad rounded wings, and a long, thin crest. Its striking appearance is especially noticeable during the breeding season, when males perform spectacular tumbling display flights. It breeds mainly in open grassland, farmland, moorland, and other open habitats, while outside the breeding season it may gather in large flocks on wetlands, mudflats, coastal fields, and agricultural land. It feeds mainly on earthworms, insects, larvae, and other small invertebrates.",
    "image": "NorthernLapwing1.jpg",
    "quick_facts": {
        "family": "Charadriidae",
        "size": "28–31 cm",
        "weight": "Approximately 250 g",
        "wingspan": "67–72 cm",
        "diet": "seeds, insects, fruit and other suitable foods",
        "habitat": "woodland and open habitats",
        "behaviour": "forages actively and uses a range of vocal calls",
        "activity": "Diurnal",
        "nesting": "Shallow scrape on the ground, usually placed in short vegetation",
        "breeding_season": "Generally March to July",
        "clutch_size": "Usually 4 eggs",
        "call": "Distinctive nasal 'pee-wit' calls, particularly during display flights",
        "lifespan": "Several years; individuals may survive considerably longer under favourable conditions",
        "conservation_status": "🟡 Near Threatened (NT)",
        "where_to_find": "United Kingdom: England, Scotland, Wales, and Northern Ireland; Ireland; France: Normandy, Brittany, Hauts-de-France, and other regions; Germany: Lower Saxony, Bavaria, Brandenburg, and other open regions; Netherlands: Friesland, Groningen, and other provinces; Poland: Masovia, Greater Poland, and other regions; Sweden: Götaland and Svealand; Spain: Castilla y León, Aragón, and other suitable regions; also widespread across much of central and northern Europe and parts of western Asia."
    },
    "similar_birds": "Northern Lapwing is best separated from Red-wattled Lapwing by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Red-wattled Lapwing, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Little Ringed Plover can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "British Trust for Ornithology — European bird ecology and monitoring",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Orange-headed Thrush",
    "scientific": "Geokichla citrina",
    "description": "The Orange-headed Thrush is a colourful forest thrush with a bright orange head and underparts contrasting with darker wings and back. It is generally secretive and spends much of its time foraging among leaf litter on the forest floor for insects and other small prey.",
    "image": "Orange-HeadedThrush1.jpg",
    "quick_facts": {
        "family": "Turdidae",
        "size": "20-23 cm",
        "weight": "About 45-60 g",
        "wingspan": "About 33-38 cm",
        "diet": "insects, worms, fruit and other small food",
        "habitat": "forest, shaded woodland, plantations and dense undergrowth",
        "behaviour": "forages quietly on the forest floor among leaf litter",
        "activity": "Diurnal, especially active around dawn and dusk",
        "nesting": "A cup-shaped nest placed in a tree, shrub or other sheltered vegetation",
        "breeding_season": "Varies by region, generally during warmer or wetter months",
        "clutch_size": "Usually 2-3 eggs",
        "call": "Musical whistles and soft notes",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "India: Himalayan foothills, northeastern states and parts of central and southern India; Sri Lanka; Bangladesh; Bhutan; Nepal"
    },
    "similar_birds": "Orange-headed Thrush is best separated from Malabar Whistling Thrush by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Malabar Whistling Thrush, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Orange-headed Ground Thrush can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Oriental Darter",
    "scientific": "Anhinga melanogaster",
    "description": "Recognising the Oriental Darter starts with a long-necked waterbird with a narrow body and pointed bill, often appearing snake-like in water. The species uses freshwater lakes, rivers, marshes and sheltered wetlands and takes fish and other aquatic animals as its principal food. It dives underwater and often dries its wings while perched. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "OrientalDarter1.jpg",
    "quick_facts": {
        "family": "Anhingidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fish and other aquatic animals",
        "habitat": "freshwater lakes, rivers, marshes and sheltered wetlands",
        "behaviour": "dives underwater and often dries its wings while perched",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Oriental Darter is best separated from Australian Darter by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Australian Darter, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Little Cormorant can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Oriental Magpie-Robin",
    "scientific": "Copsychus saularis",
    "description": "The Oriental Magpie-Robin is a black-and-white songbird with a long tail and upright posture, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in gardens, woodland, forest edges and human settlements and feeds mainly on insects and other small invertebrates. It forages on the ground and sings strongly from exposed perches. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "OrientalMagpie-Robin1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects and other small invertebrates",
        "habitat": "gardens, woodland, forest edges and human settlements",
        "behaviour": "forages on the ground and sings strongly from exposed perches",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Oriental Magpie-Robin is best separated from White-rumped Shama by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with White-rumped Shama, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Indian Robin can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Oriental Skylark",
    "scientific": "Alauda gulgula",
    "description": "The Oriental Skylark is a small brown streaked lark with a strong flight song. It is found in grassland, farmland, open scrub and cultivated plains, where it feeds mainly on seeds and insects. The species is often noticed because it feeds on the ground and rises to sing during display. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "OrientalSkylark1.jpg",
    "quick_facts": {
        "family": "Alaudidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "seeds and insects",
        "habitat": "grassland, farmland, open scrub and cultivated plains",
        "behaviour": "feeds on the ground and rises to sing during display",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Oriental Skylark is best separated from Bengal Bush Lark by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Bengal Bush Lark, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Indian Bush Lark can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Oriental Turtle Dove",
    "scientific": "Streptopelia orientalis",
    "description": "The Oriental Turtle Dove is a medium-sized dove with a black-and-white neck patch and long pointed tail. It is found in woodland, farmland, gardens and forest edges, where it feeds mainly on seeds and grains. The species is often noticed because it usually forages on the ground and may occur in small groups. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "OrientalTurtleDove1.jpg",
    "quick_facts": {
        "family": "Columbidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "seeds and grains",
        "habitat": "woodland, farmland, gardens and forest edges",
        "behaviour": "usually forages on the ground and may occur in small groups",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Oriental Turtle Dove is best separated from Spotted Dove by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Spotted Dove, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Laughing Dove can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Oriental White-Eye",
    "scientific": "Zosterops palpebrosus",
    "description": "The Oriental White-Eye is a tiny greenish bird with a conspicuous white eye-ring, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in woodland, gardens, plantations and forest edges and feeds mainly on nectar, fruit and insects. It moves actively through foliage in small groups. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "OrientalWhite-Eye1.jpg",
    "quick_facts": {
        "family": "Zosteropidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "nectar, fruit and insects",
        "habitat": "woodland, gardens, plantations and forest edges",
        "behaviour": "moves actively through foliage in small groups",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Oriental White-Eye is best separated from Indian White-eye by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Indian White-eye, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Oriental Leafbird can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Pacific Black Duck",
    "scientific": "Anas superciliosa",
    "description": "The Pacific Black Duck is one of Australia's most widespread and adaptable ducks. It can live in an impressive variety of aquatic habitats, from forest pools and rivers to lakes, swamps, tidal mudflats and coastal wetlands. Its dark plumage and distinctive facial markings help separate it from many other Australian ducks. It feeds mainly by dabbling, tipping its body forward so that its head and neck reach underwater while its tail points upward. Plant material forms much of its diet, although aquatic insects, molluscs and crustaceans are also eaten. It is closely related to the Mallard and the two species can interbreed where introduced Mallards occur.",
    "image": "PacificBlackDuck1.jpg",
    "quick_facts": {
        "family": "Anatidae",
        "size": "50-60 cm",
        "weight": "About 900-1100 g",
        "wingspan": "About 80-90 cm",
        "diet": "aquatic plants, seeds and invertebrates",
        "habitat": "wetlands, rivers, lakes, estuaries and coastal lagoons",
        "behaviour": "feeds by dabbling and grazing and often forms mixed flocks",
        "activity": "Diurnal",
        "nesting": "Usually nests in dense vegetation near water, sometimes using tree hollows or old nests",
        "breeding_season": "Varies with rainfall and local conditions",
        "clutch_size": "Usually 8-12 eggs",
        "call": "Females produce loud quacking calls while males have quieter whistles and calls",
        "lifespan": "Usually several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: widespread throughout the continent except the most arid regions; also Tasmania and nearby islands"
    },
    "similar_birds": "Pacific Black Duck is best separated from Australian Wood Duck by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Australian Wood Duck, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Indian Spot-billed Duck can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Painted Stork",
    "scientific": "Mycteria leucocephala",
    "description": "The Painted Stork is a large stork with a long yellow bill, pink wing coverts and black-and-white body pattern. It is found in marshes, lakes, floodplains, rice fields and shallow wetlands, where it feeds mainly on fish, frogs, insects and other aquatic animals. The species is often noticed because it wades slowly while sweeping its partly open bill through water. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "PaintedStork1.jpg",
    "quick_facts": {
        "family": "Ciconiidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fish, frogs, insects and other aquatic animals",
        "habitat": "marshes, lakes, floodplains, rice fields and shallow wetlands",
        "behaviour": "wades slowly while sweeping its partly open bill through water",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Painted Stork is best separated from Asian Openbill by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Asian Openbill, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Woolly-necked Stork can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Pied Bushchat",
    "scientific": "Saxicola caprata",
    "description": "The Pied Bushchat is a small black-and-white chat with a short tail and upright posture. It is found in grassland, farmland, scrub, villages and open woodland, where it feeds mainly on insects and other small invertebrates. The species is often noticed because it perches on fences and shrubs before dropping to the ground. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "PiedBushchat1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects and other small invertebrates",
        "habitat": "grassland, farmland, scrub, villages and open woodland",
        "behaviour": "perches on fences and shrubs before dropping to the ground",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Pied Bushchat is best separated from Common Stonechat by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Common Stonechat, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Indian Robin can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Pied Cuckoo",
    "scientific": "Clamator jacobinus",
    "description": "The Pied Cuckoo is a black-and-white cuckoo with a long tail and strong curved bill, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in open woodland, farmland, scrub and grassland and feeds mainly on insects, especially caterpillars, and other small animals. It is often conspicuous on exposed perches and is a brood parasite. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "PiedCuckoo1.jpg",
    "quick_facts": {
        "family": "Cuculidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects, especially caterpillars, and other small animals",
        "habitat": "open woodland, farmland, scrub and grassland",
        "behaviour": "is often conspicuous on exposed perches and is a brood parasite",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Pied Cuckoo is best separated from Common Hawk-Cuckoo by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Common Hawk-Cuckoo, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Asian Koel can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Pied Currawong",
    "scientific": "Strepera graculina",
    "description": "The Pied Currawong is a large mostly black Australian songbird with a bright yellow eye and small white patches on the wings and tail. It is common across eastern Australia and has adapted particularly well to suburban environments. Pied Currawongs are intelligent and opportunistic feeders that eat fruit, insects and small animals, and they may also take eggs or young birds. Their loud ringing calls can carry over long distances and are one of the characteristic sounds of Australian woodland and suburbia. It can be confused with other currawongs or the Australian Magpie, but its yellow eye, larger bill and white wing and tail markings help distinguish it.",
    "image": "PiedCurrawong1.jpg",
    "quick_facts": {
        "family": "Artamidae",
        "size": "44-51 cm",
        "weight": "About 250-350 g",
        "wingspan": "About 60-75 cm",
        "diet": "fruit, insects, small animals, eggs and young birds",
        "habitat": "forest, woodland, coastal scrub, parks and suburbs",
        "behaviour": "moves through trees and often gives loud ringing calls",
        "activity": "Diurnal",
        "nesting": "A bulky stick nest lined with grass and other soft material, usually placed in a tree",
        "breeding_season": "August to January",
        "clutch_size": "Usually 2-4 eggs",
        "call": "Loud, ringing and far-carrying whistles and calls",
        "lifespan": "Can live for more than 10 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: eastern Australia from northern Queensland to Victoria; absent from Tasmania"
    },
    "similar_birds": "Pied Currawong is best separated from Australian Magpie by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Australian Magpie, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Australian Raven can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Pied Kingfisher",
    "scientific": "Ceryle rudis",
    "description": "The Pied Kingfisher is a black-and-white kingfisher with a large crest and long bill, often hovering over water. It is found in rivers, lakes, reservoirs, estuaries and coasts, where it feeds mainly on fish and aquatic animals. The species is often noticed because it hovers over water before diving steeply. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "PiedKingfisher1.jpg",
    "quick_facts": {
        "family": "Alcedinidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fish and aquatic animals",
        "habitat": "rivers, lakes, reservoirs, estuaries and coasts",
        "behaviour": "hovers over water before diving steeply",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Pied Kingfisher is best separated from White-throated Kingfisher by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with White-throated Kingfisher, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Common Kingfisher can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Pied Oystercatcher",
    "scientific": "Haematopus longirostris",
    "description": "The Pied Oystercatcher is a large Australian shorebird with black upperparts, white underparts, a long orange-red bill and pinkish-red legs. It forages along sandy and muddy shores, using its powerful bill to open shellfish and probe for other invertebrates.",
    "image": "PiedOystercatcher1.jpg",
    "quick_facts": {
        "family": "Haematopodidae",
        "size": "About 50 cm",
        "weight": "About 500-800 g",
        "wingspan": "About 80-90 cm",
        "diet": "shellfish and other intertidal invertebrates",
        "habitat": "sandy beaches, mudflats, estuaries and rocky coasts",
        "behaviour": "walks along the shore and pries or hammers open prey",
        "activity": "Diurnal, with some feeding at night depending on tides",
        "nesting": "A simple scrape on sand, shell or gravel above the high-tide line",
        "breeding_season": "Winter to spring",
        "clutch_size": "Usually 2-3 eggs",
        "call": "Loud piping and whistling calls",
        "lifespan": "Can live for more than 20 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: Queensland, New South Wales, Victoria, Tasmania, South Australia, Western Australia and Northern Territory"
    },
    "similar_birds": "Pied Oystercatcher is best separated from Sooty Oystercatcher by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Sooty Oystercatcher, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Black Oystercatcher can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Plain Prinia",
    "scientific": "Prinia inornata",
    "description": "The Plain Prinia is a small brownish prinia with a long upright tail and plain overall plumage. It is found in grassland, farmland, scrub, wetlands and gardens, where it feeds mainly on insects and other small arthropods. The species is often noticed because it keeps low in vegetation and frequently flicks its tail. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "PlainPrinia1.jpg",
    "quick_facts": {
        "family": "Cisticolidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects and other small arthropods",
        "habitat": "grassland, farmland, scrub, wetlands and gardens",
        "behaviour": "keeps low in vegetation and frequently flicks its tail",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Plain Prinia is best separated from Ashy Prinia by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Ashy Prinia, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Grey-breasted Prinia can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Puff-Throated Babbler",
    "scientific": "Pellorneum ruficeps",
    "description": "The Puff-Throated Babbler is a brown forest babbler with a pale throat and strong legs for ground foraging, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in forest, woodland and dense undergrowth and feeds mainly on insects, worms and other small invertebrates. It forages in groups through leaf litter and low vegetation. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "Puff-ThroatedBabbler1.jpg",
    "quick_facts": {
        "family": "Pellorneidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects, worms and other small invertebrates",
        "habitat": "forest, woodland and dense undergrowth",
        "behaviour": "forages in groups through leaf litter and low vegetation",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Puff-Throated Babbler is best separated from Jungle Babbler by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Jungle Babbler, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Puff-throated Babbler can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Purple Heron",
    "scientific": "Ardea purpurea",
    "description": "Recognising the Purple Heron starts with a tall dark heron with a long neck, narrow body and rich chestnut and grey plumage. The species uses reedbeds, marshes, rivers, lakes and shallow wetlands and takes fish, frogs, insects and small vertebrates as its principal food. It hunts slowly among reeds and shallow water. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "PurpleHeron1.jpg",
    "quick_facts": {
        "family": "Ardeidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fish, frogs, insects and small vertebrates",
        "habitat": "reedbeds, marshes, rivers, lakes and shallow wetlands",
        "behaviour": "hunts slowly among reeds and shallow water",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Purple Heron is best separated from Grey Heron by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Grey Heron, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Great Egret can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Purple Sunbird",
    "scientific": "Cinnyris asiaticus",
    "description": "Recognising the Purple Sunbird starts with a tiny nectar-feeding bird whose male becomes glossy dark purple-blue in breeding plumage. The species uses gardens, scrub, woodland, plantations and urban areas and takes nectar and small insects as its principal food. It moves rapidly among flowers and often feeds while hovering. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "PurpleSunbird1.jpg",
    "quick_facts": {
        "family": "Nectariniidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "nectar and small insects",
        "habitat": "gardens, scrub, woodland, plantations and urban areas",
        "behaviour": "moves rapidly among flowers and often feeds while hovering",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Purple Sunbird is best separated from Crimson Sunbird by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Crimson Sunbird, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Purple-rumped Sunbird can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Purple-Rumped Sunbird",
    "scientific": "Leptocoma zeylonica",
    "description": "Recognising the Purple-Rumped Sunbird starts with a small sunbird with a slender curved bill and a colourful purple rump in males. The species uses forest, gardens, plantations and flowering woodland and takes nectar, insects and spiders as its principal food. It moves actively between flowers and foliage. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "Purple-RumpedSunbird1.jpg",
    "quick_facts": {
        "family": "Nectariniidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "nectar, insects and spiders",
        "habitat": "forest, gardens, plantations and flowering woodland",
        "behaviour": "moves actively between flowers and foliage",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Purple-Rumped Sunbird is best separated from Purple Sunbird by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Purple Sunbird, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Crimson Sunbird can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Rainbow Lorikeet",
    "scientific": "Trichoglossus moluccanus",
    "description": "The Rainbow Lorikeet is a brilliantly coloured parrot with a blue head, orange-red breast, green wings and back, and a bright red bill. Its colourful plumage makes it one of the easiest Australian parrots to recognise. Rainbow Lorikeets usually travel in noisy, fast-moving flocks and gather in large communal roosts. Unlike parrots that depend heavily on seeds, they are specialised feeders on nectar and pollen, using their brush-tipped tongues to collect food from flowers. They also eat fruit, seeds and some insects. They are well adapted to urban environments and are frequently seen in gardens and tree-lined suburbs. Their vivid colours and noisy flocking behaviour make them particularly conspicuous.",
    "image": "RainbowLorikeet1.jpg",
    "quick_facts": {
        "family": "Psittaculidae",
        "size": "25-30 cm",
        "weight": "About 100-150 g",
        "wingspan": "About 40-45 cm",
        "diet": "nectar, pollen, fruit, seeds and some insects",
        "habitat": "rainforest, woodland, coastal areas and well-treed urban habitats",
        "behaviour": "is highly social and often feeds in noisy flocks",
        "activity": "Diurnal",
        "nesting": "Uses hollows in trees, usually laying eggs on decayed wood inside the cavity",
        "breeding_season": "June to January",
        "clutch_size": "Usually 2 eggs",
        "call": "Loud screeches, chattering and rapid flock calls",
        "lifespan": "Often around 15-20 years in suitable conditions",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: Queensland, New South Wales, Victoria, northern New South Wales and northeastern Australia; introduced population around Perth, Western Australia"
    },
    "similar_birds": "Rainbow Lorikeet is best separated from Scaly-breasted Lorikeet by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Scaly-breasted Lorikeet, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Musk Lorikeet can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Red Wattlebird",
    "scientific": "Anthochaera carunculata",
    "description": "The Red Wattlebird is a large Australian honeyeater with grey-brown plumage, a yellow belly, red facial wattles and a long tail. It is an active nectar feeder and can become very noisy and territorial around flowering trees. It also eats insects and fruit.",
    "image": "RedWattlebird1.jpg",
    "quick_facts": {
        "family": "Meliphagidae",
        "size": "33-37 cm",
        "weight": "About 110-150 g",
        "wingspan": "About 45-50 cm",
        "diet": "nectar, fruit and insects",
        "habitat": "woodland, forest edges, gardens, parks and coastal scrub",
        "behaviour": "forages actively in flowering trees and can be aggressive around food",
        "activity": "Diurnal",
        "nesting": "A cup-shaped nest made from twigs, grass and other vegetation, usually placed in a tree or shrub",
        "breeding_season": "July to December",
        "clutch_size": "Usually 2-3 eggs",
        "call": "Loud harsh and nasal calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: Queensland, New South Wales, Victoria, South Australia, Western Australia and Tasmania"
    },
    "similar_birds": "Red Wattlebird is best separated from Little Wattlebird by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Little Wattlebird, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Yellow Wattlebird can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Red-browed Finch",
    "scientific": "Neochmia temporalis",
    "description": "The Red-browed Finch is a small and colourful Australian finch with a bright red eyebrow, red bill and red rump contrasting with olive-green and grey plumage. It is commonly found in grassy areas near woodland, forest edges, wetlands, farmland and gardens in eastern and southeastern Australia. Red-browed Finches are social birds and usually occur in pairs or small groups, often feeding together on the ground. They eat mainly seeds and may also take insects and other small food items. Their attractive plumage and active behaviour make them a familiar finch in suitable habitats.",
    "image": "Red-BrowedFinch1.jpg",
    "quick_facts": {
        "family": "Estrildidae",
        "size": "11-12 cm",
        "weight": "About 10-15 g",
        "wingspan": "About 15-17 cm",
        "diet": "grass seeds, other seeds and small insects",
        "habitat": "grassland, woodland edges, forest, wetlands, farmland and gardens",
        "behaviour": "is social and usually feeds in pairs or small flocks",
        "activity": "Diurnal",
        "nesting": "A domed grass nest with a side entrance, usually placed in dense vegetation",
        "breeding_season": "Usually spring and summer",
        "clutch_size": "Usually 4-6 eggs",
        "call": "High-pitched twittering and soft contact calls",
        "lifespan": "Often several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: eastern Queensland, New South Wales, Victoria and southeastern South Australia; also Tasmania"
    },
    "similar_birds": "Red-browed Finch is best separated from Double-barred Finch by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Double-barred Finch, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Chestnut-breasted Mannikin can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Red-legged Partridge",
    "scientific": "Alectoris rufa",
    "description": "The Red-legged Partridge is a compact European gamebird with a grey back, barred flanks, a white throat bordered by black markings, red legs and a red bill. It is strongly associated with dry farmland, scrub, vineyards and open Mediterranean countryside. It usually walks or runs rather than flies unless disturbed.",
    "image": "Red-LeggedPartridge1.jpg",
    "quick_facts": {
        "family": "Phasianidae",
        "size": "32-35 cm",
        "weight": "About 350-550 g",
        "wingspan": "About 47-50 cm",
        "diet": "seeds, grains, shoots and insects",
        "habitat": "farmland, scrub, grassland and open woodland",
        "behaviour": "forages on the ground in coveys and runs quickly when disturbed",
        "activity": "Diurnal",
        "nesting": "A shallow ground scrape lined with grass and plant material",
        "breeding_season": "April to June",
        "clutch_size": "Usually 10-16 eggs",
        "call": "Loud repeated 'chuk-chuk' and other harsh calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Spain: most regions; Portugal; southwestern France; introduced populations in parts of the United Kingdom and elsewhere"
    },
    "similar_birds": "Red-legged Partridge is best separated from Chukar by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Chukar, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Grey Partridge can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "British Trust for Ornithology — European bird ecology and monitoring",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Red-Naped Ibis",
    "scientific": "Pseudibis papillosa",
    "description": "The Red-Naped Ibis is a dark ibis with a bare red patch on the back of the neck and a long down-curved bill. It is found in dry grassland, scrub, farmland and open country, where it feeds mainly on insects, small vertebrates and other ground prey. The species is often noticed because it walks steadily over dry ground while probing for food. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "Red-NapedIbis1.jpg",
    "quick_facts": {
        "family": "Threskiornithidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects, small vertebrates and other ground prey",
        "habitat": "dry grassland, scrub, farmland and open country",
        "behaviour": "walks steadily over dry ground while probing for food",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Red-Naped Ibis is best separated from Black-headed Ibis by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Black-headed Ibis, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Black-faced Ibis can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Red-Vented Bulbul",
    "scientific": "Pycnonotus cafer",
    "description": "The Red-Vented Bulbul is a dark-crested bulbul with a brown body, black head and red vent, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in gardens, scrub, woodland, farmland and towns and feeds mainly on fruit, nectar, seeds and insects. It moves actively through shrubs and often calls from exposed perches. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "Red-VentedBulbul1.jpg",
    "quick_facts": {
        "family": "Pycnonotidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fruit, nectar, seeds and insects",
        "habitat": "gardens, scrub, woodland, farmland and towns",
        "behaviour": "moves actively through shrubs and often calls from exposed perches",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Red-Vented Bulbul is best separated from Red-whiskered Bulbul by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Red-whiskered Bulbul, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. White-browed Bulbul can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Red-Wattled Lapwing",
    "scientific": "Vanellus indicus",
    "description": "The Red-Wattled Lapwing is a large lapwing with a red bill, yellow facial wattles and bold black-and-white plumage, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in grassland, farmland, wetlands, riverbeds and urban open spaces and feeds mainly on insects, worms, seeds and other small food. It walks across open ground and gives loud alarm calls when disturbed. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "Red-WattledLapwing1.jpg",
    "quick_facts": {
        "family": "Charadriidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects, worms, seeds and other small food",
        "habitat": "grassland, farmland, wetlands, riverbeds and urban open spaces",
        "behaviour": "walks across open ground and gives loud alarm calls when disturbed",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Red-Wattled Lapwing is best separated from Masked Lapwing by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Masked Lapwing, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Northern Lapwing can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Red-Whiskered Bulbul",
    "scientific": "Pycnonotus jocosus",
    "description": "The Red-Whiskered Bulbul is a crested bulbul with a white face, black crest, red cheek patch and red vent. It is found in woodland, scrub, gardens, plantations and towns, where it feeds mainly on fruit, nectar and insects. The species is often noticed because it moves actively through vegetation in pairs or small groups. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "Red-WhiskeredBulbul1.jpg",
    "quick_facts": {
        "family": "Pycnonotidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fruit, nectar and insects",
        "habitat": "woodland, scrub, gardens, plantations and towns",
        "behaviour": "moves actively through vegetation in pairs or small groups",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Red-Whiskered Bulbul is best separated from Red-vented Bulbul by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Red-vented Bulbul, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. White-browed Bulbul can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Red-winged Blackbird",
    "scientific": "Agelaius phoeniceus",
    "description": "The Red-winged Blackbird is a widespread North American blackbird. Males are glossy black with vivid red and yellow shoulder patches, while females are streaked brown. Males defend territories aggressively during the breeding season and display their colourful shoulder patches during disputes.",
    "image": "Red-WingedBlackbird1.jpg",
    "quick_facts": {
        "family": "Icteridae",
        "size": "17-23 cm",
        "weight": "About 42-85 g",
        "wingspan": "About 31-40 cm",
        "diet": "seeds, insects and grains",
        "habitat": "marshes, grassland, farmland, wetlands and open woodland",
        "behaviour": "males defend territories from prominent perches while females forage lower",
        "activity": "Diurnal",
        "nesting": "A cup-shaped nest woven from grasses and reeds, usually attached to vegetation",
        "breeding_season": "March to August",
        "clutch_size": "Usually 2-4 eggs",
        "call": "Distinctive nasal 'konk-a-ree' song",
        "lifespan": "Up to about 15 years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Canada: most provinces; United States: most states; Mexico: northern and central regions"
    },
    "similar_birds": "Red-winged Blackbird is best separated from Tricolored Blackbird by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Tricolored Blackbird, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Common Grackle can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "Cornell Lab of Ornithology — All About Birds / eBird",
        "Audubon — North American bird identification and natural history",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Rose-breasted Grosbeak",
    "scientific": "Pheucticus ludovicianus",
    "description": "The Rose-breasted Grosbeak is a handsome North American songbird. Breeding males have a black head, white underparts and a vivid rose-red breast patch, while females and immature birds are brown and heavily streaked. Its large conical bill is well suited to cracking seeds.",
    "image": "Rose-BreastedGrosbeak1.jpg",
    "quick_facts": {
        "family": "Cardinalidae",
        "size": "18-22 cm",
        "weight": "About 39-49 g",
        "wingspan": "About 29-33 cm",
        "diet": "seeds, fruit and insects",
        "habitat": "deciduous woodland, forest edges, gardens and thickets",
        "behaviour": "forages in foliage and often sings from shaded perches",
        "activity": "Diurnal",
        "nesting": "A loose open cup of twigs and plant material placed in a shrub or low tree",
        "breeding_season": "May to July",
        "clutch_size": "Usually 3-5 eggs",
        "call": "Rich robin-like song and sharp chink calls",
        "lifespan": "Up to about 13 years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Canada: southern and central provinces; United States: northern and eastern states; winters mainly in Mexico, Central America and the Caribbean"
    },
    "similar_birds": "Rose-breasted Grosbeak is best separated from Black-headed Grosbeak by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Black-headed Grosbeak, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Scarlet Tanager can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "Cornell Lab of Ornithology — All About Birds / eBird",
        "Audubon — North American bird identification and natural history",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Rose-Ringed Parakeet",
    "scientific": "Psittacula krameri",
    "description": "The Rose-Ringed Parakeet is a bright green long-tailed parakeet with a red bill and a neck ring in adult males, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in woodland, farmland, parks, gardens and cities and feeds mainly on seeds, fruit, flowers and grains. It travels in noisy flocks and readily uses urban trees. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "Rose-RingedParakeet1.jpg",
    "quick_facts": {
        "family": "Psittaculidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "seeds, fruit, flowers and grains",
        "habitat": "woodland, farmland, parks, gardens and cities",
        "behaviour": "travels in noisy flocks and readily uses urban trees",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Rose-Ringed Parakeet is best separated from Alexandrine Parakeet by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Alexandrine Parakeet, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Plum-headed Parakeet can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Rufous Treepie",
    "scientific": "Dendrocitta vagabunda",
    "description": "Recognising the Rufous Treepie starts with a long-tailed brown, grey and black corvid with a rich rufous body. The species uses woodland, scrub, farmland, gardens and forest edges and takes fruit, insects, small animals and carrion as its principal food. It moves noisily through trees and often forages in groups. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "RufousTreepie1.jpg",
    "quick_facts": {
        "family": "Corvidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fruit, insects, small animals and carrion",
        "habitat": "woodland, scrub, farmland, gardens and forest edges",
        "behaviour": "moves noisily through trees and often forages in groups",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Rufous Treepie is best separated from Grey Treepie by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Grey Treepie, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Common Myna can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Sand Martin",
    "scientific": "Riparia riparia",
    "description": "The Sand Martin is a small brown-and-white swallow with a dark breast band and rapid, agile flight. It usually breeds colonially by excavating tunnels into sandy or soft earth near rivers, lakes and quarries. It spends much of its time in the air catching flying insects.",
    "image": "SandMartin1.jpg",
    "quick_facts": {
        "family": "Hirundinidae",
        "size": "12-13 cm",
        "weight": "About 11-18 g",
        "wingspan": "About 26-30 cm",
        "diet": "flying insects",
        "habitat": "riverbanks, wetlands, farmland and open country",
        "behaviour": "feeds almost entirely in flight and nests colonially in sandy banks",
        "activity": "Diurnal",
        "nesting": "A tunnel excavated in a sandy or earthen bank, ending in a nest chamber",
        "breeding_season": "April to August in much of its northern breeding range",
        "clutch_size": "Usually 3-7 eggs",
        "call": "Rapid dry chattering calls",
        "lifespan": "Can live for several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Europe, northern Asia and North America; winters mainly in Africa, South Asia and South America depending on population"
    },
    "similar_birds": "Sand Martin is best separated from Barn Swallow by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Barn Swallow, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. House Martin can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Sardinian Warbler",
    "scientific": "Curruca melanocephala",
    "description": "The Sardinian Warbler is a small Mediterranean warbler with a dark head, pale throat and grey-brown body. It is an energetic and often secretive bird of dense scrub, maquis and woodland edges. It feeds mainly on insects and small fruits.",
    "image": "SardinianWarbler1.jpg",
    "quick_facts": {
        "family": "Sylviidae",
        "size": "13-14 cm",
        "weight": "About 10-15 g",
        "wingspan": "About 15-18 cm",
        "diet": "insects, berries and other small food",
        "habitat": "Mediterranean scrub, woodland edges, gardens and dry thickets",
        "behaviour": "keeps low in dense bushes and is often easier to hear than see",
        "activity": "Diurnal",
        "nesting": "A small cup nest placed low in dense shrubs",
        "breeding_season": "March to June",
        "clutch_size": "Usually 3-5 eggs",
        "call": "Fast scratchy song with harsh alarm calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Spain: Mediterranean regions and Balearic Islands; Portugal; southern France; Italy; Greece; North Africa"
    },
    "similar_birds": "Sardinian Warbler is best separated from Dartford Warbler by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Dartford Warbler, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Common Whitethroat can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "British Trust for Ornithology — European bird ecology and monitoring",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Sarus Crane",
    "scientific": "Antigone antigone",
    "description": "The Sarus Crane is a magnificent tall crane distinguished by its grey body, long pinkish legs and bare red head and upper neck. It is the world's tallest flying bird and is strongly associated with wetlands, flooded fields and open agricultural landscapes. Pairs are famous for their loud calls and coordinated courtship displays.",
    "image": "SarusCrane1.jpg",
    "quick_facts": {
        "family": "Gruidae",
        "size": "Up to about 180 cm tall",
        "weight": "About 6.8-12 kg",
        "wingspan": "About 220-280 cm",
        "diet": "roots, tubers, grains, insects and small animals",
        "habitat": "wet grassland, marshes, floodplains and agricultural wetlands",
        "behaviour": "forms strong pair bonds and performs elaborate synchronized displays",
        "activity": "Diurnal",
        "nesting": "A large mound of vegetation constructed in or beside shallow water",
        "breeding_season": "Usually during the monsoon and wet season",
        "clutch_size": "Usually 2 eggs",
        "call": "Very loud trumpeting calls often given by pairs in duet",
        "lifespan": "Can live for more than 20 years",
        "conservation_status": "🟠 Vulnerable (VU)",
        "where_to_find": "India: Uttar Pradesh, Rajasthan, Gujarat, Madhya Pradesh, Maharashtra, Bihar, Haryana, Punjab, West Bengal and other suitable regions; Nepal: Terai; Cambodia; Myanmar; northern Australia"
    },
    "similar_birds": "Sarus Crane is best separated from Brolga by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Brolga, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Common Crane can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Scaly-Breasted Munia",
    "scientific": "Lonchura punctulata",
    "description": "Recognising the Scaly-Breasted Munia starts with a small brown finch with a pale belly marked by dark scale-like feather edges. The species uses grassland, farmland, scrub, wetlands and gardens and takes grass seeds and grains as its principal food. It travels in flocks and feeds close to the ground. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "Scaly-BreastedMunia1.jpg",
    "quick_facts": {
        "family": "Estrildidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "grass seeds and grains",
        "habitat": "grassland, farmland, scrub, wetlands and gardens",
        "behaviour": "travels in flocks and feeds close to the ground",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Scaly-Breasted Munia is best separated from Indian Silverbill by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Indian Silverbill, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. White-rumped Munia can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Scarlet Tanager",
    "scientific": "Piranga olivacea",
    "description": "The Scarlet Tanager is a striking North American songbird. Breeding males are brilliant scarlet with black wings and tail, while females are yellow-green. The species spends much of its time high in mature forest canopies, where it searches for insects and fruit.",
    "image": "ScarletTanager1.jpg",
    "quick_facts": {
        "family": "Cardinalidae",
        "size": "16-17 cm",
        "weight": "About 23-38 g",
        "wingspan": "About 25-29 cm",
        "diet": "insects, fruit and berries",
        "habitat": "deciduous forest and mature woodland",
        "behaviour": "forages high in the canopy and is often hidden among leaves",
        "activity": "Diurnal",
        "nesting": "A loose open cup of twigs and grass placed on a horizontal branch",
        "breeding_season": "May to July",
        "clutch_size": "Usually 3-5 eggs",
        "call": "A rich robin-like song and a distinctive harsh call",
        "lifespan": "Often several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Canada: southern Ontario, Quebec and Atlantic provinces; United States: eastern and northern states; winters mainly in northern and western South America"
    },
    "similar_birds": "Scarlet Tanager is best separated from Summer Tanager by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Summer Tanager, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Rose-breasted Grosbeak can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "Cornell Lab of Ornithology — All About Birds / eBird",
        "Audubon — North American bird identification and natural history",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Secretarybird",
    "scientific": "Sagittarius serpentarius",
    "description": "The Secretarybird is a remarkable African terrestrial bird of prey with extremely long legs, a crest of elongated black feathers and a powerful hooked bill. Unlike most raptors, it spends much of its time walking through open grassland while searching for prey. It is particularly famous for using powerful kicks to subdue snakes and other animals.",
    "image": "Secretarybird1.jpg",
    "quick_facts": {
        "family": "Sagittariidae",
        "size": "112-150 cm",
        "weight": "About 2.3-4.3 kg",
        "wingspan": "About 190-220 cm",
        "diet": "snakes, lizards, insects and small mammals",
        "habitat": "open savanna, grassland and semi-arid country",
        "behaviour": "walks long distances while stamping and striking prey with its feet",
        "activity": "Diurnal",
        "nesting": "A large stick nest constructed in a tree or thorny shrub",
        "breeding_season": "Varies geographically, often during the dry or early wet season",
        "clutch_size": "Usually 1-3 eggs",
        "call": "Generally quiet; produces croaks, hisses and other low calls around the nest",
        "lifespan": "Can live for 10-20 years",
        "conservation_status": "🔴 Endangered(EN)",
        "where_to_find": "Africa: South Africa, Namibia, Botswana, Zimbabwe, Zambia, Kenya, Tanzania, Uganda, Ethiopia, Sudan and other sub-Saharan countries"
    },
    "similar_birds": "Secretarybird is best separated from Bateleur by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Bateleur, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Southern Ground Hornbill can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — Birds of the World / eBird",
        "IUCN Red List of Threatened Species",
        "Raptors of the World / regional raptor references"
    ]
},

{
    "name": "Shikra",
    "scientific": "Accipiter badius",
    "description": "The Shikra is a small accipiter with rounded wings, a long tail and a hooked bill, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in woodland, farmland, gardens and open forest and feeds mainly on small birds, reptiles, rodents and insects. It hunts from cover and makes fast surprise attacks. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "Shikra1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "small birds, reptiles, rodents and insects",
        "habitat": "woodland, farmland, gardens and open forest",
        "behaviour": "hunts from cover and makes fast surprise attacks",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Shikra is best separated from Besra by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Besra, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Black-winged Kite can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Silver Gull",
    "scientific": "Chroicocephalus novaehollandiae",
    "description": "The Silver Gull is a common Australian gull with a white body, pale grey wings, black wing tips and a red bill. It is highly adaptable and occurs around beaches, estuaries, harbours, lakes and cities. Its ability to exploit food around humans has made it one of Australia's most familiar gulls.",
    "image": "SilverGull1.jpg",
    "quick_facts": {
        "family": "Laridae",
        "size": "40-45 cm",
        "weight": "About 270-315 g",
        "wingspan": "About 94-110 cm",
        "diet": "fish, invertebrates, carrion and human food",
        "habitat": "beaches, estuaries, harbours, lakes, rubbish tips and cities",
        "behaviour": "is highly adaptable and often gathers in large flocks",
        "activity": "Diurnal",
        "nesting": "A shallow nest made from vegetation, usually on islands, cliffs or sheltered ground",
        "breeding_season": "August to November",
        "clutch_size": "Usually 1-3 eggs",
        "call": "Loud gull-like cries and yelps",
        "lifespan": "Often lives for more than 10 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: all states and territories; Tasmania; New Zealand and surrounding islands"
    },
    "similar_birds": "Silver Gull is best separated from Pacific Gull by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Pacific Gull, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Kelp Gull can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Small Minivet",
    "scientific": "Pericrocotus cinnamomeus",
    "description": "The Small Minivet is a tiny colourful minivet in which males are orange-red and females are yellowish with dark wings. It is found in forest, woodland and plantations, where it feeds mainly on insects and other small arthropods. The species is often noticed because it moves through foliage in active mixed flocks. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "SmallMinivet1.jpg",
    "quick_facts": {
        "family": "Campephagidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects and other small arthropods",
        "habitat": "forest, woodland and plantations",
        "behaviour": "moves through foliage in active mixed flocks",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Small Minivet is best separated from Long-tailed Minivet by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Long-tailed Minivet, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Scarlet Minivet can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Southern Cassowary",
    "scientific": "Casuarius casuarius",
    "description": "The Southern Cassowary is a huge, flightless rainforest bird and one of Australia's most distinctive birds. Adults have glossy black, hair-like feathers, a tall helmet-like casque, blue skin on the head and neck, and bright red wattles. Females are generally larger and more brightly coloured than males. The species is mainly solitary and spends much of its time moving quietly through dense rainforest in search of fallen fruit. It plays an important ecological role because it disperses the seeds of many rainforest plants. Unlike most birds, the female lays the eggs and then leaves the male to incubate them and raise the chicks. Its powerful legs and large inner claws make it a bird that is best admired from a respectful distance.",
    "image": "SouthernCassowary1.jpg",
    "quick_facts": {
        "family": "Casuariidae",
        "size": "150-200 cm tall",
        "weight": "Females can reach about 60 kg; males are considerably smaller",
        "wingspan": "Reduced wings; flightless",
        "diet": "fallen fruit, seeds and small animals",
        "habitat": "tropical rainforest, swamp forest and dense woodland",
        "behaviour": "moves quietly through dense forest and disperses large seeds",
        "activity": "Diurnal, with activity varying according to conditions",
        "nesting": "A shallow scrape on the ground lined with plant material; the male incubates the eggs and raises the chicks",
        "breeding_season": "Usually June to October",
        "clutch_size": "About 4 large green eggs",
        "call": "Deep rumbling and booming sounds, often surprisingly difficult to locate",
        "lifespan": "Approximately 30 years in the wild",
        "conservation_status": "🟡 Near Threatened (NT)",
        "where_to_find": "Australia: northern Queensland, especially the Wet Tropics and Cape York Peninsula; also New Guinea and eastern Indonesia"
    },
    "similar_birds": "Southern Cassowary is best separated from Emu by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Emu, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Northern Cassowary can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Spotted Dove",
    "scientific": "Spilopelia chinensis",
    "description": "Recognising the Spotted Dove starts with a medium-sized dove with a black-and-white spotted neck patch and warm brown body. The species uses farmland, gardens, towns, scrub and woodland and takes seeds and grains as its principal food. It forages mainly on the ground and often lives near people. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "SpottedDove1.jpg",
    "quick_facts": {
        "family": "Columbidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "seeds and grains",
        "habitat": "farmland, gardens, towns, scrub and woodland",
        "behaviour": "forages mainly on the ground and often lives near people",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Spotted Dove is best separated from Laughing Dove by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Laughing Dove, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Oriental Turtle Dove can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Spotted Owlet",
    "scientific": "Athene brama",
    "description": "The Spotted Owlet is a small spotted owl with a rounded head, pale eyebrows and bright yellow eyes, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in woodland, farmland, gardens, villages and urban areas and feeds mainly on insects, small reptiles, rodents and birds. It often hunts from exposed perches around dusk and at night. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "SpottedOwlet1.jpg",
    "quick_facts": {
        "family": "Strigidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects, small reptiles, rodents and birds",
        "habitat": "woodland, farmland, gardens, villages and urban areas",
        "behaviour": "often hunts from exposed perches around dusk and at night",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Spotted Owlet is best separated from Jungle Owlet by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Jungle Owlet, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Little Owl can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — Birds of the World / eBird",
        "IUCN Red List of Threatened Species",
        "Raptors of the World / regional raptor references"
    ]
},

{
    "name": "Stork-Billed Kingfisher",
    "scientific": "Pelargopsis capensis",
    "description": "The Stork-Billed Kingfisher is a very large kingfisher with a massive red bill, blue-green wings and warm brown head, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in rivers, lakes, forest streams, mangroves and wetlands and feeds mainly on fish, frogs, crabs, reptiles and other animals. It perches quietly near water before making powerful dives. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "Stork-BilledKingfisher1.jpg",
    "quick_facts": {
        "family": "Alcedinidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fish, frogs, crabs, reptiles and other animals",
        "habitat": "rivers, lakes, forest streams, mangroves and wetlands",
        "behaviour": "perches quietly near water before making powerful dives",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Stork-Billed Kingfisher is best separated from White-throated Kingfisher by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with White-throated Kingfisher, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Common Kingfisher can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Sulphur-crested Cockatoo",
    "scientific": "Cacatua galerita",
    "description": "The Sulphur-crested Cockatoo is a large white cockatoo with a striking yellow crest and a powerful dark bill. When alarmed or excited, it raises the yellow crest into a dramatic fan. It is highly intelligent, social and adaptable, and can be found in forests, woodland, farmland and urban environments. Large flocks may gather in trees or feed on the ground, where they search for seeds, roots, fruits and other plant material. Its loud calls can carry over considerable distances, making the species much easier to hear than to overlook. It is also one of Australia's most familiar urban birds, particularly in eastern Australia.",
    "image": "Sulphur-CrestedCockatoo1.jpg",
    "quick_facts": {
        "family": "Cacatuidae",
        "size": "45-50 cm",
        "weight": "About 800-1000 g",
        "wingspan": "About 100-110 cm",
        "diet": "seeds, nuts, roots, fruit and other plant material",
        "habitat": "forest, woodland, farmland, parks and suburbs",
        "behaviour": "forms noisy flocks and uses its strong bill to manipulate food",
        "activity": "Diurnal",
        "nesting": "A tree hollow, often lined with decayed wood",
        "breeding_season": "Usually August to January",
        "clutch_size": "Usually 2-3 eggs",
        "call": "Very loud, harsh screeches and repeated contact calls",
        "lifespan": "Can reach about 80 years in captivity",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: mainly eastern and northern Australia, including Queensland, New South Wales and Victoria; also introduced populations in parts of Western Australia"
    },
    "similar_birds": "Sulphur-crested Cockatoo is best separated from Galah by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Galah, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Little Corella can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird and life-history information",
        "IUCN Red List of Threatened Species"
    ]
},

{
    "name": "Superb Fairywren",
    "scientific": "Malurus cyaneus",
    "description": "The Superb Fairywren is a tiny Australian songbird famous for the brilliant blue breeding plumage of the male. The male has a bright blue crown, ear coverts and throat, contrasted with a dark eye stripe and blue-black upperparts, while females and young birds are mostly brown. It lives in small social groups and spends much of its time hopping through dense vegetation and foraging close to the ground. Although it is small and delicate-looking, it is an active and highly social bird. It can be distinguished from other fairywrens by the male's particularly vivid blue breeding plumage and its preference for dense understorey in woodland, gardens and parks.",
    "image": "SuperbFairywren1.jpg",
    "quick_facts": {
        "family": "Maluridae",
        "size": "13-14 cm",
        "weight": "About 8-13 g",
        "wingspan": "About 14-18 cm",
        "diet": "insects and other small arthropods, with seeds also taken",
        "habitat": "woodland, scrub, gardens and dense undergrowth",
        "behaviour": "lives in social family groups and forages close to the ground",
        "activity": "Diurnal",
        "nesting": "A small domed nest with a side entrance, made from grasses and spider webbing and usually placed low in dense vegetation",
        "breeding_season": "Usually September to January",
        "clutch_size": "3-4 eggs",
        "call": "Sharp, repeated contact and alarm calls",
        "lifespan": "Usually several years, with survival strongly affected by predators and environmental conditions",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: New South Wales, Victoria, Tasmania, South Australia and southeastern Queensland"
    },
    "similar_birds": "Superb Fairywren is best separated from Variegated Fairywren by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Variegated Fairywren, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Splendid Fairywren can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Superb Lyrebird",
    "scientific": "Menura novaehollandiae",
    "description": "The Superb Lyrebird is a large Australian ground-dwelling bird famous for the elaborate lyre-shaped tail of the adult male and its extraordinary ability to mimic natural and mechanical sounds. It lives mainly in moist forests and rainforests, where it scratches through leaf litter while searching for food.",
    "image": "SuperbLyrebird1.jpg",
    "quick_facts": {
        "family": "Menuridae",
        "size": "74-100 cm",
        "weight": "About 700-1,200 g",
        "wingspan": "About 75-90 cm",
        "diet": "insects, worms and other forest-floor invertebrates",
        "habitat": "wet forest, rainforest and dense understorey",
        "behaviour": "scratches through leaf litter and males perform elaborate displays while mimicking sounds",
        "activity": "Diurnal",
        "nesting": "A large domed nest built by the female, usually close to the ground or on a bank",
        "breeding_season": "May to August",
        "clutch_size": "Usually 1 egg",
        "call": "Remarkable mimicry of birds, mammals and mechanical sounds, along with whistles and alarm calls",
        "lifespan": "Often lives for more than 15 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: New South Wales, Victoria and southeastern Queensland"
    },
    "similar_birds": "Superb Lyrebird is best separated from Albert's Lyrebird by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Albert's Lyrebird, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Superb Fairywren can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Tawny Frogmouth",
    "scientific": "Podargus strigoides",
    "description": "The Tawny Frogmouth is a distinctive Australian night bird that is often mistaken for an owl because of its large eyes, upright posture and nocturnal habits. It is actually more closely related to nightjars than to true owls. Its grey, brown and rufous mottled plumage provides excellent camouflage when it sits motionless against a tree branch during the day. Unlike owls, it has relatively weak feet and does not have the strongly curved talons typical of birds of prey. At night it becomes active and hunts insects, worms, snails and occasionally small vertebrates, usually by dropping onto prey from a perch. It occurs in a remarkably wide variety of Australian habitats, from woodland and forest to urban areas.",
    "image": "TawnyFrogmouth1.jpg",
    "quick_facts": {
        "family": "Podargidae",
        "size": "34-53 cm",
        "weight": "About 140-680 g",
        "wingspan": "About 65-90 cm",
        "diet": "insects, frogs, reptiles and small mammals",
        "habitat": "woodland, forest edges, parks and gardens",
        "behaviour": "sits motionless against branches during the day and hunts at night",
        "activity": "Nocturnal",
        "nesting": "A small platform of sticks placed on a horizontal tree branch",
        "breeding_season": "Usually August to December",
        "clutch_size": "Usually 2-3 eggs",
        "call": "A deep, repeated booming or grunting call",
        "lifespan": "Can live for many years; captive birds have exceeded 10 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: widespread across mainland Australia and Tasmania, except the densest rainforests and treeless deserts"
    },
    "similar_birds": "Tawny Frogmouth is best separated from Podargus species by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Podargus species, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Australian Owlet-nightjar can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Wedge-tailed Eagle",
    "scientific": "Aquila audax",
    "description": "The Wedge-tailed Eagle is Australia's largest living bird of prey and one of the world's largest eagles. It has long wings, fully feathered legs and a distinctive long wedge-shaped tail that gives the species its name. Adults are generally dark brown to blackish-brown, while younger birds are lighter reddish-brown and become darker as they mature. Wedge-tailed Eagles are powerful hunters but are also important scavengers, feeding on carrion when available. They spend long periods soaring on thermal air currents while searching the landscape below.",
    "image": "Wedge-TailedEagle1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "87-105 cm",
        "weight": "Males about 3.2-4.0 kg; females about 4.2-5.3 kg",
        "wingspan": "Up to about 230 cm",
        "diet": "mammals, birds, reptiles and carrion",
        "habitat": "open woodland, grassland, farmland and arid country",
        "behaviour": "soars for long periods while searching the landscape below",
        "activity": "Diurnal",
        "nesting": "A very large stick nest built in a tall tree or sometimes on a cliff",
        "breeding_season": "Usually May to September",
        "clutch_size": "Usually 1-2 eggs",
        "call": "A range of whistles and high-pitched calls, especially around the nest",
        "lifespan": "Can live for more than 20 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: widespread across mainland Australia and Tasmania; also occurs in southern New Guinea"
    },
    "similar_birds": "Wedge-tailed Eagle is best separated from White-bellied Sea-Eagle by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with White-bellied Sea-Eagle, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Little Eagle can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Welcome Swallow",
    "scientific": "Hirundo neoxena",
    "description": "The Welcome Swallow is a small, fast-flying Australian swallow with a glossy blue-black back, reddish forehead and throat, pale underparts and a deeply forked tail. It is one of the most familiar swallows in Australia and can be found around wetlands, farmland, open woodland, parks, towns and coastal areas. Welcome Swallows spend much of their time in flight catching insects, often flying low over water or grassland. They are agile fliers capable of sudden turns and rapid changes of direction while pursuing flying insects. The species frequently nests on buildings, bridges and other structures close to suitable feeding areas.",
    "image": "WelcomeSwallow1.jpg",
    "quick_facts": {
        "family": "Hirundinidae",
        "size": "15-17 cm",
        "weight": "About 15-20 g",
        "wingspan": "About 30 cm",
        "diet": "flying insects",
        "habitat": "wetlands, farmland, grassland, parks, towns and coasts",
        "behaviour": "spends much of its time in fast aerial flight and nests on buildings and bridges",
        "activity": "Diurnal",
        "nesting": "A mud cup nest attached to a wall, building, bridge or other structure",
        "breeding_season": "Usually August to February",
        "clutch_size": "Usually 3-5 eggs",
        "call": "Rapid twittering and soft chattering calls",
        "lifespan": "Often several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: widespread across Queensland, New South Wales, Victoria, South Australia, Western Australia, the Northern Territory and Tasmania"
    },
    "similar_birds": "Welcome Swallow is best separated from Fairy Martin by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Fairy Martin, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Tree Swallow can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "White Stork",
    "scientific": "Ciconia ciconia",
    "description": "The White Stork is a large, long-legged wading bird with mostly white plumage, black flight feathers, a long red bill and red legs. It is strongly associated with open landscapes and often builds its enormous stick nest on tall structures such as trees, chimneys, rooftops and electricity pylons. White Storks feed opportunistically, walking across grasslands, wetlands and agricultural fields while searching for insects, amphibians, reptiles, small mammals and other prey. Many populations undertake long-distance migrations between Europe and Africa, using rising thermal air currents to travel efficiently. The species is particularly notable for its traditional nesting sites, with some pairs returning to the same areas year after year.",
    "image": "WhiteStork1.jpg",
    "quick_facts": {
        "family": "Ciconiidae",
        "size": "100-125 cm",
        "weight": "About 3.3-3.5 kg",
        "wingspan": "155-165 cm",
        "diet": "insects, frogs, small mammals, reptiles and fish",
        "habitat": "wet grassland, farmland, marshes and open country",
        "behaviour": "walks slowly across open ground while searching for prey",
        "activity": "Diurnal",
        "nesting": "Large stick nest built on trees, buildings, chimneys, pylons or other elevated structures",
        "breeding_season": "Usually March to July in European breeding areas",
        "clutch_size": "Usually 3-5 eggs",
        "call": "Mostly silent; famously communicates at the nest by bill-clattering",
        "lifespan": "Can live up to about 40 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Europe: widespread in southern, central and eastern Europe; also western Asia and North Africa. Migratory populations winter mainly in sub-Saharan Africa"
    },
    "similar_birds": "White Stork is best separated from Black Stork by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Black Stork, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Woolly-necked Stork can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "British Trust for Ornithology — European bird ecology and monitoring",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "White-bellied Drongo",
    "scientific": "Dicrurus caerulescens",
    "description": "The White-bellied Drongo is a striking Indian drongo with dark blue-black upperparts, a contrasting pale belly and a deeply forked tail. It is an active insect hunter and often sits on exposed perches before making short flights to catch prey.",
    "image": "White-BelliedDrongo1.jpg",
    "quick_facts": {
        "family": "Dicruridae",
        "size": "28-30 cm",
        "weight": "About 40-55 g",
        "wingspan": "About 40-45 cm",
        "diet": "insects and other small arthropods",
        "habitat": "forest, woodland and scrub, especially in the Indian subcontinent",
        "behaviour": "hunts from perches and makes short aerial sallies",
        "activity": "Diurnal",
        "nesting": "A small cup nest placed in a tree fork",
        "breeding_season": "March to June",
        "clutch_size": "Usually 2-4 eggs",
        "call": "Varied whistles, harsh notes and imitations of other birds",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "India: Maharashtra, Goa, Karnataka, Kerala and Tamil Nadu; Sri Lanka"
    },
    "similar_birds": "White-bellied Drongo is best separated from Black Drongo by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Black Drongo, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Ashy Drongo can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "White-Bellied Sea-Eagle",
    "scientific": "Icthyophaga leucogaster",
    "description": "The White-Bellied Sea-Eagle is a large coastal eagle with a white head and belly contrasting with dark wings and back, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in coasts, estuaries, rivers, lakes and large wetlands and feeds mainly on fish, waterbirds, reptiles and carrion. It soars over water and often carries prey in its talons. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "White-BelliedSea-Eagle1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fish, waterbirds, reptiles and carrion",
        "habitat": "coasts, estuaries, rivers, lakes and large wetlands",
        "behaviour": "soars over water and often carries prey in its talons",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "White-Bellied Sea-Eagle is best separated from Wedge-tailed Eagle by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Wedge-tailed Eagle, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. White-tailed Sea-Eagle can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "White-Breasted Waterhen",
    "scientific": "Amaurornis phoenicurus",
    "description": "The White-Breasted Waterhen is a dark rail with a white face, breast and belly and a red bill and legs, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in marshes, ponds, rice fields, mangroves and wet grassland and feeds mainly on insects, seeds, aquatic plants and small animals. It walks through dense vegetation at the water's edge and often calls loudly. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "White-BreastedWaterhen1.jpg",
    "quick_facts": {
        "family": "Rallidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects, seeds, aquatic plants and small animals",
        "habitat": "marshes, ponds, rice fields, mangroves and wet grassland",
        "behaviour": "walks through dense vegetation at the water's edge and often calls loudly",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "White-Breasted Waterhen is best separated from White-breasted Waterhen by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with White-breasted Waterhen, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Common Moorhen can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "White-Browed Fantail",
    "scientific": "Rhipidura aureola",
    "description": "Recognising the White-Browed Fantail starts with a small dark fantail with a white eyebrow and boldly fanned tail. The species uses forest, woodland, plantations and gardens and takes flying insects as its principal food. It fans its tail repeatedly while making short aerial sallies. Although it may be familiar in suitable areas, its behaviour can be surprisingly varied, especially outside the breeding season.",
    "image": "White-BrowedFantail1.jpg",
    "quick_facts": {
        "family": "Rhipiduridae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "flying insects",
        "habitat": "forest, woodland, plantations and gardens",
        "behaviour": "fans its tail repeatedly while making short aerial sallies",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "White-Browed Fantail is best separated from White-throated Fantail by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with White-throated Fantail, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Willie Wagtail can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "White-Browed Wagtail",
    "scientific": "Motacilla maderaspatensis",
    "description": "The White-Browed Wagtail is a large black-and-white wagtail with a bold white eyebrow and long tail. It is found in rivers, streams, ponds, gardens, farmland and towns, where it feeds mainly on insects and other small invertebrates. The species is often noticed because it walks briskly on the ground while constantly wagging its tail. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "White-BrowedWagtail1.jpg",
    "quick_facts": {
        "family": "Motacillidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "insects and other small invertebrates",
        "habitat": "rivers, streams, ponds, gardens, farmland and towns",
        "behaviour": "walks briskly on the ground while constantly wagging its tail",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "White-Browed Wagtail is best separated from White Wagtail by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with White Wagtail, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Grey Wagtail can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "White-Rumped Munia",
    "scientific": "Lonchura striata",
    "description": "The White-Rumped Munia is a small brown munia with a conspicuous white rump and stout conical bill, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in grassland, farmland, scrub and wetlands and feeds mainly on grass seeds and grains. It travels in flocks and feeds on the ground. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "White-RumpedMunia1.jpg",
    "quick_facts": {
        "family": "Estrildidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "grass seeds and grains",
        "habitat": "grassland, farmland, scrub and wetlands",
        "behaviour": "travels in flocks and feeds on the ground",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "White-Rumped Munia is best separated from Scaly-breasted Munia by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Scaly-breasted Munia, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Indian Silverbill can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "White-Throated Kingfisher",
    "scientific": "Halcyon smyrnensis",
    "description": "The White-Throated Kingfisher is a bright blue-and-chestnut kingfisher with a large red bill and clean white throat. It is found in woodland, farmland, gardens, wetlands and towns, where it feeds mainly on fish, frogs, lizards, insects and small animals. The species is often noticed because it often perches conspicuously and dives or drops onto prey. Its behaviour and appearance are closely tied to the habitat it occupies, and individuals may change their feeding routine with season and local conditions.",
    "image": "White-ThroatedKingfisher1.jpg",
    "quick_facts": {
        "family": "Alcedinidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fish, frogs, lizards, insects and small animals",
        "habitat": "woodland, farmland, gardens, wetlands and towns",
        "behaviour": "often perches conspicuously and dives or drops onto prey",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "White-Throated Kingfisher is best separated from Common Kingfisher by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Common Kingfisher, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Stork-billed Kingfisher can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Willie Wagtail",
    "scientific": "Rhipidura leucophrys",
    "description": "The Willie Wagtail is a familiar black-and-white Australian fantail with a long rounded tail and a distinctive white eyebrow. Despite its name, it is not a true wagtail like the Eurasian species of the family Motacillidae. Instead, it belongs to the fantail family. Willie Wagtails are energetic birds that frequently chase insects through the air, often returning to a low perch between flights. They are highly adaptable and can live in woodland, farmland, wetlands, parks and gardens. Their cheerful appearance and active behaviour make them one of the easiest Australian birds to notice. They are also known for their varied songs and bold behaviour around other birds.",
    "image": "WillieWagtail1.jpg",
    "quick_facts": {
        "family": "Rhipiduridae",
        "size": "About 20 cm",
        "weight": "About 17-24 g",
        "wingspan": "About 30 cm",
        "diet": "insects and other small arthropods",
        "habitat": "open woodland, farmland, wetlands, parks and gardens",
        "behaviour": "chases flying insects with energetic aerial sallies and fans its tail",
        "activity": "Diurnal",
        "nesting": "A small cup-shaped nest made from grass, bark and spider web, usually placed on a horizontal branch",
        "breeding_season": "Usually July to January, with breeding possible during other periods in suitable conditions",
        "clutch_size": "Usually 2-4 eggs",
        "call": "A varied series of musical, chattering and alarm notes",
        "lifespan": "Usually several years in the wild",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia: widespread across mainland Australia, including most states and territories; also occurs in parts of New Guinea, the Moluccas and Solomon Islands"
    },
    "similar_birds": "Willie Wagtail is best separated from White-browed Fantail by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with White-browed Fantail, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Magpie-lark can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Woolly-Necked Stork",
    "scientific": "Ciconia episcopus",
    "description": "The Woolly-Necked Stork is a large dark stork with a contrasting white neck and long legs and bill, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in wet grassland, marshes, open woodland and agricultural wetlands and feeds mainly on fish, frogs, reptiles, insects and small mammals. It walks slowly through shallow water and open ground while hunting. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "Woolly-NeckedStork1.jpg",
    "quick_facts": {
        "family": "Ciconiidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fish, frogs, reptiles, insects and small mammals",
        "habitat": "wet grassland, marshes, open woodland and agricultural wetlands",
        "behaviour": "walks slowly through shallow water and open ground while hunting",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟡 Near Threatened (NT)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Woolly-Necked Stork is best separated from Asian Openbill by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Asian Openbill, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Painted Stork can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife International — species factsheet and distribution",
        "Cornell Lab of Ornithology — eBird species accounts and identification",
        "Bombay Natural History Society — Indian bird research and conservation",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Yellow-Footed Green Pigeon",
    "scientific": "Treron phoenicopterus",
    "description": "The Yellow-Footed Green Pigeon is a green pigeon with yellow feet, a pale head and subtle orange and yellow plumage details, and its appearance makes it reasonably distinctive once the main field marks are familiar. It occurs in forest, woodland, orchards and fruiting trees and feeds mainly on fruit, berries and other plant material. It feeds quietly in trees and may gather at fruiting trees. Like many birds with a broad range, it can behave differently from one region to another, particularly when food, water or cover changes.",
    "image": "Yellow-FootedGreenPigeon1.jpg",
    "quick_facts": {
        "family": "Columbidae",
        "size": "Species-specific size varies by sex and region",
        "weight": "Not given where a current, consistent figure could not be verified",
        "wingspan": "Not given where a current, consistent figure could not be verified",
        "diet": "fruit, berries and other plant material",
        "habitat": "forest, woodland, orchards and fruiting trees",
        "behaviour": "feeds quietly in trees and may gather at fruiting trees",
        "activity": "Diurnal",
        "nesting": "Breeding and nest placement vary by region; typically uses a species-specific sheltered nest site",
        "breeding_season": "Varies with region, rainfall and local conditions",
        "clutch_size": "Varies by species and region",
        "call": "Species-specific calls, including contact and territorial vocalisations",
        "lifespan": "Not given where a current, consistent figure could not be verified",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "See current species distribution in BirdLife International and the IUCN Red List."
    },
    "similar_birds": "Yellow-Footed Green Pigeon is best separated from Yellow-legged Green Pigeon by looking at the overall shape and the strongest plumage pattern rather than one small mark. Compared with Yellow-legged Green Pigeon, it has a different combination of colour, proportions and typical behaviour, which becomes clearer when the whole bird is visible. Orange-breasted Green Pigeon can also resemble it in some settings, but differences in bill shape, tail length, wing pattern, posture or habitat can help narrow the identification. Calls and behaviour are useful supporting clues when plumage is difficult to see, especially for birds that spend much of their time in dense vegetation. Using several features together is more reliable than identifying the bird from a single characteristic.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},

{
    "name": "Black Swan",
    "scientific": "Cygnus atratus",
    "description": "Black Swan is a large Australian waterbird distinguished by its mostly black plumage, broad white wing feathers and striking red bill. It occurs on lakes, rivers, wetlands, estuaries and sheltered coastal waters, where it feeds mainly by grazing on aquatic vegetation. It is strongly social and often forms large groups, especially where food and open water are plentiful. Unlike many large swans, it commonly feeds with its head and long neck submerged while swimming.",
    "image": "BlackSwan1.jpg",
    "quick_facts": {
        "family": "Anatidae",
        "size": "110–142 cm",
        "weight": "About 3.7–9 kg",
        "wingspan": "160–200 cm",
        "diet": "Mainly aquatic vegetation and algae; also some terrestrial vegetation and small aquatic animals",
        "habitat": "Freshwater lakes, rivers, wetlands, estuaries, lagoons and sheltered coastal waters",
        "behaviour": "Highly social; grazes while swimming and often gathers in large flocks; strong sustained flight",
        "activity": "Diurnal",
        "nesting": "Large nest of reeds, grasses and other vegetation, usually on or close to water",
        "breeding_season": "Variable across Australia and strongly influenced by rainfall and water conditions; breeding can occur through much of the year in favourable conditions",
        "clutch_size": "Usually 5–9 eggs",
        "call": "Soft bugling and trumpeting calls; hissing and other calls also occur, especially around nesting birds",
        "lifespan": "Can live for more than 20 years",
        "conservation_status": "🟢 Least Concern (LC)",
        "where_to_find": "Australia, including Tasmania; established populations also occur in New Zealand and some introduced localities"
    },
    "similar_birds": "Black Swan is unlikely to be confused with most Australian waterbirds once its combination of black body, white flight feathers and red bill is visible. Australian Shelduck is much smaller and has a very different chestnut, white and black pattern, while Cape Barren Goose is bulkier and grey rather than predominantly black. The Black Swan's long neck, strongly aquatic behaviour and broad white wing panels in flight are particularly useful field marks. Its habit of gathering in large groups on open water also helps separate it from smaller dark waterfowl. Range and habitat provide useful supporting evidence when lighting makes plumage harder to judge.",
    "sources": [
        "BirdLife Australia — species profile and distribution",
        "Australian Museum — Australian bird biology and identification",
        "IUCN Red List of Threatened Species — conservation status"
    ]
},
]
for bird in birds:
    page = template
    page = page.replace("{{NAME}}", bird["name"])
    page = page.replace("{{SCIENTIFIC}}", bird["scientific"])
    page = page.replace("{{DESCRIPTION}}", bird["description"])
    page = page.replace("{{IMAGE}}", bird["image"])
    page = page.replace("{{WINGSPAN}}",bird["quick_facts"]["wingspan"])
    page = page.replace("{{FAMILY}}",bird["quick_facts"]["family"])
    page = page.replace("{{BREEDING_SEASON}}",bird["quick_facts"]["breeding_season"])
    page = page.replace("{{CLUTCH_SIZE}}", bird["quick_facts"]["clutch_size"])
    page = page.replace("{{ACTIVITY}}",bird["quick_facts"]["activity"])
    page = page.replace("{{CONSERVATION_STATUS}}", bird["quick_facts"]["conservation_status"])
    page = page.replace("{{CALL}}", bird["quick_facts"]["call"])
    page = page.replace("{{LIFESPAN}}", bird["quick_facts"]["lifespan"])
    page = page.replace("{{NESTING}}",bird["quick_facts"]["nesting"])
    page = page.replace("{{HABITAT}}", bird["quick_facts"]["habitat"])
    page = page.replace("{{WHERE_TO_FIND}}",bird["quick_facts"]["where_to_find"])
    page = page.replace("{{SIZE}}",bird["quick_facts"]["size"])
    page = page.replace("{{WEIGHT}}",bird["quick_facts"]["weight"])
    page = page.replace("{{DIET}}",bird["quick_facts"]["diet"])
    page = page.replace("{{BEHAVIOUR}}",bird["quick_facts"]["behaviour"])
    page = page.replace("{{SOURCES}}", ", ".join(bird["sources"]))
    page = page.replace("{{SIMILAR_BIRDS}}", bird["similar_birds"])
    
    current_index = birds.index(bird)
    if current_index < len(birds) - 1:
       next_bird = birds[current_index + 1]
       next_page = next_bird["name"].lower().replace(" ", "-") + ".html"
       page = page.replace("{{NEXT_PAGE}}", next_page)
    else:
        page = page.replace("{{NEXT_PAGE}}", "")
    if current_index > 0:
       previous_bird = birds[current_index - 1]
       previous_page = previous_bird["name"].lower().replace(" ", "-") + ".html"
       page = page.replace("{{PREVIOUS_PAGE}}", previous_page)
      
    else:
         page = page.replace("{{PREVIOUS_PAGE}}","")
       
    filename = bird["name"].lower().replace(" ", "-") + ".html"

    open("birds/" + filename, "w").write(page)

    
index_template = open("index_template.html", "r").read()



bird_list = ""

for bird in birds:
    filename = bird["name"].lower().replace(" ", "-") + ".html"
    bird_list += '<li class="bird"><a style = "text-decoration:none;" href="birds/' + filename + '">' +  bird["name"] + '</a></li>'

date = datetime.date.today().timetuple().tm_yday
bod_random = random.Random(date)
bird_of_the_day = bod_random.choice(birds)
bod_image = bird_of_the_day["image"]
bod_filename = bird_of_the_day["name"].lower().replace(" ","-") + ".html"
bird_count = len(birds)

index = index_template.replace("{{BIRD_COUNT}}", str(bird_count))
index = index.replace("{{BIRD_LIST}}",bird_list)
index = index.replace("{{BIRD_OF_THE_DAY}}", bird_of_the_day["name"])
index = index.replace("{{BOD_FILENAME}}", bod_filename)
index = index.replace("{{BOD_IMAGE}}", bod_image)
open("index.html", "w").write(index)

print("Pages Done, Sir")
