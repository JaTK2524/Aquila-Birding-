import random
import datetime

template = open("template.html", "r").read()

birds = [
{
    "name": "Alexandrine Parakeet",
    "scientific": "Psittacula eupatria",
    "description": "The Alexandrine Parakeet is a large and striking parakeet found across the Indian subcontinent and parts of Southeast Asia. It has predominantly green plumage, a large red bill, and distinctive maroon shoulder patches. Mature males develop a dark neck ring, while females and young birds lack the complete ring. It is an adaptable bird that occurs in forests, woodlands, farmland, plantations, gardens, and urban areas, where it feeds mainly on fruits, seeds, flowers, grains, and buds. Compared with the similar Rose-Ringed Parakeet, it is distinguished by the combination of features described above. Its preference for forests, woodlands, farmland, plantations, gardens, and urban areas also helps separate it from species that use different habitats. Its characteristic behaviour, including social and active; often seen singly, in pairs, or in small groups while feeding in trees, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "AlexandrineParakeet1.jpg",
    "quick_facts": {
        "family": "Psittaculidae",
        "size": "56–62 cm",
        "weight": "200–300 g",
        "wingspan": "Approximately 20–25 cm",
        "diet": "Fruits, seeds, flowers, grains, buds, and other plant matter",
        "habitat": "Forests, woodlands, farmland, plantations, gardens, and urban areas",
        "behaviour": "Social and active; often seen singly, in pairs, or in small groups while feeding in trees",
        "activity": "Diurnal",
        "nesting": "Nests in tree cavities, usually using existing holes or abandoned woodpecker nests",
        "breeding_season": "November to April",
        "clutch_size": "2–4 eggs",
        "call": "Loud, harsh and ringing calls, often given while flying or moving between trees",
        "lifespan": "Up to around 30 years in captivity",
        "conservation_status": "Least Concern",
        "where_to_find": "India: Jammu and Kashmir, Himachal Pradesh, Uttarakhand, Uttar Pradesh, Bihar, West Bengal, Odisha, Assam, Meghalaya, Tripura, Rajasthan, Gujarat, Maharashtra, Goa, Karnataka, Kerala, Tamil Nadu, Andhra Pradesh and Telangana; Pakistan: Punjab and Sindh; Nepal: Terai and lower hills; Bangladesh: most lowland regions; Sri Lanka: lowlands; Bhutan: southern foothills; Myanmar: western and central regions; Thailand and Laos: local populations."
    }
},

{
    "name": "Asian-Green Bee-eater",
    "scientific": "Merops orientalis",
    "description": "The Asian Green Bee-eater is a small, brightly coloured insect-eating bird with vivid green plumage, a slender black bill, and a distinctive black eye stripe. It is an agile aerial hunter that launches from exposed perches to catch insects in flight before returning to the same or another perch. Despite its name, it eats a wide variety of flying insects in addition to bees. It is commonly found in open country, grasslands, agricultural areas, scrub, riverbanks, and lightly wooded habitats. Compared with the similar Blue-Tailed Bee-Eater, it is distinguished by the combination of features described above. Its preference for open woodland, grassland, farmland, scrub, riverbanks, and gardens also helps separate it from species that use different habitats. Its characteristic behaviour, including highly agile aerial hunter that frequently catches insects from the air and returns to a perch, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Asian-GreenBee-Eater1.jpg",
    "quick_facts": {
        "family": "Meropidae",
        "size": "16–18 cm",
        "weight": "15–20 g",
        "wingspan": "Approximately 28–32 cm",
        "diet": "Bees, wasps, dragonflies, butterflies, beetles, and other flying insects",
        "habitat": "Open woodland, grassland, farmland, scrub, riverbanks, and gardens",
        "behaviour": "Highly agile aerial hunter that frequently catches insects from the air and returns to a perch",
        "activity": "Diurnal",
        "nesting": "Excavates a tunnel in sandy or soft soil, banks, or other suitable ground",
        "breeding_season": "March to June, varying by region",
        "clutch_size": "4–8 eggs",
        "call": "High-pitched, rapid and pleasant twittering calls, often heard in flight",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in most states, especially Rajasthan, Gujarat, Maharashtra, Madhya Pradesh, Uttar Pradesh, Bihar, West Bengal, Odisha, Telangana, Andhra Pradesh, Karnataka, Tamil Nadu and Kerala; Pakistan: Punjab and Sindh; Nepal: Terai; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar: widespread; Thailand, Cambodia and Vietnam: widespread in suitable open country."
    }
},

{
    "name": "Asian Koel",
    "scientific": "Eudynamys scolopaceus",
    "description": "The Asian Koel is a familiar cuckoo of the Indian subcontinent, famous for its loud and distinctive calls during the breeding season. Adult males are glossy black with striking red eyes, while females are brown with extensive pale spots and streaks. Asian Koels spend much of their time in trees and feed heavily on fruits, berries, and figs. Like other cuckoos, they are brood parasites and lay their eggs in the nests of other birds, particularly crows. Compared with the similar Common Hawk-Cuckoo, it is distinguished by the combination of features described above. Its preference for woodlands, gardens, plantations, parks, forests, and urban areas also helps separate it from species that use different habitats. Its characteristic behaviour, including usually remains in trees and feeds on fruit; males are particularly vocal during breeding, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "AsianKoel1.jpg",
    "quick_facts": {
        "family": "Cuculidae",
        "size": "39–46 cm",
        "weight": "190–300 g",
        "wingspan": "Approximately 45–50 cm",
        "diet": "Fruits, berries, figs, seeds, and occasionally insects",
        "habitat": "Woodlands, gardens, plantations, parks, forests, and urban areas",
        "behaviour": "Usually remains in trees and feeds on fruit; males are particularly vocal during breeding",
        "activity": "Diurnal",
        "nesting": "Does not build its own nest; lays eggs in the nests of host birds, especially crows",
        "breeding_season": "March to August, varying by region",
        "clutch_size": "Usually 1–2 eggs laid in a host nest",
        "call": "Males produce a loud, repeated rising 'ku-oo' call; females have different harsh calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across most states, including the plains and warmer peninsular states; Pakistan: Sindh and Punjab; Nepal: Terai and lower hills; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar: widespread; Thailand, Laos, Cambodia, Vietnam, Malaysia, Singapore and Indonesia: widespread in suitable woodland and cultivated areas."
    }
},

{
    "name": "Ashy Drongo",
    "scientific": "Dicrurus leucophaeus",
    "description": "The Ashy Drongo is a slender, medium-sized drongo with grey plumage and a distinctive deeply forked tail. Its plumage varies considerably between different populations, with some forms being much darker than others. It is an active aerial hunter that frequently launches from exposed perches to capture insects in flight. The species occurs in forests, open woodland, plantations, gardens, and hilly regions and often perches prominently while scanning for prey. Compared with the similar Black Drongo, it is distinguished by the combination of features described above. Its preference for forests, woodland, plantations, gardens, scrub, and hills also helps separate it from species that use different habitats. Its characteristic behaviour, including active and agile; frequently sallies from exposed perches to catch insects in flight, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "AshyDrongo1.jpg",
    "quick_facts": {
        "family": "Dicruridae",
        "size": "25–30 cm",
        "weight": "40–60 g",
        "wingspan": "Approximately 35–40 cm",
        "diet": "Insects and other small invertebrates",
        "habitat": "Forests, woodland, plantations, gardens, scrub, and hills",
        "behaviour": "Active and agile; frequently sallies from exposed perches to catch insects in flight",
        "activity": "Diurnal",
        "nesting": "Builds a small cup-shaped nest, usually placed on a horizontal tree branch",
        "breeding_season": "April to June",
        "clutch_size": "Usually 2–4 eggs",
        "call": "Varied calls including whistles, harsh notes, and chattering sounds",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: Himalaya, Northeast, central India and peninsular hill regions, including Uttarakhand, Himachal Pradesh, West Bengal, Assam, Meghalaya, Nagaland, Madhya Pradesh, Maharashtra, Karnataka, Kerala and Tamil Nadu; Nepal: hills and foothills; Bhutan: widespread; Bangladesh: eastern regions; Myanmar: widespread; Thailand and Laos: northern and western regions."
    }
},

{
    "name": "Barn Owl",
    "scientific": "Tyto alba",
    "description": "The Barn Owl is one of the world's most widespread owls and is easily recognized by its pale, heart-shaped facial disc. Its upperparts are generally golden-brown and grey, while the underparts are often pale. It is primarily nocturnal and hunts over open ground, using its exceptional hearing and vision to locate prey. Barn Owls frequently use barns, towers, buildings, tree cavities, and other sheltered places for roosting and nesting and are especially valuable to farmers because they consume large numbers of rodents. Compared with the similar Spotted Owlet, it is distinguished by the combination of features described above. Its preference for farmland, grassland, open country, villages, wetlands, and areas around buildings also helps separate it from species that use different habitats. Its characteristic behaviour, including usually hunts low over open ground and relies heavily on hearing to locate prey, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "BarnOwl1.jpg",
    "quick_facts": {
        "family": "Tytonidae",
        "size": "32–40 cm",
        "weight": "250–550 g",
        "wingspan": "80–95 cm",
        "diet": "Small mammals, especially rodents, as well as small birds, reptiles, frogs, and insects",
        "habitat": "Farmland, grassland, open country, villages, wetlands, and areas around buildings",
        "behaviour": "Usually hunts low over open ground and relies heavily on hearing to locate prey",
        "activity": "Primarily nocturnal",
        "nesting": "Nests in cavities, barns, buildings, towers, tree hollows, and other sheltered locations",
        "breeding_season": "Varies by region; may breed throughout much of the year where food is plentiful",
        "clutch_size": "Usually 4–7 eggs",
        "call": "Harsh hissing, screeching, and rasping calls rather than the classic hoot associated with many other owls",
        "lifespan": "Around 1–5 years commonly in the wild, with some individuals living considerably longer",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread, including Punjab, Haryana, Rajasthan, Uttar Pradesh, Bihar, West Bengal, Gujarat, Maharashtra, Madhya Pradesh, Odisha, Telangana, Andhra Pradesh, Karnataka, Kerala and Tamil Nadu; Pakistan: widespread; Nepal: lowlands; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar: widespread; Europe, Africa, the Middle East and Australia: widespread in suitable open habitats."
    }
},

{
    "name": "Black Drongo",
    "scientific": "Dicrurus macrocercus",
    "description": "The Black Drongo is a bold and highly adaptable bird with glossy black plumage and a distinctive deeply forked tail. It is commonly seen perched on wires, poles, fences, and exposed branches while scanning the surroundings for insects. It is an accomplished aerial hunter and can also take prey from the ground or vegetation. Black Drongos are widespread in open country, farmland, grasslands, plantations, and urban areas and are well known for aggressively defending their territories against much larger birds. Compared with the similar Ashy Drongo, it is distinguished by the combination of features described above. Its preference for grasslands, farmland, open woodland, plantations, parks, and towns also helps separate it from species that use different habitats. Its characteristic behaviour, including aggressive and territorial; frequently chases larger birds away from its nesting area, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "BlackDrongo1.jpg",
    "quick_facts": {
        "family": "Dicruridae",
        "size": "28–31 cm",
        "weight": "70–100 g",
        "wingspan": "Approximately 35–40 cm",
        "diet": "Insects and other small invertebrates",
        "habitat": "Grasslands, farmland, open woodland, plantations, parks, and towns",
        "behaviour": "Aggressive and territorial; frequently chases larger birds away from its nesting area",
        "activity": "Diurnal",
        "nesting": "Builds a small cup-shaped nest on a horizontal branch, often high above the ground",
        "breeding_season": "April to August",
        "clutch_size": "Usually 2–4 eggs",
        "call": "Sharp, varied calls including metallic notes, whistles, and harsh sounds",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across nearly all states and many islands; Pakistan: Punjab and Sindh; Nepal: Terai and lower hills; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar: widespread; Thailand, Laos, Cambodia and Vietnam: widespread in open country."
    }
},

{
    "name": "Black-Headed Ibis",
    "scientific": "Threskiornis melanocephalus",
    "description": "The Black-Headed Ibis is a large wading bird with a mostly white body, a bare black head and neck, and long dark legs. It is commonly found in wetlands, marshes, flooded fields, riverbanks, and agricultural areas, where it searches for prey by probing mud and soft ground with its long, curved bill. It feeds on a wide range of aquatic and terrestrial animals and may forage both in shallow water and on dry ground. Compared with the similar Red-Naped Ibis, it is distinguished by the combination of features described above. Its preference for wetlands, marshes, flooded fields, riverbanks, grasslands, and agricultural areas also helps separate it from species that use different habitats. Its characteristic behaviour, including forages by walking slowly through shallow water or wet ground and probing with its long bill, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Black-HeadedIbis1.jpg",
    "quick_facts": {
        "family": "Threskiornithidae",
        "size": "65–75 cm",
        "weight": "1.3–1.6 kg",
        "wingspan": "Approximately 110–125 cm",
        "diet": "Fish, frogs, insects, crustaceans, worms, molluscs, and other small animals",
        "habitat": "Wetlands, marshes, flooded fields, riverbanks, grasslands, and agricultural areas",
        "behaviour": "Forages by walking slowly through shallow water or wet ground and probing with its long bill",
        "activity": "Diurnal",
        "nesting": "Builds a stick nest in trees, shrubs, or other vegetation, often in colonies",
        "breeding_season": "June to October in many parts of India",
        "clutch_size": "Usually 2–4 eggs",
        "call": "Generally quiet, producing low grunts and croaks around breeding colonies",
        "lifespan": "Several years in the wild",
        "conservation_status": "Near Threatened",
        "where_to_find": "India: widespread in the northern, central and eastern plains and parts of peninsular India, including Rajasthan, Gujarat, Uttar Pradesh, Bihar, West Bengal, Odisha, Madhya Pradesh, Maharashtra, Karnataka, Telangana, Andhra Pradesh and Tamil Nadu; Pakistan: Sindh and Punjab; Nepal: Terai; Bangladesh: widespread; Sri Lanka: local wetlands; Myanmar: local wetlands."
    }
},

{
    "name": "Black Kite",
    "scientific": "Milvus migrans",
    "description": "The Black Kite is a widespread bird of prey and one of the most familiar raptors around towns and cities in South Asia. Despite its common name, its plumage is generally dark brown rather than truly black, with a somewhat paler head and body. Its long wings and forked tail allow it to soar effortlessly on rising air currents. Black Kites are opportunistic feeders and consume carrion, insects, small animals, fish, and discarded food, allowing them to thrive in a wide variety of habitats. Compared with the similar Brahminy Kite, it is distinguished by the combination of features described above. Its preference for cities, farmland, wetlands, grasslands, open woodland, and rubbish sites also helps separate it from species that use different habitats. Its characteristic behaviour, including often soars for long periods and searches for food while flying; highly adaptable around human settlements, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "BlackKite1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "55–60 cm",
        "weight": "560–1000 g",
        "wingspan": "130–155 cm",
        "diet": "Carrion, insects, fish, small animals, and discarded food",
        "habitat": "Cities, farmland, wetlands, grasslands, open woodland, and rubbish sites",
        "behaviour": "Often soars for long periods and searches for food while flying; highly adaptable around human settlements",
        "activity": "Diurnal",
        "nesting": "Builds a large stick nest in trees, often reusing the same nesting area in successive years",
        "breeding_season": "December to April in much of India",
        "clutch_size": "Usually 2–3 eggs",
        "call": "High-pitched, drawn-out whistling or screaming calls",
        "lifespan": "Around 15–20 years or more in favourable conditions",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across most states, especially cities, farmland and open country; Pakistan: widespread; Nepal: widespread in lowlands and valleys; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: valleys and foothills; Myanmar: widespread; Europe, Africa, the Middle East and much of Asia: widespread, with regional migratory populations."
    }
},

{
    "name": "Black-Rumped Flameback",
    "scientific": "Dinopium benghalense",
    "description": "The Black-Rumped Flameback is a colourful woodpecker found across much of the Indian subcontinent. It has a bright golden-yellow back and wings, a black rump, and a striking red crest. It uses its powerful bill to hammer into tree trunks and branches in search of insects and their larvae. Its characteristic drumming and calls can reveal its presence even when it is hidden among foliage. The species occurs in forests, wooded areas, gardens, plantations, and urban environments with mature trees. Compared with the similar Indian Grey Hornbill, it is distinguished by the combination of features described above. Its preference for forests, woodland, plantations, gardens, orchards, and wooded urban areas also helps separate it from species that use different habitats. Its characteristic behaviour, including climbs tree trunks and branches while hammering into wood to locate insects; often drums on resonant surfaces, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Black-RumpedFlameback1.jpg",
    "quick_facts": {
        "family": "Picidae",
        "size": "26–30 cm",
        "weight": "90–130 g",
        "wingspan": "Approximately 40–45 cm",
        "diet": "Insects, beetle larvae, ants, termites, and other small invertebrates",
        "habitat": "Forests, woodland, plantations, gardens, orchards, and wooded urban areas",
        "behaviour": "Climbs tree trunks and branches while hammering into wood to locate insects; often drums on resonant surfaces",
        "activity": "Diurnal",
        "nesting": "Excavates a cavity in a tree trunk or branch, usually in dead or decaying wood",
        "breeding_season": "January to May",
        "clutch_size": "Usually 2–3 eggs",
        "call": "Loud, repeated calls accompanied by characteristic drumming on wood",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across much of the country, especially Rajasthan, Gujarat, Maharashtra, Madhya Pradesh, Odisha, West Bengal, Assam, Karnataka, Kerala, Tamil Nadu and Andhra Pradesh; Pakistan: local in the northwest; Nepal: Terai and lower hills; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar: widespread."
    }
},

{
    "name": "Black-Winged Kite",
    "scientific": "Elanus caeruleus",
    "description": "The Black-Winged Kite is a small and elegant bird of prey with a pale grey body, striking black shoulders and wing patches, and bright red eyes. It is often seen hovering almost motionless over grassland and agricultural fields while searching for prey below. Small rodents form an important part of its diet, although it also takes insects, lizards, and small birds. It favours open habitats and frequently perches on poles, wires, and isolated trees from which it can survey the ground. Compared with the similar Shikra, it is distinguished by the combination of features described above. Its preference for grasslands, farmland, open scrub, savannas, and other open country also helps separate it from species that use different habitats. Its characteristic behaviour, including frequently hovers almost motionless while hunting and may also perch on poles, wires, and isolated trees, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Black-WingedKite1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "30–35 cm",
        "weight": "200–300 g",
        "wingspan": "75–90 cm",
        "diet": "Small rodents, insects, lizards, and small birds",
        "habitat": "Grasslands, farmland, open scrub, savannas, and other open country",
        "behaviour": "Frequently hovers almost motionless while hunting and may also perch on poles, wires, and isolated trees",
        "activity": "Diurnal, with increased hunting activity during the cooler parts of the day",
        "nesting": "Builds a small stick nest in a tree, often using a relatively low branch",
        "breeding_season": "Varies by region; may breed during much of the year where conditions are favourable",
        "clutch_size": "Usually 3–5 eggs",
        "call": "Generally quiet, with soft whistles and squeaks around breeding areas",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread, including Rajasthan, Gujarat, Punjab, Haryana, Uttar Pradesh, Bihar, West Bengal, Madhya Pradesh, Maharashtra, Telangana, Andhra Pradesh, Karnataka and Tamil Nadu; Pakistan: widespread in plains; Nepal: Terai; Bangladesh: local; Sri Lanka: widespread; Africa, southern Europe and much of Asia: widespread in open country."
    }
},
{
    "name": "Brown-Headed Barbet",
    "scientific": "Psilopogon zeylanicus",
    "description": "The Brown-Headed Barbet is a large green barbet with a brown head and throat and a distinctive red patch around the eye. It is mainly arboreal and spends much of its time in trees, where it feeds on fruits and occasionally insects. Its repeated, resonant call is one of the characteristic sounds of wooded areas in the Indian subcontinent. It is commonly found in forests, gardens, plantations, orchards, and urban areas with mature trees. Compared with the similar Coppersmith Barbet, it is distinguished by the combination of features described above. Its preference for forests, gardens, orchards, plantations, and wooded urban areas also helps separate it from species that use different habitats. Its characteristic behaviour, including arboreal and usually solitary or found in pairs; spends much of its time feeding in trees, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Brown-HeadedBarbet1.jpg",
    "quick_facts": {
        "family": "Megalaimidae",
        "size": "30–34 cm",
        "weight": "180–250 g",
        "wingspan": "Approximately 45–50 cm",
        "diet": "Fruits, berries, figs, and occasionally insects",
        "habitat": "Forests, gardens, orchards, plantations, and wooded urban areas",
        "behaviour": "Arboreal and usually solitary or found in pairs; spends much of its time feeding in trees",
        "activity": "Diurnal",
        "nesting": "Excavates a cavity in a tree trunk or branch",
        "breeding_season": "January to June",
        "clutch_size": "2–4 eggs",
        "call": "Loud, repetitive and resonant calls repeated for long periods",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in northern, central and peninsular states, including Punjab, Haryana, Rajasthan, Uttar Pradesh, Bihar, West Bengal, Odisha, Madhya Pradesh, Maharashtra, Gujarat, Karnataka, Kerala, Tamil Nadu, Telangana and Andhra Pradesh; Pakistan: local; Nepal: Terai; Bangladesh: widespread; Sri Lanka: local; Bhutan: southern foothills."
    }
},

{
    "name": "Cattle Egret",
    "scientific": "Bubulcus ibis",
    "description": "The Cattle Egret is a compact white heron that is often seen following cattle and other large animals across fields. The birds take advantage of insects and other small creatures disturbed by the animals as they move through grass. During the breeding season, adults develop orange-buff plumage on the head, neck, and back. It is one of the most adaptable herons and is frequently found far from water. Compared with the similar Indian Pond Heron, it is distinguished by the combination of features described above. Its preference for grasslands, farmland, wetlands, pastures, and open countryside also helps separate it from species that use different habitats. Its characteristic behaviour, including often follows cattle, buffalo, and other large animals to catch disturbed prey, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "CattleEgret1.jpg",
    "quick_facts": {
        "family": "Ardeidae",
        "size": "46–56 cm",
        "weight": "270–512 g",
        "wingspan": "88–96 cm",
        "diet": "Insects, frogs, small reptiles, fish, and other small animals",
        "habitat": "Grasslands, farmland, wetlands, pastures, and open countryside",
        "behaviour": "Often follows cattle, buffalo, and other large animals to catch disturbed prey",
        "activity": "Diurnal",
        "nesting": "Builds a platform of sticks in trees or shrubs, usually in colonies",
        "breeding_season": "Varies by region, often during the monsoon or wet season",
        "clutch_size": "2–5 eggs",
        "call": "Harsh croaks and grating calls, especially around colonies",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across nearly all states and Union Territories; Pakistan: widespread; Nepal: Terai; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern valleys; Myanmar: widespread; Africa, Europe, the Middle East, Southeast Asia and Australia: widespread."
    }
},

{
    "name": "Common Hoopoe",
    "scientific": "Upupa epops",
    "description": "The Common Hoopoe is a distinctive bird with a long slender bill, boldly patterned black-and-white wings, a warm cinnamon body, and a prominent erectile crest. It usually forages on the ground, probing soil with its long bill for insects and other small prey. Hoopoes are often encountered in open landscapes and cultivated areas, where their striking appearance makes them easy to recognize. Compared with the similar Indian Roller, it is distinguished by the combination of features described above. Its preference for open woodland, farmland, grassland, gardens, and cultivated areas also helps separate it from species that use different habitats. Its characteristic behaviour, including forages mainly on the ground by probing soil and leaf litter with its bill, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "CommonHoopoe1.jpg",
    "quick_facts": {
        "family": "Upupidae",
        "size": "25–32 cm",
        "weight": "46–89 g",
        "wingspan": "44–48 cm",
        "diet": "Insects, larvae, worms, and other small invertebrates",
        "habitat": "Open woodland, farmland, grassland, gardens, and cultivated areas",
        "behaviour": "Forages mainly on the ground by probing soil and leaf litter with its bill",
        "activity": "Diurnal",
        "nesting": "Nests in tree cavities, holes in walls, rocks, or other sheltered cavities",
        "breeding_season": "February to June in much of its range",
        "clutch_size": "5–8 eggs",
        "call": "Distinctive soft, repeated 'oop-oop-oop' calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in open country across most states; Pakistan: widespread; Nepal: Terai and lower hills; Bangladesh: local; Sri Lanka: widespread; Bhutan: lower valleys; Myanmar: local; Europe, North Africa, the Middle East and much of Asia: widespread."
    }
},

{
    "name": "Common Kingfisher",
    "scientific": "Alcedo atthis",
    "description": "The Common Kingfisher is a small, brilliantly coloured kingfisher with vivid blue-green upperparts, orange underparts, and a long pointed bill. It usually sits quietly on a branch or other perch overlooking water before plunging rapidly to catch prey. Although widespread across Eurasia, it requires suitable clear water and fish-rich habitats for successful feeding. Compared with the similar White-Throated Kingfisher, it is distinguished by the combination of features described above. Its preference for rivers, streams, lakes, ponds, canals, and mangrove waterways also helps separate it from species that use different habitats. Its characteristic behaviour, including perches quietly near water and dives rapidly to catch prey, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "CommonKingfisher1.jpg",
    "quick_facts": {
        "family": "Alcedinidae",
        "size": "17–19 cm",
        "weight": "34–46 g",
        "wingspan": "24–26 cm",
        "diet": "Small fish, aquatic insects, crustaceans, tadpoles, and other small aquatic animals",
        "habitat": "Rivers, streams, lakes, ponds, canals, and mangrove waterways",
        "behaviour": "Perches quietly near water and dives rapidly to catch prey",
        "activity": "Diurnal",
        "nesting": "Excavates a tunnel in a sandy or earthen bank, ending in a nesting chamber",
        "breeding_season": "November to March in many parts of India",
        "clutch_size": "5–7 eggs",
        "call": "High-pitched, sharp whistling calls, especially during flight",
        "lifespan": "Around 2–7 years, with some individuals living longer",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread near freshwater and coastal habitats, including Kerala, Karnataka, Tamil Nadu, Maharashtra, Gujarat, West Bengal, Assam, Uttar Pradesh, Bihar and Odisha; Pakistan: northern and eastern wetlands; Nepal: lowlands and hills; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: valleys; Myanmar, Thailand, Laos, Cambodia, Vietnam and much of Europe and Asia: widespread."
    }
},

{
    "name": "Common Myna",
    "scientific": "Acridotheres tristis",
    "description": "The Common Myna is a highly adaptable bird with a brown body, black head, bright yellow eye patch, and yellow legs and bill. It thrives alongside people and can be found in towns, cities, farmland, gardens, and open countryside. Mynas are opportunistic feeders and eat a remarkably varied diet. They are social and vocal birds, often gathering in groups around feeding and roosting sites. Compared with the similar Indian Pied Starling, it is distinguished by the combination of features described above. Its preference for cities, villages, farmland, gardens, grasslands, and open woodland also helps separate it from species that use different habitats. Its characteristic behaviour, including highly social, adaptable, and often seen foraging on the ground in pairs or groups, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "CommonMyna1.jpg",
    "quick_facts": {
        "family": "Sturnidae",
        "size": "23–26 cm",
        "weight": "90–140 g",
        "wingspan": "120–140 cm",
        "diet": "Insects, fruits, seeds, grains, nectar, small reptiles, and food scraps",
        "habitat": "Cities, villages, farmland, gardens, grasslands, and open woodland",
        "behaviour": "Highly social, adaptable, and often seen foraging on the ground in pairs or groups",
        "activity": "Diurnal",
        "nesting": "Uses cavities in trees, buildings, walls, roofs, and other structures",
        "breeding_season": "March to September",
        "clutch_size": "4–5 eggs",
        "call": "Loud whistles, chatters, squawks, and varied imitations",
        "lifespan": "Around 4–12 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across most states; Pakistan: widespread; Nepal: widespread; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar: widespread; Thailand, Malaysia and Singapore: widespread, with introduced populations in many other regions."
    }
},

{
    "name": "Common Rosefinch",
    "scientific": "Carpodacus erythrinus",
    "description": "The Common Rosefinch is a medium-sized finch in which adult males develop a distinctive rosy-red head, breast, and rump. Females and immature birds are more subdued brown and heavily streaked. It feeds mainly on seeds, buds, berries, and other plant material and is generally associated with woodland edges, scrub, gardens, and open areas with suitable vegetation. Compared with the similar Common Stonechat, it is distinguished by the combination of features described above. Its preference for scrub, woodland edges, meadows, gardens, and mountain valleys also helps separate it from species that use different habitats. Its characteristic behaviour, including usually forages quietly in vegetation and may occur singly or in small groups, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "CommonRosefinch1.jpg",
    "quick_facts": {
        "family": "Fringillidae",
        "size": "13–15 cm",
        "weight": "20–25 g",
        "wingspan": "22–26 cm",
        "diet": "Seeds, buds, berries, grains, and plant material",
        "habitat": "Scrub, woodland edges, meadows, gardens, and mountain valleys",
        "behaviour": "Usually forages quietly in vegetation and may occur singly or in small groups",
        "activity": "Diurnal",
        "nesting": "Builds a cup-shaped nest in shrubs or low trees",
        "breeding_season": "May to August",
        "clutch_size": "4–6 eggs",
        "call": "Soft whistles and varied musical notes",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: Himalaya, including Jammu and Kashmir, Himachal Pradesh, Uttarakhand, Sikkim, Arunachal Pradesh and other northern hill areas, mainly seasonally; Pakistan: northern mountains; Nepal: mountains; Bhutan: mountains; Afghanistan and Central Asia: widespread breeding areas; China, Mongolia and Russia: widespread breeding range."
    }
},

{
    "name": "Common Sandpiper",
    "scientific": "Actitis hypoleucos",
    "description": "The Common Sandpiper is a small wader with brown upperparts, white underparts, and a characteristic habit of bobbing its tail and rear body while walking. It is usually found along the edges of water, where it runs quickly over mud, sand, and stones while searching for small invertebrates. Many individuals seen in India are winter visitors from northern breeding grounds. Compared with the similar Little Ringed Plover, it is distinguished by the combination of features described above. Its preference for riverbanks, lakeshores, ponds, mudflats, streams, and coastal areas also helps separate it from species that use different habitats. Its characteristic behaviour, including walks quickly along the water's edge while constantly bobbing its hindquarters, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "CommonSandpiper1.jpg",
    "quick_facts": {
        "family": "Scolopacidae",
        "size": "18–24 cm",
        "weight": "20–60 g",
        "wingspan": "32–35 cm",
        "diet": "Insects, worms, crustaceans, molluscs, and other small invertebrates",
        "habitat": "Riverbanks, lakeshores, ponds, mudflats, streams, and coastal areas",
        "behaviour": "Walks quickly along the water's edge while constantly bobbing its hindquarters",
        "activity": "Diurnal",
        "nesting": "Breeds on the ground near freshwater in its northern breeding range",
        "breeding_season": "May to August in breeding areas",
        "clutch_size": "3–5 eggs",
        "call": "Clear, high-pitched whistles, particularly during flight",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in winter, especially along rivers, lakes, reservoirs, coasts and wetlands; Pakistan: widespread; Nepal: lowlands and valleys; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: valleys; Myanmar, Thailand, Malaysia, Indonesia and Australia: widespread wintering areas; Europe and northern Asia: major breeding range."
    }
},

{
    "name": "Common Stonechat",
    "scientific": "Saxicola torquatus",
    "description": "The Common Stonechat is a small, upright songbird often seen perched prominently on shrubs, grass stems, fences, and other exposed points. Adult males typically have a dark head, orange breast, and pale collar, while females are more subdued. It feeds mainly on insects and other small invertebrates and prefers open habitats with scattered vegetation. Compared with the similar Pied Bushchat, it is distinguished by the combination of features described above. Its preference for grassland, scrub, farmland, marsh edges, and open countryside also helps separate it from species that use different habitats. Its characteristic behaviour, including perches prominently and makes short flights to catch insects before returning to a perch, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "CommonStonechat1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "11–13 cm",
        "weight": "12–17 g",
        "wingspan": "18–21 cm",
        "diet": "Insects, spiders, larvae, and other small invertebrates",
        "habitat": "Grassland, scrub, farmland, marsh edges, and open countryside",
        "behaviour": "Perches prominently and makes short flights to catch insects before returning to a perch",
        "activity": "Diurnal",
        "nesting": "Builds a cup-shaped nest low in dense vegetation or on the ground",
        "breeding_season": "March to August in breeding regions",
        "clutch_size": "4–6 eggs",
        "call": "Sharp clicking and chattering calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: mainly northern, western and highland regions, including Jammu and Kashmir, Himachal Pradesh, Uttarakhand, Rajasthan, Gujarat, Maharashtra and peninsular hill regions during appropriate seasons; Pakistan: widespread; Nepal: hills and lowlands; Bangladesh: wintering areas; Bhutan: widespread; Europe, Africa and Asia: widespread complex with regional forms."
    }
},

{
    "name": "Coppersmith Barbet",
    "scientific": "Psilopogon haemacephalus",
    "description": "The Coppersmith Barbet is a small, colourful green barbet with a red forehead, red throat, and yellow-and-blue facial markings. Its name comes from its repetitive call, which resembles the ringing sound of a coppersmith striking metal. It feeds mainly on fruits and berries and is commonly found in gardens, orchards, wooded parks, and areas with mature fruiting trees. Compared with the similar Brown-Headed Barbet, it is distinguished by the combination of features described above. Its preference for gardens, orchards, woodland, plantations, parks, and urban areas also helps separate it from species that use different habitats. Its characteristic behaviour, including arboreal and often remains hidden among foliage while feeding and calling, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "CoppersmithBarbet1.jpg",
    "quick_facts": {
        "family": "Megalaimidae",
        "size": "16–18 cm",
        "weight": "30–50 g",
        "wingspan": "28–32 cm",
        "diet": "Fruits, berries, figs, and occasionally insects",
        "habitat": "Gardens, orchards, woodland, plantations, parks, and urban areas",
        "behaviour": "Arboreal and often remains hidden among foliage while feeding and calling",
        "activity": "Diurnal",
        "nesting": "Excavates a cavity in a tree branch or trunk",
        "breeding_season": "February to June",
        "clutch_size": "2–4 eggs",
        "call": "Repeated metallic 'tuk-tuk-tuk' notes resembling a coppersmith at work",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across most states, especially Maharashtra, Gujarat, Rajasthan, Madhya Pradesh, Uttar Pradesh, Bihar, West Bengal, Odisha, Karnataka, Kerala, Tamil Nadu, Telangana and Andhra Pradesh; Pakistan: local; Nepal: Terai; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar and Thailand: widespread."
    }
},

{
    "name": "Crested Serpent Eagle",
    "scientific": "Spilornis cheela",
    "description": "The Crested Serpent Eagle is a medium-sized forest raptor with a broad wingspan, rounded wings, a prominent crest, and a distinctive yellow facial area. It feeds mainly on snakes and other reptiles but also takes frogs, small mammals, birds, and insects. Its loud, ringing call is often heard from forested hills before the bird itself is seen soaring overhead. Compared with the similar Shikra, it is distinguished by the combination of features described above. Its preference for forests, woodland, plantations, and forested hills also helps separate it from species that use different habitats. Its characteristic behaviour, including often perches quietly before taking short flights or soaring over forested areas, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "CrestedSerpentEagle1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "55–75 cm",
        "weight": "420–1800 g",
        "wingspan": "110–140 cm",
        "diet": "Snakes, lizards, frogs, small mammals, birds, and insects",
        "habitat": "Forests, woodland, plantations, and forested hills",
        "behaviour": "Often perches quietly before taking short flights or soaring over forested areas",
        "activity": "Diurnal",
        "nesting": "Builds a large stick nest in a tree",
        "breeding_season": "December to May",
        "clutch_size": "Usually 1 egg",
        "call": "Loud, repeated, high-pitched whistling or screaming calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in forested regions from the Himalaya and Northeast to central and peninsular India, including Uttarakhand, West Bengal, Assam, Meghalaya, Odisha, Chhattisgarh, Maharashtra, Goa, Karnataka, Kerala and Tamil Nadu; Pakistan: local foothills; Nepal: widespread in hills and lowlands; Bangladesh: widespread; Sri Lanka: widespread; Bhutan and Myanmar: widespread."
    }
},

{
    "name": "Great Hornbill",
    "scientific": "Buceros bicornis",
    "description": "The Great Hornbill is one of the most spectacular birds of the Indian subcontinent, recognized by its enormous yellow-and-black bill, large casque, black-and-white wings, and white tail. It is strongly associated with mature forests and depends heavily on large trees for nesting and feeding. Fruits form a major part of its diet, although it also takes small animals. Its powerful wingbeats produce a distinctive whooshing sound as it flies through the forest. Compared with the similar Malabar Pied Hornbill, it is distinguished by the combination of features described above. Its preference for mature tropical and subtropical forests also helps separate it from species that use different habitats. Its characteristic behaviour, including arboreal and usually found in pairs or small groups; capable of long flights between fruiting trees, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "GreatHornbill1.jpg",
    "quick_facts": {
        "family": "Bucerotidae",
        "size": "90–105 cm",
        "weight": "2.2–4 kg",
        "wingspan": "150–180 cm",
        "diet": "Fruits, figs, small mammals, birds, reptiles, and insects",
        "habitat": "Mature tropical and subtropical forests",
        "behaviour": "Arboreal and usually found in pairs or small groups; capable of long flights between fruiting trees",
        "activity": "Diurnal",
        "nesting": "Female seals herself inside a tree cavity, leaving a narrow opening through which the male feeds her",
        "breeding_season": "March to July",
        "clutch_size": "Usually 1–2 eggs",
        "call": "Loud barking, grunting, and honking calls",
        "lifespan": "Several decades are possible",
        "conservation_status": "Vulnerable",
        "where_to_find": "India: Western Ghats, Northeast and Himalayan foothills, especially Kerala, Karnataka, Goa, Maharashtra, Tamil Nadu, Assam, Arunachal Pradesh, Meghalaya, Nagaland, Manipur, Mizoram and Tripura; Nepal: southern foothills; Bhutan: southern forests; Bangladesh: very local; Myanmar, Thailand, Laos, Malaysia and Indonesia: forested regions."
    }
},

{
    "name": "Greater Coucal",
    "scientific": "Centropus sinensis",
    "description": "The Greater Coucal is a large, heavy cuckoo with a glossy black head and body, chestnut wings, and a long black tail. Unlike many cuckoos, it is a poor flyer and spends much of its time walking and hopping through dense vegetation. It feeds on insects, frogs, reptiles, eggs, nestlings, and various other small animals. Its deep, resonant calls are a familiar sound in scrub and gardens across India. Compared with the similar Asian Koel, it is distinguished by the combination of features described above. Its preference for scrub, grassland, gardens, plantations, wetlands, and woodland edges also helps separate it from species that use different habitats. Its characteristic behaviour, including usually walks through dense vegetation rather than flying long distances, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "GreaterCoucal1.jpg",
    "quick_facts": {
        "family": "Cuculidae",
        "size": "43–50 cm",
        "weight": "225–400 g",
        "wingspan": "Approximately 55–65 cm",
        "diet": "Insects, frogs, lizards, small snakes, eggs, nestlings, and small animals",
        "habitat": "Scrub, grassland, gardens, plantations, wetlands, and woodland edges",
        "behaviour": "Usually walks through dense vegetation rather than flying long distances",
        "activity": "Diurnal",
        "nesting": "Builds a large domed nest from grasses and leaves in dense vegetation",
        "breeding_season": "March to September",
        "clutch_size": "2–4 eggs",
        "call": "Deep, resonant 'coop-coop-coop' calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across most states, especially lowlands and agricultural regions; Pakistan: Sindh and Punjab; Nepal: Terai; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar, Thailand, Laos, Cambodia, Vietnam and Malaysia: widespread."
    }
},

{
    "name": "Indian Golden Oriole",
    "scientific": "Oriolus kundoo",
    "description": "The Indian Golden Oriole is a striking yellow-and-black songbird, with adult males showing brilliant golden-yellow plumage and bold black markings around the eye and wings. It spends much of its time in the canopy, feeding on fruits and insects. Its melodious calls are often heard before the bird is located among the leaves. Compared with the similar Black-Naped Oriole, it is distinguished by the combination of features described above. Its preference for woodland, forests, gardens, orchards, and plantations also helps separate it from species that use different habitats. Its characteristic behaviour, including arboreal and usually stays high in trees while feeding, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "IndianGoldenOriole1.jpg",
    "quick_facts": {
        "family": "Oriolidae",
        "size": "23–25 cm",
        "weight": "65–100 g",
        "wingspan": "Approximately 40–45 cm",
        "diet": "Fruits, berries, insects, caterpillars, and nectar",
        "habitat": "Woodland, forests, gardens, orchards, and plantations",
        "behaviour": "Arboreal and usually stays high in trees while feeding",
        "activity": "Diurnal",
        "nesting": "Builds a suspended cup-like nest in a tree fork",
        "breeding_season": "April to June",
        "clutch_size": "2–3 eggs",
        "call": "Clear, fluting and melodious whistles",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread, especially northern, central and peninsular states including Jammu and Kashmir, Himachal Pradesh, Uttarakhand, Rajasthan, Gujarat, Maharashtra, Madhya Pradesh, West Bengal, Odisha, Karnataka, Kerala and Tamil Nadu; Pakistan: local; Nepal: widespread in lowlands and hills; Bangladesh: local; Bhutan: foothills; Myanmar: local."
    }
},

{
    "name": "Indian Grey Hornbill",
    "scientific": "Ocyceros birostris",
    "description": "The Indian Grey Hornbill is a medium-sized hornbill with grey plumage, a long tail, and a dark bill with a casque. It is well adapted to open woodland and urban environments containing mature trees. Fruits form a major part of its diet, although it also catches insects and small animals. It is frequently seen flying between trees with steady, powerful wingbeats. Compared with the similar Malabar Pied Hornbill, it is distinguished by the combination of features described above. Its preference for open woodland, gardens, farmland, plantations, and urban areas with mature trees also helps separate it from species that use different habitats. Its characteristic behaviour, including arboreal and usually seen in pairs or small groups, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "IndianGreyHornbill1.jpg",
    "quick_facts": {
        "family": "Bucerotidae",
        "size": "61 cm",
        "weight": "350–450 g",
        "wingspan": "Approximately 80–90 cm",
        "diet": "Fruits, figs, insects, reptiles, and small birds",
        "habitat": "Open woodland, gardens, farmland, plantations, and urban areas with mature trees",
        "behaviour": "Arboreal and usually seen in pairs or small groups",
        "activity": "Diurnal",
        "nesting": "Female seals herself inside a tree cavity while the male supplies food",
        "breeding_season": "February to May",
        "clutch_size": "2–3 eggs",
        "call": "Loud squeals, grunts, and hornbill-like calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in drier woodland and open forest, including Rajasthan, Gujarat, Madhya Pradesh, Uttar Pradesh, Bihar, Maharashtra, Telangana, Andhra Pradesh, Karnataka, Tamil Nadu and parts of Odisha; Pakistan: local; Nepal: Terai; Bangladesh: local; Sri Lanka: local records; Bhutan: southern foothills."
    }
},

{
    "name": "Indian Openbill",
    "scientific": "Anastomus oscitans",
    "description": "The Indian Openbill is a medium-sized stork named for the noticeable gap between the upper and lower parts of its bill when it is closed. It is mainly associated with wetlands, flooded fields, marshes, and shallow waters, where it feeds largely on freshwater snails and other aquatic animals. It often forages in groups and can be seen walking through shallow water searching for prey. Compared with the similar Painted Stork, it is distinguished by the combination of features described above. Its preference for marshes, flooded fields, ponds, lakes, wetlands, and rice paddies also helps separate it from species that use different habitats. Its characteristic behaviour, including usually forages by walking through shallow water and probing for aquatic prey, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "IndianOpenbill1.jpg",
    "quick_facts": {
        "family": "Ciconiidae",
        "size": "68–81 cm",
        "weight": "1.2–1.6 kg",
        "wingspan": "Approximately 145–155 cm",
        "diet": "Freshwater snails, frogs, fish, insects, and other aquatic animals",
        "habitat": "Marshes, flooded fields, ponds, lakes, wetlands, and rice paddies",
        "behaviour": "Usually forages by walking through shallow water and probing for aquatic prey",
        "activity": "Diurnal",
        "nesting": "Builds a large stick nest in trees, often in colonies",
        "breeding_season": "July to October in much of India",
        "clutch_size": "2–4 eggs",
        "call": "Generally quiet away from colonies, with bill-clattering and other sounds at nesting sites",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in wetlands and agricultural areas, especially Uttar Pradesh, Bihar, West Bengal, Assam, Odisha, Jharkhand, Chhattisgarh, Madhya Pradesh, Maharashtra, Telangana, Andhra Pradesh and Karnataka; Pakistan: local; Nepal: Terai; Bangladesh: widespread; Sri Lanka: local; Myanmar: widespread."
    }
},

{
    "name": "Indian Peafowl",
    "scientific": "Pavo cristatus",
    "description": "The Indian Peafowl is one of the most recognizable birds of the Indian subcontinent. Adult males have an elaborate train of elongated upper-tail coverts decorated with eye-like markings, while females are smaller and more subdued in colour. Peafowl feed on seeds, fruits, insects, reptiles, and other food and are highly adaptable. Males display their train during courtship and produce loud calls that carry over considerable distances. Compared with the similar Indian Pitta, it is distinguished by the combination of features described above. Its preference for open woodland, scrub, farmland, grassland, villages, and parks also helps separate it from species that use different habitats. Its characteristic behaviour, including usually forages on the ground and roosts in trees at night, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "IndianPeafowl1.jpg",
    "quick_facts": {
        "family": "Phasianidae",
        "size": "90–230 cm including male's train",
        "weight": "2.7–6 kg",
        "wingspan": "Approximately 130–160 cm",
        "diet": "Seeds, grains, fruits, insects, reptiles, small animals, and plant matter",
        "habitat": "Open woodland, scrub, farmland, grassland, villages, and parks",
        "behaviour": "Usually forages on the ground and roosts in trees at night",
        "activity": "Diurnal",
        "nesting": "Scrapes a shallow nest on the ground, usually concealed in vegetation",
        "breeding_season": "April to September, varying with rainfall",
        "clutch_size": "4–8 eggs",
        "call": "Loud, harsh and far-carrying calls",
        "lifespan": "Around 10–20 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across most states, especially Rajasthan, Gujarat, Uttar Pradesh, Madhya Pradesh, Maharashtra, Karnataka, Tamil Nadu, Kerala, Telangana, Andhra Pradesh, Odisha and West Bengal; Pakistan: Punjab and Sindh; Nepal: Terai; Bangladesh: local; Sri Lanka: widespread; Bhutan: southern foothills."
    }
},

{
    "name": "Indian Pitta",
    "scientific": "Pitta brachyura",
    "description": "The Indian Pitta is a brightly coloured forest-floor bird with a green back, blue crown, black eye stripe, buff underparts, and red or orange lower body. It is generally shy and spends much of its time moving through leaf litter in search of prey. Its distinctive two-note call is often heard from dense vegetation. The species is especially associated with moist forests and woodland during its breeding range and can be encountered more widely during migration. Compared with the similar Indian Roller, it is distinguished by the combination of features described above. Its preference for moist forest, woodland, scrub, plantations, and leafy gardens also helps separate it from species that use different habitats. Its characteristic behaviour, including forages mainly on the ground, tossing aside leaf litter while searching for prey, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "IndianPitta1.jpg",
    "quick_facts": {
        "family": "Pittidae",
        "size": "15–18 cm",
        "weight": "40–60 g",
        "wingspan": "25–28 cm",
        "diet": "Insects, worms, snails, spiders, and other small invertebrates",
        "habitat": "Moist forest, woodland, scrub, plantations, and leafy gardens",
        "behaviour": "Forages mainly on the ground, tossing aside leaf litter while searching for prey",
        "activity": "Diurnal",
        "nesting": "Builds a roughly spherical nest of leaves and vegetation close to the ground",
        "breeding_season": "June to August in much of India",
        "clutch_size": "4–6 eggs",
        "call": "Distinctive repeated two-note whistle",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: breeding populations in Himalayan foothills and peninsular forests, including Uttarakhand, West Bengal, Odisha, Jharkhand, Chhattisgarh, Maharashtra, Karnataka, Goa, Kerala, Tamil Nadu, Telangana and Andhra Pradesh; Nepal: foothills; Bangladesh: local; Sri Lanka: wintering populations; Bhutan: southern foothills; Myanmar: local."
    }
},

{
    "name": "Indian Roller",
    "scientific": "Coracias benghalensis",
    "description": "The Indian Roller is a striking blue and brown bird commonly seen perched on wires, poles, trees, and other exposed locations. Its wings display brilliant shades of blue when it flies, making it especially spectacular in flight. It hunts insects and small animals from a perch and is common in open country, farmland, grassland, and urban areas. During courtship and territorial disputes, it performs dramatic rolling and tumbling flights. Compared with the similar Common Hoopoe, it is distinguished by the combination of features described above. Its preference for open woodland, farmland, grassland, roadside areas, and towns also helps separate it from species that use different habitats. Its characteristic behaviour, including perches in exposed locations and drops down to capture prey from the ground, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "IndianRoller1.jpg",
    "quick_facts": {
        "family": "Coraciidae",
        "size": "30–34 cm",
        "weight": "130–180 g",
        "wingspan": "65–75 cm",
        "diet": "Insects, frogs, lizards, small birds, and other small animals",
        "habitat": "Open woodland, farmland, grassland, roadside areas, and towns",
        "behaviour": "Perches in exposed locations and drops down to capture prey from the ground",
        "activity": "Diurnal",
        "nesting": "Uses cavities in trees, buildings, cliffs, or other structures",
        "breeding_season": "March to June",
        "clutch_size": "3–5 eggs",
        "call": "Harsh, chattering and crow-like calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across most states, especially open country and farmland; Pakistan: widespread; Nepal: Terai; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar: local; Iran and other parts of the Indian subcontinent: local populations."
    }
},

{
    "name": "Indian Silverbill",
    "scientific": "Euodice malabarica",
    "description": "The Indian Silverbill is a small finch-like munia with a pale brown body, whitish underparts, a blackish bill, and a distinctive pale rump. It is usually found in dry grasslands, scrub, agricultural areas, and open woodland, where it feeds mainly on grass seeds. It is social and often travels in small flocks, particularly outside the breeding season. Compared with the similar Scaly-Breasted Munia, it is distinguished by the combination of features described above. Its preference for grassland, scrub, farmland, dry woodland, and open country also helps separate it from species that use different habitats. Its characteristic behaviour, including social and often seen in small flocks feeding on the ground or among grasses, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "IndianSilverbill1.jpg",
    "quick_facts": {
        "family": "Estrildidae",
        "size": "11–12 cm",
        "weight": "10–15 g",
        "wingspan": "16–18 cm",
        "diet": "Grass seeds, grains, and other small seeds",
        "habitat": "Grassland, scrub, farmland, dry woodland, and open country",
        "behaviour": "Social and often seen in small flocks feeding on the ground or among grasses",
        "activity": "Diurnal",
        "nesting": "Builds a rounded grass nest in bushes, grass clumps, or other vegetation",
        "breeding_season": "Throughout much of the year, depending on rainfall",
        "clutch_size": "4–8 eggs",
        "call": "Soft chirps and twittering calls",
        "lifespan": "Several years in captivity; shorter on average in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in dry and semi-arid regions, including Rajasthan, Gujarat, Maharashtra, Madhya Pradesh, Karnataka, Telangana, Andhra Pradesh, Tamil Nadu and parts of Uttar Pradesh; Pakistan: widespread in dry country; Nepal: Terai; Bangladesh: local; Sri Lanka: local; Middle East: local populations."
    }
},

{
    "name": "Jungle Babbler",
    "scientific": "Argya striata",
    "description": "The Jungle Babbler is a social, noisy bird commonly seen moving through vegetation in small groups. Its grey-brown plumage is relatively plain, but its lively behaviour and constant chatter make it easy to recognize. Groups forage together on the ground and in shrubs, searching for insects, seeds, fruit, and other food. They are common in gardens, woodland, scrub, farmland, and urban areas. Compared with the similar Puff-Throated Babbler, it is distinguished by the combination of features described above. Its preference for scrub, gardens, woodland, farmland, parks, and urban areas also helps separate it from species that use different habitats. Its characteristic behaviour, including highly social and usually travels in noisy groups, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "JungleBabbler1.jpg",
    "quick_facts": {
        "family": "Leiothrichidae",
        "size": "23–25 cm",
        "weight": "60–85 g",
        "wingspan": "Approximately 30–35 cm",
        "diet": "Insects, fruits, seeds, grains, and small invertebrates",
        "habitat": "Scrub, gardens, woodland, farmland, parks, and urban areas",
        "behaviour": "Highly social and usually travels in noisy groups",
        "activity": "Diurnal",
        "nesting": "Builds a cup-shaped nest in dense shrubs or low trees",
        "breeding_season": "February to September",
        "clutch_size": "2–4 eggs",
        "call": "Loud, continuous chattering and harsh contact calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across northern, central and peninsular states, especially Uttar Pradesh, Bihar, Rajasthan, Gujarat, Madhya Pradesh, Maharashtra, Karnataka, Telangana, Andhra Pradesh, Tamil Nadu and Kerala; Nepal: Terai and lower hills; Bangladesh: local; Sri Lanka: local; Pakistan: eastern lowlands."
    }
},

{
    "name": "Little Cormorant",
    "scientific": "Microcarbo niger",
    "description": "The Little Cormorant is a small dark waterbird that is common across South Asia. It spends much of its time in or around freshwater, diving beneath the surface to catch fish and other aquatic prey. After feeding, it often perches with its wings spread to dry its plumage. It is highly adaptable and occurs in ponds, lakes, rivers, canals, marshes, and flooded fields. Compared with the similar Indian Cormorant, it is distinguished by the combination of features described above. Its preference for lakes, ponds, rivers, canals, marshes, reservoirs, and flooded fields also helps separate it from species that use different habitats. Its characteristic behaviour, including excellent underwater swimmer that dives repeatedly to catch prey, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "LittleCormorant1.jpg",
    "quick_facts": {
        "family": "Phalacrocoracidae",
        "size": "55–60 cm",
        "weight": "430–800 g",
        "wingspan": "85–95 cm",
        "diet": "Fish, frogs, crustaceans, and other aquatic animals",
        "habitat": "Lakes, ponds, rivers, canals, marshes, reservoirs, and flooded fields",
        "behaviour": "Excellent underwater swimmer that dives repeatedly to catch prey",
        "activity": "Diurnal",
        "nesting": "Builds a platform of sticks in trees, shrubs, or sometimes reed beds, usually in colonies",
        "breeding_season": "Varies with region and rainfall",
        "clutch_size": "3–5 eggs",
        "call": "Usually quiet away from colonies; produces croaks and grunts at nesting sites",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across nearly all states with suitable wetlands; Pakistan: Sindh and Punjab; Nepal: lowlands; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: valleys; Myanmar, Thailand, Laos, Cambodia and Vietnam: widespread."
    }
},

{
    "name": "Little Egret",
    "scientific": "Egretta garzetta",
    "description": "The Little Egret is a graceful white heron with a slender black bill, black legs, and bright yellow feet. It usually forages in shallow water, moving carefully or stirring the bottom to flush out small prey. During the breeding season, adults develop delicate plumes on the head and back. It occurs in freshwater and coastal wetlands and is often seen alone or in small groups. Compared with the similar Cattle Egret, it is distinguished by the combination of features described above. Its preference for marshes, ponds, rivers, lakes, estuaries, mudflats, and coastal wetlands also helps separate it from species that use different habitats. Its characteristic behaviour, including wades through shallow water and uses quick movements to catch prey, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "LittleEgret1.jpg",
    "quick_facts": {
        "family": "Ardeidae",
        "size": "55–65 cm",
        "weight": "250–350 g",
        "wingspan": "88–106 cm",
        "diet": "Fish, frogs, crustaceans, insects, and small aquatic animals",
        "habitat": "Marshes, ponds, rivers, lakes, estuaries, mudflats, and coastal wetlands",
        "behaviour": "Wades through shallow water and uses quick movements to catch prey",
        "activity": "Diurnal",
        "nesting": "Builds a stick nest in trees, shrubs, reed beds, or colonies",
        "breeding_season": "Varies by region, often during the wet season",
        "clutch_size": "3–5 eggs",
        "call": "Generally quiet, with harsh croaks around breeding colonies",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across nearly all states and coastal regions; Pakistan: widespread; Nepal: Terai; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern valleys; Myanmar, Thailand, Malaysia, Indonesia, Africa, Europe and Australia: widespread."
    }
},

{
    "name": "Little Ringed Plover",
    "scientific": "Charadrius dubius",
    "description": "The Little Ringed Plover is a small wader with a distinctive black-and-white head pattern, yellow eye-ring, and yellowish legs. It is usually found near freshwater, especially along exposed muddy or sandy shores. It runs rapidly across open ground before stopping to pick small prey from the surface. Many birds encountered in parts of India are winter visitors. Compared with the similar Common Sandpiper, it is distinguished by the combination of features described above. Its preference for mudflats, sandy shores, riverbanks, lake edges, gravel beds, and wetlands also helps separate it from species that use different habitats. Its characteristic behaviour, including runs quickly over open ground, frequently stopping to pick prey from the surface, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Little-RingedPlover1.jpg",
    "quick_facts": {
        "family": "Charadriidae",
        "size": "14–15 cm",
        "weight": "30–55 g",
        "wingspan": "35–40 cm",
        "diet": "Insects, worms, crustaceans, and other small invertebrates",
        "habitat": "Mudflats, sandy shores, riverbanks, lake edges, gravel beds, and wetlands",
        "behaviour": "Runs quickly over open ground, frequently stopping to pick prey from the surface",
        "activity": "Diurnal",
        "nesting": "Makes a shallow scrape on bare ground, usually among stones or gravel",
        "breeding_season": "April to July in breeding areas",
        "clutch_size": "3–4 eggs",
        "call": "Soft, high-pitched whistles and piping calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in suitable freshwater and riverine habitats, including Rajasthan, Gujarat, Uttar Pradesh, Bihar, West Bengal, Odisha, Madhya Pradesh, Maharashtra, Karnataka, Telangana, Andhra Pradesh and Tamil Nadu; Pakistan: widespread; Nepal: lowlands and valleys; Bangladesh: widespread; Sri Lanka: wintering areas; Europe and Asia: widespread breeding range."
    }
},

{
    "name": "Oriental Magpie-Robin",
    "scientific": "Copsychus saularis",
    "description": "The Oriental Magpie-Robin is a familiar black-and-white songbird of gardens, forests, villages, and urban areas. Males are glossy black with white wing and tail markings, while females are generally greyish. It is an active ground and low-level forager that eats insects and other small invertebrates. Males are especially well known for their varied and melodious songs. Compared with the similar Indian Robin, it is distinguished by the combination of features described above. Its preference for gardens, forests, woodland, plantations, parks, and villages also helps separate it from species that use different habitats. Its characteristic behaviour, including active and territorial; frequently forages on the ground and low branches, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "OrientalMagpie-Robin1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "19–21 cm",
        "weight": "30–45 g",
        "wingspan": "Approximately 25–30 cm",
        "diet": "Insects, spiders, worms, small reptiles, and other invertebrates",
        "habitat": "Gardens, forests, woodland, plantations, parks, and villages",
        "behaviour": "Active and territorial; frequently forages on the ground and low branches",
        "activity": "Diurnal",
        "nesting": "Uses cavities, holes, pipes, boxes, and other sheltered spaces",
        "breeding_season": "March to August",
        "clutch_size": "3–5 eggs",
        "call": "Rich, varied and melodious song with many imitations and phrases",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across most states; Pakistan: eastern regions; Nepal: widespread; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar, Thailand, Laos, Cambodia, Vietnam, Malaysia and Indonesia: widespread."
    }
},

{
    "name": "Painted Stork",
    "scientific": "Mycteria leucocephala",
    "description": "The Painted Stork is a large wading bird with a white body, black wing markings, a pinkish head and neck, and a long yellow-orange bill. It often feeds in shallow water by sweeping its partly open bill from side to side to detect fish and other aquatic animals. It is commonly associated with wetlands, lakes, marshes, and flooded fields and frequently nests in large colonies. Compared with the similar Woolly-Necked Stork, it is distinguished by the combination of features described above. Its preference for wetlands, lakes, marshes, flooded fields, rivers, and shallow water bodies also helps separate it from species that use different habitats. Its characteristic behaviour, including forages by sweeping its bill through shallow water and often feeds in groups, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "PaintedStork1.jpg",
    "quick_facts": {
        "family": "Ciconiidae",
        "size": "93–102 cm",
        "weight": "2–3.5 kg",
        "wingspan": "150–160 cm",
        "diet": "Fish, frogs, crustaceans, insects, and other aquatic animals",
        "habitat": "Wetlands, lakes, marshes, flooded fields, rivers, and shallow water bodies",
        "behaviour": "Forages by sweeping its bill through shallow water and often feeds in groups",
        "activity": "Diurnal",
        "nesting": "Builds large stick nests in trees, usually in colonies",
        "breeding_season": "August to October in many parts of India",
        "clutch_size": "2–5 eggs",
        "call": "Generally quiet, with bill-clattering and soft sounds around colonies",
        "lifespan": "Several years in the wild",
        "conservation_status": "Near Threatened",
        "where_to_find": "India: wetlands and floodplains across northern, central and peninsular states, especially Rajasthan, Gujarat, Uttar Pradesh, Bihar, West Bengal, Odisha, Madhya Pradesh, Maharashtra, Karnataka, Telangana, Andhra Pradesh and Tamil Nadu; Pakistan: Sindh and Punjab; Nepal: Terai; Bangladesh: widespread; Sri Lanka: local; Myanmar: local."
    }
},

{
    "name": "Purple-Rumped Sunbird",
    "scientific": "Leptocoma zeylonica",
    "description": "The Purple-Rumped Sunbird is a tiny nectar-feeding bird found mainly in the Indian subcontinent. Breeding males display brilliant purple, blue, green, and maroon plumage, while females are much more subdued. It feeds on nectar from flowers and also takes small insects, particularly when feeding young. Its small size and rapid movements make it easy to miss despite its vivid colours. Compared with the similar Purple Sunbird, it is distinguished by the combination of features described above. Its preference for gardens, forests, plantations, scrub, and flowering trees also helps separate it from species that use different habitats. Its characteristic behaviour, including highly active and frequently moves between flowers while feeding, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Purple-RumpedSunbird1.jpg",
    "quick_facts": {
        "family": "Nectariniidae",
        "size": "10–12 cm",
        "weight": "6–8 g",
        "wingspan": "13–15 cm",
        "diet": "Nectar, small insects, spiders, and other tiny invertebrates",
        "habitat": "Gardens, forests, plantations, scrub, and flowering trees",
        "behaviour": "Highly active and frequently moves between flowers while feeding",
        "activity": "Diurnal",
        "nesting": "Builds a hanging pouch-like nest from plant fibres, grass, and spider webs",
        "breeding_season": "November to March in many areas, with regional variation",
        "clutch_size": "Usually 2 eggs",
        "call": "High-pitched, rapid and twittering calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: mainly peninsular and western India, especially Maharashtra, Goa, Karnataka, Kerala, Tamil Nadu, Andhra Pradesh, Telangana and Gujarat; Sri Lanka: widespread; Pakistan: local; Bangladesh: local; Nepal: southern foothills; Bhutan: local."
    }
},

{
    "name": "Purple Sunbird",
    "scientific": "Cinnyris asiaticus",
    "description": "The Purple Sunbird is a tiny, active nectar feeder and one of the most familiar sunbirds in India. Breeding males can appear almost black in ordinary light but show brilliant purple, blue, and green iridescence when illuminated. Females are olive-yellow and much less conspicuous. The species is highly adaptable and occurs in gardens, forests, scrub, plantations, and cities wherever flowering plants provide food. Compared with the similar Purple-Rumped Sunbird, it is distinguished by the combination of features described above. Its preference for gardens, scrub, woodland, plantations, parks, and urban areas also helps separate it from species that use different habitats. Its characteristic behaviour, including active and agile; frequently hovers or perches beside flowers while feeding, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "PurpleSunbird1.jpg",
    "quick_facts": {
        "family": "Nectariniidae",
        "size": "10–11 cm",
        "weight": "7–10 g",
        "wingspan": "13–15 cm",
        "diet": "Nectar, insects, spiders, and other small invertebrates",
        "habitat": "Gardens, scrub, woodland, plantations, parks, and urban areas",
        "behaviour": "Active and agile; frequently hovers or perches beside flowers while feeding",
        "activity": "Diurnal",
        "nesting": "Builds a hanging pouch-shaped nest from fibres, grass, and spider webs",
        "breeding_season": "Throughout much of the year, depending on local conditions",
        "clutch_size": "Usually 2 eggs",
        "call": "Rapid, high-pitched twittering and chirping",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across most states, especially gardens, scrub and woodland; Pakistan: widespread; Nepal: Terai and lower hills; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar, Thailand, Laos and Cambodia: widespread."
    }
},

{
    "name": "Red-Vented Bulbul",
    "scientific": "Pycnonotus cafer",
    "description": "The Red-Vented Bulbul is a familiar and adaptable songbird with a black head and crest, brown body, white rump patch, and distinctive red vent. It occurs in almost every type of semi-open habitat, including gardens, farmland, scrub, parks, and cities. It feeds on fruits, berries, nectar, insects, and other foods and is often seen moving actively through bushes and trees. Compared with the similar Red-Whiskered Bulbul, it is distinguished by the combination of features described above. Its preference for gardens, scrub, woodland, farmland, parks, and urban areas also helps separate it from species that use different habitats. Its characteristic behaviour, including active and social; often forages in pairs or small groups, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Red-VentedBulbul1.jpg",
    "quick_facts": {
        "family": "Pycnonotidae",
        "size": "19–21 cm",
        "weight": "30–45 g",
        "wingspan": "26–30 cm",
        "diet": "Fruits, berries, nectar, insects, seeds, and flower buds",
        "habitat": "Gardens, scrub, woodland, farmland, parks, and urban areas",
        "behaviour": "Active and social; often forages in pairs or small groups",
        "activity": "Diurnal",
        "nesting": "Builds a small cup-shaped nest in bushes, shrubs, or low trees",
        "breeding_season": "February to September",
        "clutch_size": "2–3 eggs",
        "call": "Varied musical, chattering, and sharp calls",
        "lifespan": "Around 10 years in favourable conditions",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across most states; Pakistan: widespread in settled areas; Nepal: widespread; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar, Thailand, Laos, Cambodia and Vietnam: widespread; introduced populations occur in several other regions."
    }
},

{
    "name": "Red-Whiskered Bulbul",
    "scientific": "Pycnonotus jocosus",
    "description": "The Red-Whiskered Bulbul is an attractive crested bulbul with a black head, white cheek, red ear patch, brown back, and red vent. It is an energetic bird that feeds on fruit, nectar, and insects and is often found in gardens, forest edges, plantations, and scrub. Its pointed crest and red facial markings make it particularly distinctive. Compared with the similar Red-Vented Bulbul, it is distinguished by the combination of features described above. Its preference for gardens, scrub, woodland edges, plantations, and forests also helps separate it from species that use different habitats. Its characteristic behaviour, including active and social, often moving through vegetation in pairs or small groups, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Red-WhiskeredBulbul1.jpg",
    "quick_facts": {
        "family": "Pycnonotidae",
        "size": "20–22 cm",
        "weight": "23–42 g",
        "wingspan": "26–29 cm",
        "diet": "Fruits, berries, nectar, insects, and flower buds",
        "habitat": "Gardens, scrub, woodland edges, plantations, and forests",
        "behaviour": "Active and social, often moving through vegetation in pairs or small groups",
        "activity": "Diurnal",
        "nesting": "Builds a cup-shaped nest in shrubs, bushes, or small trees",
        "breeding_season": "January to August, varying by region",
        "clutch_size": "2–3 eggs",
        "call": "Clear whistles, chattering notes, and varied calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in wooded and garden habitats, especially peninsular, central and eastern states; Pakistan: local Sindh populations; Nepal: Terai; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar, Thailand, Laos, Cambodia, Vietnam, Malaysia and Indonesia: widespread."
    }
},

{
    "name": "Red-Wattled Lapwing",
    "scientific": "Vanellus indicus",
    "description": "The Red-Wattled Lapwing is a large, conspicuous wader with a black head and breast, white underparts, brown wings, yellow legs, and a distinctive red fleshy wattle at the base of the bill. It is commonly found in open habitats near water but can also live far from wetlands. Its loud alarm call is one of the characteristic sounds of the Indian countryside, especially at night. Compared with the similar Indian Courser, it is distinguished by the combination of features described above. Its preference for open fields, wetlands, riverbanks, grasslands, farmland, and lake margins also helps separate it from species that use different habitats. Its characteristic behaviour, including alert and territorial; gives loud alarm calls when predators or people approach, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Red-WattledLapwing1.jpg",
    "quick_facts": {
        "family": "Charadriidae",
        "size": "32–35 cm",
        "weight": "200–300 g",
        "wingspan": "75–85 cm",
        "diet": "Insects, worms, molluscs, seeds, and other small invertebrates",
        "habitat": "Open fields, wetlands, riverbanks, grasslands, farmland, and lake margins",
        "behaviour": "Alert and territorial; gives loud alarm calls when predators or people approach",
        "activity": "Diurnal and often active at night",
        "nesting": "Makes a shallow scrape on open ground, usually with little nest material",
        "breeding_season": "March to August",
        "clutch_size": "Usually 3–4 eggs",
        "call": "Extremely loud, repeated 'did-he-do-it' style alarm calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across most states; Pakistan: widespread; Nepal: Terai; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern valleys; Myanmar, Thailand, Laos and Cambodia: widespread."
    }
},

{
    "name": "Rose-Ringed Parakeet",
    "scientific": "Psittacula krameri",
    "description": "The Rose-Ringed Parakeet is a familiar bright-green parakeet with a long pointed tail and large red bill. Adult males develop a narrow dark and rose-coloured neck ring, while females and young birds lack the complete male pattern. It is highly adaptable and thrives in gardens, farmland, forests, plantations, and cities. Large noisy flocks are often seen flying between roosting and feeding areas. Compared with the similar Alexandrine Parakeet, it is distinguished by the combination of features described above. Its preference for woodland, farmland, gardens, plantations, parks, and cities also helps separate it from species that use different habitats. Its characteristic behaviour, including highly social and often gathers in noisy flocks, particularly at roosts, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Rose-RingedParakeet1.jpg",
    "quick_facts": {
        "family": "Psittaculidae",
        "size": "40–42 cm",
        "weight": "95–140 g",
        "wingspan": "42–48 cm",
        "diet": "Fruits, seeds, grains, flowers, buds, and nectar",
        "habitat": "Woodland, farmland, gardens, plantations, parks, and cities",
        "behaviour": "Highly social and often gathers in noisy flocks, particularly at roosts",
        "activity": "Diurnal",
        "nesting": "Uses cavities in trees, buildings, walls, and other structures",
        "breeding_season": "December to May",
        "clutch_size": "3–5 eggs",
        "call": "Loud, harsh and repetitive screeches",
        "lifespan": "Around 15–20 years in favourable conditions",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across most states; Pakistan: widespread; Nepal: Terai and lower hills; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar and Afghanistan: local; introduced populations occur across Europe, the Middle East and elsewhere."
    }
},

{
    "name": "Rufous Treepie",
    "scientific": "Dendrocitta vagabunda",
    "description": "The Rufous Treepie is a long-tailed member of the crow family with a striking combination of rufous, grey, black, and white plumage. It is an active and opportunistic bird that moves through trees and often visits the ground in search of food. Its varied diet includes fruits, insects, small animals, eggs, and carrion. It is a common inhabitant of forests, gardens, farmland, and urban areas. Compared with the similar Common Myna, it is distinguished by the combination of features described above. Its preference for forests, woodland, farmland, gardens, plantations, and towns also helps separate it from species that use different habitats. Its characteristic behaviour, including active, curious, and usually seen alone, in pairs, or small family groups, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "RufousTreepie1.jpg",
    "quick_facts": {
        "family": "Corvidae",
        "size": "45–50 cm",
        "weight": "90–130 g",
        "wingspan": "Approximately 55–65 cm",
        "diet": "Fruits, insects, small reptiles, eggs, nestlings, carrion, and food scraps",
        "habitat": "Forests, woodland, farmland, gardens, plantations, and towns",
        "behaviour": "Active, curious, and usually seen alone, in pairs, or small family groups",
        "activity": "Diurnal",
        "nesting": "Builds a shallow stick nest in trees",
        "breeding_season": "April to June",
        "clutch_size": "2–5 eggs",
        "call": "Loud, varied and distinctive chattering or metallic calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across northern, central and peninsular states, especially Rajasthan, Gujarat, Uttar Pradesh, Bihar, West Bengal, Odisha, Madhya Pradesh, Maharashtra, Karnataka, Kerala, Tamil Nadu, Telangana and Andhra Pradesh; Pakistan: eastern regions; Nepal: Terai; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills."
    }
},

{
    "name": "Scaly-Breasted Munia",
    "scientific": "Lonchura punctulata",
    "description": "The Scaly-Breasted Munia is a small, compact finch-like bird with a chestnut head and upperparts and strongly scaled markings across the pale breast and belly. It feeds mainly on grass seeds and grains and is often found in flocks in grassland and agricultural areas. It is a common bird of fields, scrub, gardens, and areas of tall grass. Compared with the similar White-Rumped Munia, it is distinguished by the combination of features described above. Its preference for grassland, farmland, scrub, gardens, and reed beds also helps separate it from species that use different habitats. Its characteristic behaviour, including highly social and often forms flocks while feeding on the ground or in grasses, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Scaly-BreastedMunia1.jpg",
    "quick_facts": {
        "family": "Estrildidae",
        "size": "11–12 cm",
        "weight": "10–15 g",
        "wingspan": "16–18 cm",
        "diet": "Grass seeds, grains, and other small seeds",
        "habitat": "Grassland, farmland, scrub, gardens, and reed beds",
        "behaviour": "Highly social and often forms flocks while feeding on the ground or in grasses",
        "activity": "Diurnal",
        "nesting": "Builds a spherical or dome-shaped nest from grass and plant fibres",
        "breeding_season": "Throughout much of the year, especially after rains",
        "clutch_size": "4–8 eggs",
        "call": "Soft chirps, whistles, and twittering calls",
        "lifespan": "Several years in captivity and generally shorter in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across most states; Pakistan: Punjab and Sindh; Nepal: Terai; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar, Thailand, Laos, Cambodia, Vietnam, Malaysia and Indonesia: widespread."
    }
},

{
    "name": "Shikra",
    "scientific": "Accipiter badius",
    "description": "The Shikra is a small woodland hawk with short rounded wings, a long tail, and sharp talons. Adults commonly show grey upperparts and barred underparts, while females are generally larger than males. It is an agile hunter that catches small birds, lizards, rodents, frogs, and insects. Shikras are adaptable and can live in forests, farmland, gardens, plantations, and cities with sufficient tree cover. Compared with the similar Black-Winged Kite, it is distinguished by the combination of features described above. Its preference for woodland, forests, farmland, plantations, gardens, and urban areas also helps separate it from species that use different habitats. Its characteristic behaviour, including fast and agile hunter that often uses surprise attacks from cover, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Shikra1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "26–30 cm",
        "weight": "90–250 g",
        "wingspan": "50–60 cm",
        "diet": "Small birds, lizards, rodents, frogs, insects, and other small animals",
        "habitat": "Woodland, forests, farmland, plantations, gardens, and urban areas",
        "behaviour": "Fast and agile hunter that often uses surprise attacks from cover",
        "activity": "Diurnal",
        "nesting": "Builds a stick nest in a tree, often using an existing structure",
        "breeding_season": "March to June",
        "clutch_size": "3–4 eggs",
        "call": "Repeated high-pitched whistles, particularly around breeding areas",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across most states; Pakistan: widespread; Nepal: Terai and lower hills; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar, Thailand, Laos, Cambodia and Vietnam: widespread; Africa: related populations occur widely."
    }
},

{
    "name": "White-Breasted Waterhen",
    "scientific": "Amaurornis phoenicurus",
    "description": "The White-Breasted Waterhen is a dark waterbird with a white face, breast, and belly, a reddish undertail, and long yellowish legs. It is commonly found around freshwater wetlands, ponds, marshes, canals, and overgrown waterways. It often walks through dense vegetation and shallow water searching for insects, molluscs, seeds, and other food. Despite its wetland association, it can occur surprisingly close to human settlements. Compared with the similar White-Browed Wagtail, it is distinguished by the combination of features described above. Its preference for marshes, ponds, canals, rice fields, wetlands, and dense vegetation near water also helps separate it from species that use different habitats. Its characteristic behaviour, including walks actively through vegetation and shallow water and may swim when necessary, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "White-BreastedWaterhen1.jpg",
    "quick_facts": {
        "family": "Rallidae",
        "size": "28–33 cm",
        "weight": "170–300 g",
        "wingspan": "45–50 cm",
        "diet": "Insects, worms, molluscs, seeds, frogs, and small aquatic animals",
        "habitat": "Marshes, ponds, canals, rice fields, wetlands, and dense vegetation near water",
        "behaviour": "Walks actively through vegetation and shallow water and may swim when necessary",
        "activity": "Diurnal and crepuscular",
        "nesting": "Builds a platform or cup-like nest among reeds, grasses, or waterside vegetation",
        "breeding_season": "June to September in many parts of India",
        "clutch_size": "4–9 eggs",
        "call": "Loud repeated clucks, screams, and harsh calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in wetlands across most states; Pakistan: Sindh and Punjab; Nepal: Terai; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar, Thailand, Laos, Cambodia, Vietnam, Malaysia and Indonesia: widespread."
    }
},

{
    "name": "White-Rumped Munia",
    "scientific": "Lonchura striata",
    "description": "The White-Rumped Munia is a small, social seed-eating bird with dark brown plumage and a contrasting white rump. It usually occurs in grasslands, scrub, cultivated areas, and forest edges and often travels in flocks. It feeds mainly on grass seeds and grains and can be difficult to notice until a group suddenly rises from the vegetation. Compared with the similar Scaly-Breasted Munia, it is distinguished by the combination of features described above. Its preference for grassland, scrub, farmland, woodland edges, and gardens also helps separate it from species that use different habitats. Its characteristic behaviour, including highly social and usually feeds in flocks among grasses, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "White-RumpedMunia1.jpg",
    "quick_facts": {
        "family": "Estrildidae",
        "size": "10–12 cm",
        "weight": "10–15 g",
        "wingspan": "16–18 cm",
        "diet": "Grass seeds, grains, and other small seeds",
        "habitat": "Grassland, scrub, farmland, woodland edges, and gardens",
        "behaviour": "Highly social and usually feeds in flocks among grasses",
        "activity": "Diurnal",
        "nesting": "Builds a rounded or domed nest from grass and plant fibres",
        "breeding_season": "Varies by region and rainfall",
        "clutch_size": "4–7 eggs",
        "call": "Soft chirping and twittering calls",
        "lifespan": "Several years in captivity; generally shorter in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread, especially the Himalaya, Northeast and peninsular forests and grasslands; Pakistan: northern and eastern regions; Nepal: widespread; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: widespread; Myanmar, Thailand, Laos, Cambodia, Vietnam, Malaysia and Indonesia: widespread."
    }
},

{
    "name": "White-Throated Kingfisher",
    "scientific": "Halcyon smyrnensis",
    "description": "The White-Throated Kingfisher is a large and colourful kingfisher with a bright blue back and wings, chestnut head and body, white throat and breast, and a large red bill. Despite its name, it is not restricted to aquatic habitats and frequently hunts from perches far from water. It catches insects, lizards, frogs, small birds, and other prey and is one of the most widespread kingfishers in India. Compared with the similar Common Kingfisher, it is distinguished by the combination of features described above. Its preference for open woodland, farmland, gardens, wetlands, villages, and urban areas also helps separate it from species that use different habitats. Its characteristic behaviour, including perches on exposed branches, wires, or poles before diving or dropping onto prey, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "White-ThroatedKingfisher1.jpg",
    "quick_facts": {
        "family": "Alcedinidae",
        "size": "27–29 cm",
        "weight": "80–100 g",
        "wingspan": "42–45 cm",
        "diet": "Fish, frogs, lizards, insects, small birds, rodents, and other small animals",
        "habitat": "Open woodland, farmland, gardens, wetlands, villages, and urban areas",
        "behaviour": "Perches on exposed branches, wires, or poles before diving or dropping onto prey",
        "activity": "Diurnal",
        "nesting": "Excavates a tunnel in an earthen bank or similar soft substrate",
        "breeding_season": "February to July",
        "clutch_size": "4–7 eggs",
        "call": "Loud, harsh and rattling calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across most states; Pakistan: widespread; Nepal: Terai and lower hills; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar, Thailand, Laos, Cambodia, Vietnam and Malaysia: widespread."
    }
},

{
    "name": "Brahminy Kite",
    "scientific": "Haliastur indus",
    "description": "The Brahminy Kite is a striking raptor with a chestnut-brown body, contrasting white head and breast, broad wings, and a rounded tail. It is particularly associated with coastal areas, rivers, wetlands, and other places where fish and carrion are available. It often soars gracefully and can be seen perched near water. Its distinctive plumage makes it one of India's most recognizable birds of prey. Compared with the similar Black Kite, it is distinguished by the combination of features described above. Its preference for coasts, rivers, wetlands, lakes, mangroves, and open woodland also helps separate it from species that use different habitats. Its characteristic behaviour, including often soars over water and scavenges or catches prey near the surface, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "BrahminyKite1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "44–52 cm",
        "weight": "500–800 g",
        "wingspan": "110–125 cm",
        "diet": "Fish, carrion, frogs, insects, crustaceans, and small animals",
        "habitat": "Coasts, rivers, wetlands, lakes, mangroves, and open woodland",
        "behaviour": "Often soars over water and scavenges or catches prey near the surface",
        "activity": "Diurnal",
        "nesting": "Builds a large stick nest in tall trees, often near water",
        "breeding_season": "December to April",
        "clutch_size": "Usually 2 eggs",
        "call": "High-pitched whistles and shrill calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: coastal and riverine regions across many states, especially West Bengal, Odisha, Andhra Pradesh, Telangana, Tamil Nadu, Kerala, Karnataka, Goa, Maharashtra, Gujarat and Assam; Pakistan: Sindh; Nepal: lowlands; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern valleys; Myanmar, Thailand, Malaysia, Indonesia and Australia: widespread."
    }
},

{
    "name": "Brahminy Starling",
    "scientific": "Sturnia pagodarum",
    "description": "The Brahminy Starling is an attractive medium-sized starling with a pale body, black crest, chestnut shoulders, and yellowish bill and legs. It is usually found in open woodland, scrub, farmland, gardens, and dry areas. It feeds on fruits, insects, nectar, and seeds and often moves through trees and bushes in pairs or small groups. Compared with the similar Indian Pied Starling, it is distinguished by the combination of features described above. Its preference for open woodland, scrub, farmland, gardens, and dry countryside also helps separate it from species that use different habitats. Its characteristic behaviour, including active and social, usually seen singly, in pairs, or small groups, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "BrahminyStarling1.jpg",
    "quick_facts": {
        "family": "Sturnidae",
        "size": "19–21 cm",
        "weight": "55–70 g",
        "wingspan": "Approximately 35–40 cm",
        "diet": "Fruits, insects, nectar, seeds, and grains",
        "habitat": "Open woodland, scrub, farmland, gardens, and dry countryside",
        "behaviour": "Active and social, usually seen singly, in pairs, or small groups",
        "activity": "Diurnal",
        "nesting": "Uses tree cavities and other sheltered holes for nesting",
        "breeding_season": "April to July",
        "clutch_size": "3–5 eggs",
        "call": "Varied whistles, clicks, and chattering notes",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: mainly northern, central and peninsular plains, including Rajasthan, Gujarat, Uttar Pradesh, Madhya Pradesh, Maharashtra, Odisha, West Bengal, Karnataka, Telangana, Andhra Pradesh and Tamil Nadu; Pakistan: Punjab and Sindh; Nepal: Terai; Bangladesh: local; Sri Lanka: local."
    }
},

{
    "name": "Indian Robin",
    "scientific": "Copsychus fulicatus",
    "description": "The Indian Robin is a small, active songbird of open and dry habitats. Males are generally dark with a contrasting white shoulder or wing patch, while females are browner. It spends much of its time close to the ground, running between rocks, shrubs, and grass while searching for insects. Its upright posture and habit of flicking its tail are useful identification features. Compared with the similar Oriental Magpie-Robin, it is distinguished by the combination of features described above. Its preference for dry scrub, rocky areas, grassland, farmland, and open woodland also helps separate it from species that use different habitats. Its characteristic behaviour, including active ground forager that often perches on low rocks and bushes, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "IndianRobin1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "17–18 cm",
        "weight": "20–25 g",
        "wingspan": "Approximately 25–28 cm",
        "diet": "Insects, spiders, worms, and other small invertebrates",
        "habitat": "Dry scrub, rocky areas, grassland, farmland, and open woodland",
        "behaviour": "Active ground forager that often perches on low rocks and bushes",
        "activity": "Diurnal",
        "nesting": "Nests in cavities, holes among rocks, walls, or other sheltered places",
        "breeding_season": "February to September",
        "clutch_size": "2–4 eggs",
        "call": "Short whistles, clicks, and varied song",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in dry and open regions, especially Rajasthan, Gujarat, Madhya Pradesh, Maharashtra, Karnataka, Telangana, Andhra Pradesh and Tamil Nadu; Pakistan: widespread; Nepal: Terai; Bangladesh: local; Sri Lanka: local."
    }
},

{
    "name": "Common Tailorbird",
    "scientific": "Orthotomus sutorius",
    "description": "The Common Tailorbird is a tiny, active warbler named for its remarkable nest-building technique. It stitches or binds large leaves together with plant fibres and spider silk to form a protective structure around its nest. It has a green back, pale underparts, a rusty crown, and a long tail often held upright. It is extremely common in gardens, scrub, plantations, and urban areas. Compared with the similar Ashy Prinia, it is distinguished by the combination of features described above. Its preference for gardens, scrub, woodland edges, plantations, parks, and cities also helps separate it from species that use different habitats. Its characteristic behaviour, including highly active and often moves rapidly through leaves and shrubs, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "CommonTailorbird1.jpg",
    "quick_facts": {
        "family": "Cisticolidae",
        "size": "13–14 cm",
        "weight": "6–10 g",
        "wingspan": "13–17 cm",
        "diet": "Insects, caterpillars, spiders, and other small invertebrates",
        "habitat": "Gardens, scrub, woodland edges, plantations, parks, and cities",
        "behaviour": "Highly active and often moves rapidly through leaves and shrubs",
        "activity": "Diurnal",
        "nesting": "Stitches or binds leaves together with plant fibres and spider silk",
        "breeding_season": "Throughout much of the year, especially during the monsoon",
        "clutch_size": "2–4 eggs",
        "call": "Loud, repetitive and sharp 'chee-up' style calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across most states; Pakistan: eastern regions; Nepal: Terai and lower hills; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar, Thailand, Laos, Cambodia, Vietnam, Malaysia and Indonesia: widespread."
    }
},

{
    "name": "Greater Racket-Tailed Drongo",
    "scientific": "Dicrurus paradiseus",
    "description": "The Greater Racket-Tailed Drongo is a spectacular forest bird with glossy black plumage, a prominent crest, and exceptionally long tail feathers ending in racket-shaped tips. It is an agile aerial hunter and also feeds on insects taken from foliage. It is famous for its varied vocal abilities and can imitate the calls of other birds. It usually inhabits forests and mature woodland with dense canopy. Compared with the similar Black Drongo, it is distinguished by the combination of features described above. Its preference for forests, mature woodland, plantations, and dense tree cover also helps separate it from species that use different habitats. Its characteristic behaviour, including agile aerial hunter and vocal mimic that may join mixed-species feeding groups, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "GreaterRacket-TailedDrongo1.jpg",
    "quick_facts": {
        "family": "Dicruridae",
        "size": "31–36 cm excluding elongated tail feathers",
        "weight": "70–100 g",
        "wingspan": "Approximately 40–45 cm",
        "diet": "Insects and other small invertebrates, with occasional fruit",
        "habitat": "Forests, mature woodland, plantations, and dense tree cover",
        "behaviour": "Agile aerial hunter and vocal mimic that may join mixed-species feeding groups",
        "activity": "Diurnal",
        "nesting": "Builds a small cup-shaped nest on a tree branch",
        "breeding_season": "April to June",
        "clutch_size": "2–4 eggs",
        "call": "Extremely varied whistles, metallic notes, and imitations of other birds",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: Northeast, eastern and peninsular forests, especially Assam, Arunachal Pradesh, Meghalaya, Nagaland, Manipur, Mizoram, West Bengal, Odisha, Jharkhand, Chhattisgarh, Maharashtra, Goa, Karnataka, Kerala and Tamil Nadu; Nepal: foothills; Bhutan: widespread; Bangladesh: local; Myanmar, Thailand, Laos, Cambodia, Vietnam and Malaysia: widespread."
    }
},

{
    "name": "Grey Heron",
    "scientific": "Ardea cinerea",
    "description": "The Grey Heron is a large, long-legged wading bird with a long pointed bill, grey wings, white head and neck, and a black crown stripe. It usually hunts from shallow water, standing motionless before striking quickly at fish and other prey. It is widespread across wetlands and can often be seen standing alone along rivers, lakes, ponds, and coastal waters. Compared with the similar Purple Heron, it is distinguished by the combination of features described above. Its preference for rivers, lakes, ponds, marshes, estuaries, canals, and coastal wetlands also helps separate it from species that use different habitats. Its characteristic behaviour, including usually hunts by standing motionless before making a rapid strike at prey, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "GreyHeron1.jpg",
    "quick_facts": {
        "family": "Ardeidae",
        "size": "84–102 cm",
        "weight": "1–2 kg",
        "wingspan": "155–195 cm",
        "diet": "Fish, frogs, reptiles, small mammals, birds, insects, and crustaceans",
        "habitat": "Rivers, lakes, ponds, marshes, estuaries, canals, and coastal wetlands",
        "behaviour": "Usually hunts by standing motionless before making a rapid strike at prey",
        "activity": "Diurnal and sometimes nocturnal",
        "nesting": "Builds large stick nests in trees, reeds, or cliffs, often in colonies",
        "breeding_season": "February to June in many areas",
        "clutch_size": "3–5 eggs",
        "call": "Loud harsh croaking calls, especially in flight",
        "lifespan": "Around 5–15 years, with some individuals living longer",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across wetlands and coasts in most states; Pakistan: widespread; Nepal: lowlands and valleys; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: valleys; Myanmar, Thailand, Laos, Cambodia, Vietnam, Malaysia and Indonesia: widespread; Europe, Africa and much of Asia: widespread."
    }
},

{
    "name": "Grey-Headed Fish Eagle",
    "scientific": "Icthyophaga ichthyaetus",
    "description": "The Grey-Headed Fish Eagle is a large fish-eating raptor associated with rivers, lakes, reservoirs, and other freshwater habitats. Adults have a distinctive grey head, dark brown body, powerful yellow bill and legs, and broad wings. It usually hunts by watching from a perch near water and swooping down to seize fish. Its large size and deep wingbeats make it an impressive sight along wooded waterways. Compared with the similar White-Bellied Sea-Eagle, it is distinguished by the combination of features described above. Its preference for rivers, lakes, reservoirs, wetlands, and forested waterways also helps separate it from species that use different habitats. Its characteristic behaviour, including often watches from a high perch and dives or swoops down to catch fish, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Grey-HeadedFishEagle1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "61–72 cm",
        "weight": "1.5–2.5 kg",
        "wingspan": "150–170 cm",
        "diet": "Fish, frogs, reptiles, waterbirds, and other aquatic animals",
        "habitat": "Rivers, lakes, reservoirs, wetlands, and forested waterways",
        "behaviour": "Often watches from a high perch and dives or swoops down to catch fish",
        "activity": "Diurnal",
        "nesting": "Builds a large stick nest in a tall tree near water",
        "breeding_season": "November to May",
        "clutch_size": "Usually 1–2 eggs",
        "call": "High-pitched whistles and repeated cries",
        "lifespan": "Several years in the wild",
        "conservation_status": "Near Threatened",
        "where_to_find": "India: Himalayan foothills, Northeast and peninsular wetlands, especially Uttarakhand, West Bengal, Assam, Arunachal Pradesh, Odisha, Chhattisgarh, Maharashtra, Karnataka, Kerala and Tamil Nadu; Nepal: Terai and foothills; Bangladesh: local; Bhutan: widespread; Myanmar, Thailand, Laos, Cambodia, Vietnam and Malaysia: widespread."
    }
},

{
    "name": "Indian Cormorant",
    "scientific": "Phalacrocorax fuscicollis",
    "description": "The Indian Cormorant is a dark waterbird with a long neck, slender bill, and distinctive greenish facial skin. It is an excellent swimmer and dives underwater to catch fish and other aquatic prey. Groups often perch together on exposed branches, rocks, or posts after feeding. It is widely distributed across freshwater wetlands and is especially common in southern and central India. Compared with the similar Little Cormorant, it is distinguished by the combination of features described above. Its preference for rivers, lakes, reservoirs, ponds, canals, marshes, and wetlands also helps separate it from species that use different habitats. Its characteristic behaviour, including dives underwater to catch fish and often rests with wings spread to dry them, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "IndianCormorant1.jpg",
    "quick_facts": {
        "family": "Phalacrocoracidae",
        "size": "63–65 cm",
        "weight": "650–1000 g",
        "wingspan": "90–105 cm",
        "diet": "Fish, frogs, crustaceans, and other aquatic animals",
        "habitat": "Rivers, lakes, reservoirs, ponds, canals, marshes, and wetlands",
        "behaviour": "Dives underwater to catch fish and often rests with wings spread to dry them",
        "activity": "Diurnal",
        "nesting": "Builds a stick nest in trees or shrubs, usually in colonies",
        "breeding_season": "Varies by region and rainfall",
        "clutch_size": "3–5 eggs",
        "call": "Usually quiet away from colonies; produces grunts and croaks at nesting sites",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in freshwater and coastal wetlands, especially West Bengal, Odisha, Bihar, Uttar Pradesh, Assam, Maharashtra, Karnataka, Kerala, Tamil Nadu, Telangana and Andhra Pradesh; Pakistan: Sindh; Nepal: Terai; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: valleys; Myanmar: widespread."
    }
},

{
    "name": "Indian Paradise Flycatcher",
    "scientific": "Terpsiphone paradisi",
    "description": "The Indian Paradise Flycatcher is a striking insect-eating bird with strongly contrasting plumage. Adult males may have long flowing tail feathers and either white or rufous plumage depending on their form, while females are shorter-tailed. It hunts insects from the air and foliage and is especially associated with wooded habitats. Its graceful movements and long tail make it one of India's most beautiful flycatchers. Compared with the similar Asian Brown Flycatcher, it is distinguished by the combination of features described above. Its preference for forests, woodland, gardens, plantations, and wooded streams also helps separate it from species that use different habitats. Its characteristic behaviour, including agile flycatcher that sallies from perches to catch insects, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "IndianParadiseFlycatcher1.jpg",
    "quick_facts": {
        "family": "Monarchidae",
        "size": "19–22 cm, with male tail streamers extending much farther",
        "weight": "15–25 g",
        "wingspan": "Approximately 25–30 cm",
        "diet": "Flying insects, caterpillars, beetles, and other small invertebrates",
        "habitat": "Forests, woodland, gardens, plantations, and wooded streams",
        "behaviour": "Agile flycatcher that sallies from perches to catch insects",
        "activity": "Diurnal",
        "nesting": "Builds a small cup-shaped nest in the fork of a tree or shrub",
        "breeding_season": "April to August",
        "clutch_size": "2–4 eggs",
        "call": "Soft whistles and sharp calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in wooded habitats, especially Himalaya, Northeast, central India and peninsular forests; Pakistan: northern foothills; Nepal: widespread; Bangladesh: widespread; Sri Lanka: local; Bhutan: widespread; Myanmar, Thailand, Laos and Cambodia: widespread."
    }
},

{
    "name": "Indian Pied Starling",
    "scientific": "Gracupica contra",
    "description": "The Indian Pied Starling is a striking black-and-white starling with a pale bill and distinctive orange or reddish facial skin around the eye. It is a social and adaptable species that often feeds on the ground in groups. It consumes insects, fruits, grains, and other food and is frequently found around villages, farmland, wetlands, and urban areas. Compared with the similar Common Myna, it is distinguished by the combination of features described above. Its preference for farmland, villages, wetlands, gardens, open woodland, and cities also helps separate it from species that use different habitats. Its characteristic behaviour, including social and often forages in groups on open ground, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "IndianPiedStarling1.jpg",
    "quick_facts": {
        "family": "Sturnidae",
        "size": "21–23 cm",
        "weight": "75–100 g",
        "wingspan": "Approximately 35–40 cm",
        "diet": "Insects, fruits, grains, seeds, nectar, and food scraps",
        "habitat": "Farmland, villages, wetlands, gardens, open woodland, and cities",
        "behaviour": "Social and often forages in groups on open ground",
        "activity": "Diurnal",
        "nesting": "Uses tree cavities, buildings, walls, and other sheltered cavities",
        "breeding_season": "April to September",
        "clutch_size": "3–5 eggs",
        "call": "Loud whistles, chatters, and varied calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in plains and settled country; Pakistan: Punjab and Sindh; Nepal: Terai; Bangladesh: widespread; Bhutan: southern foothills; Myanmar: local; introduced or vagrant populations occur elsewhere in South Asia."
    }
},

{
    "name": "Lesser Whistling Duck",
    "scientific": "Dendrocygna javanica",
    "description": "The Lesser Whistling Duck is a small, brownish duck with a rounded head and longish neck. It is often seen in large groups on ponds, lakes, marshes, rice fields, and other freshwater habitats. It feeds on aquatic vegetation, seeds, insects, and small aquatic animals. Its high-pitched whistling calls are especially noticeable when groups take flight. Compared with the similar Little Cormorant, it is distinguished by the combination of features described above. Its preference for ponds, lakes, marshes, rice fields, reservoirs, and slow-moving waters also helps separate it from species that use different habitats. Its characteristic behaviour, including social and often forms large flocks; spends much time resting on water or banks, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "LesserWhistlingDuck1.jpg",
    "quick_facts": {
        "family": "Anatidae",
        "size": "38–43 cm",
        "weight": "450–700 g",
        "wingspan": "75–85 cm",
        "diet": "Aquatic plants, seeds, grains, insects, and small aquatic animals",
        "habitat": "Ponds, lakes, marshes, rice fields, reservoirs, and slow-moving waters",
        "behaviour": "Social and often forms large flocks; spends much time resting on water or banks",
        "activity": "Mostly nocturnal and crepuscular, though also active by day",
        "nesting": "Nests among aquatic vegetation, grass, tree cavities, or other sheltered locations",
        "breeding_season": "June to October in much of India",
        "clutch_size": "6–12 eggs",
        "call": "High-pitched whistling calls, especially in flight",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in wetlands, especially West Bengal, Assam, Bihar, Odisha, Uttar Pradesh, Madhya Pradesh, Chhattisgarh, Maharashtra, Karnataka, Kerala, Tamil Nadu, Telangana and Andhra Pradesh; Pakistan: local Sindh populations; Nepal: Terai; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern valleys; Myanmar, Thailand, Laos, Cambodia, Vietnam and Malaysia: widespread."
    }
},

{
    "name": "Oriental Darter",
    "scientific": "Anhinga melanogaster",
    "description": "The Oriental Darter is a long-necked waterbird that often swims with only its head and neck above the water, giving it the appearance of a snake. It is an excellent underwater hunter and spears fish with its sharp bill. After feeding, it commonly perches with its wings spread to dry its feathers. It is found in freshwater wetlands, rivers, lakes, marshes, and reservoirs. Compared with the similar Indian Cormorant, it is distinguished by the combination of features described above. Its preference for lakes, rivers, marshes, reservoirs, ponds, and freshwater wetlands also helps separate it from species that use different habitats. Its characteristic behaviour, including swims with much of its body submerged and spears fish underwater, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "OrientalDarter1.jpg",
    "quick_facts": {
        "family": "Anhingidae",
        "size": "85–97 cm",
        "weight": "1.1–1.4 kg",
        "wingspan": "110–120 cm",
        "diet": "Fish, frogs, crustaceans, and other aquatic animals",
        "habitat": "Lakes, rivers, marshes, reservoirs, ponds, and freshwater wetlands",
        "behaviour": "Swims with much of its body submerged and spears fish underwater",
        "activity": "Diurnal",
        "nesting": "Builds a stick nest in trees or shrubs near water, often in colonies",
        "breeding_season": "Varies by region and water conditions",
        "clutch_size": "3–5 eggs",
        "call": "Generally quiet away from colonies; produces grunts and croaks around nesting sites",
        "lifespan": "Several years in the wild",
        "conservation_status": "Near Threatened",
        "where_to_find": "India: widespread in freshwater wetlands, especially West Bengal, Assam, Odisha, Bihar, Uttar Pradesh, Madhya Pradesh, Chhattisgarh, Maharashtra, Karnataka, Kerala, Tamil Nadu, Telangana and Andhra Pradesh; Pakistan: Sindh; Nepal: Terai; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: valleys; Myanmar, Thailand, Laos, Cambodia, Vietnam and Malaysia: widespread."
    }
},

{
    "name": "Pied Kingfisher",
    "scientific": "Ceryle rudis",
    "description": "The Pied Kingfisher is a black-and-white kingfisher famous for hovering above water before diving vertically to catch fish. It has a shaggy crest, long pointed bill, and strongly patterned plumage. It is closely associated with rivers, lakes, reservoirs, estuaries, and other open waters and often hunts from exposed perches as well as by hovering. Compared with the similar Common Kingfisher, it is distinguished by the combination of features described above. Its preference for rivers, lakes, reservoirs, estuaries, canals, and coastal waters also helps separate it from species that use different habitats. Its characteristic behaviour, including frequently hovers over water before diving vertically to catch fish, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "PiedKingfisher1.jpg",
    "quick_facts": {
        "family": "Cerylidae",
        "size": "25–29 cm",
        "weight": "70–100 g",
        "wingspan": "46–50 cm",
        "diet": "Fish, aquatic insects, crustaceans, and other small aquatic animals",
        "habitat": "Rivers, lakes, reservoirs, estuaries, canals, and coastal waters",
        "behaviour": "Frequently hovers over water before diving vertically to catch fish",
        "activity": "Diurnal",
        "nesting": "Excavates a tunnel in a sandy or earthen bank",
        "breeding_season": "January to April and sometimes later depending on region",
        "clutch_size": "3–6 eggs",
        "call": "Sharp, rapid rattling calls, especially in flight",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread along rivers, lakes, reservoirs and coasts; Pakistan: widespread; Nepal: lowlands and valleys; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern valleys; Myanmar, Thailand, Laos, Cambodia, Vietnam, Malaysia and Indonesia: widespread; Africa and the Middle East: widespread."
    }
},

{
    "name": "Purple Heron",
    "scientific": "Ardea purpurea",
    "description": "The Purple Heron is a large, slender wading bird with rich reddish-brown and purple-grey plumage, a long neck, and long legs. It is generally more secretive than the Grey Heron and often remains hidden among reeds and tall vegetation. It hunts fish, frogs, reptiles, insects, and small mammals in shallow water and wetlands. Compared with the similar Grey Heron, it is distinguished by the combination of features described above. Its preference for reed beds, marshes, lakes, rivers, ponds, and flooded wetlands also helps separate it from species that use different habitats. Its characteristic behaviour, including usually hunts slowly and deliberately from shallow water or dense vegetation, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "PurpleHeron1.jpg",
    "quick_facts": {
        "family": "Ardeidae",
        "size": "78–97 cm",
        "weight": "525–1340 g",
        "wingspan": "120–150 cm",
        "diet": "Fish, frogs, reptiles, insects, crustaceans, and small mammals",
        "habitat": "Reed beds, marshes, lakes, rivers, ponds, and flooded wetlands",
        "behaviour": "Usually hunts slowly and deliberately from shallow water or dense vegetation",
        "activity": "Diurnal",
        "nesting": "Builds a platform nest in reeds, shrubs, or trees, often in colonies",
        "breeding_season": "March to June in many breeding areas",
        "clutch_size": "4–5 eggs",
        "call": "Harsh croaks, especially around breeding colonies",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in freshwater wetlands and reedbeds, especially northern plains, Northeast and peninsular wetlands; Pakistan: Sindh and Punjab; Nepal: Terai; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: valleys; Myanmar, Thailand, Laos, Cambodia, Vietnam and Malaysia: widespread; Europe, Africa and western Asia: widespread."
    }
},

{
    "name": "Spotted Dove",
    "scientific": "Spilopelia chinensis",
    "description": "The Spotted Dove is a medium-sized dove with a soft pinkish-grey body, dark wings, and a distinctive black-and-white spotted patch on the sides of its neck. It is a highly adaptable species and commonly occurs in gardens, farmland, woodland, villages, and cities. It feeds mainly on seeds and grains and usually forages on the ground. Compared with the similar Common Myna, it is distinguished by the combination of features described above. Its preference for gardens, farmland, woodland, scrub, villages, and urban areas also helps separate it from species that use different habitats. Its characteristic behaviour, including usually forages on the ground singly or in pairs and may gather in groups around food, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "SpottedDove1.jpg",
    "quick_facts": {
        "family": "Columbidae",
        "size": "28–32 cm",
        "weight": "150–200 g",
        "wingspan": "45–50 cm",
        "diet": "Seeds, grains, fruits, and small amounts of plant material",
        "habitat": "Gardens, farmland, woodland, scrub, villages, and urban areas",
        "behaviour": "Usually forages on the ground singly or in pairs and may gather in groups around food",
        "activity": "Diurnal",
        "nesting": "Builds a flimsy platform of twigs in trees, shrubs, buildings, or ledges",
        "breeding_season": "Throughout much of the year",
        "clutch_size": "Usually 2 eggs",
        "call": "Soft, repetitive cooing song",
        "lifespan": "Around 5–10 years in favourable conditions",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across most states; Pakistan: widespread; Nepal: Terai; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar, Thailand, Laos, Cambodia, Vietnam, Malaysia and Indonesia: widespread; introduced populations occur elsewhere."
    }
},

{
    "name": "Stork-Billed Kingfisher",
    "scientific": "Pelargopsis capensis",
    "description": "The Stork-Billed Kingfisher is a large and powerful kingfisher with a massive red bill, bright blue wings, chestnut head and body, and pale underparts. It is usually found near rivers, lakes, ponds, mangroves, and forest streams. It hunts fish and other aquatic animals but also takes reptiles, frogs, insects, and small birds. Its large size and heavy bill give it a particularly impressive appearance. Compared with the similar White-Throated Kingfisher, it is distinguished by the combination of features described above. Its preference for rivers, lakes, ponds, mangroves, forest streams, and wetlands also helps separate it from species that use different habitats. Its characteristic behaviour, including usually waits quietly on a branch before dropping or diving onto prey, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Stork-BilledKingfisher1.jpg",
    "quick_facts": {
        "family": "Alcedinidae",
        "size": "35–41 cm",
        "weight": "250–350 g",
        "wingspan": "65–75 cm",
        "diet": "Fish, frogs, reptiles, insects, crustaceans, and small birds",
        "habitat": "Rivers, lakes, ponds, mangroves, forest streams, and wetlands",
        "behaviour": "Usually waits quietly on a branch before dropping or diving onto prey",
        "activity": "Diurnal",
        "nesting": "Excavates a cavity or tunnel in an earthen bank or tree",
        "breeding_season": "January to August, depending on region",
        "clutch_size": "2–5 eggs",
        "call": "Loud, harsh and repetitive calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: forested rivers, lakes and wetlands across the Himalaya, Northeast and peninsular regions, especially Uttarakhand, West Bengal, Assam, Arunachal Pradesh, Odisha, Chhattisgarh, Maharashtra, Goa, Karnataka, Kerala and Tamil Nadu; Nepal: foothills; Bangladesh: local; Bhutan: widespread; Myanmar, Thailand, Laos, Cambodia, Vietnam, Malaysia and Indonesia: widespread."
    }
},

{
    "name": "Oriental White-Eye",
    "scientific": "Zosterops palpebrosus",
    "description": "The Oriental White-eye is a tiny, active bird with a conspicuous white ring around the eye, olive-green upperparts, and yellowish underparts. It moves rapidly through foliage while searching for insects, nectar, and small fruits. White-eyes are highly social and often travel in small groups. They are common in gardens, forests, plantations, and urban greenery. Compared with the similar Common Iora, it is distinguished by the combination of features described above. Its preference for gardens, forests, plantations, scrub, parks, and urban greenery also helps separate it from species that use different habitats. Its characteristic behaviour, including highly active and social, usually moving through foliage in small groups, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "OrientalWhite-Eye1.jpg",
    "quick_facts": {
        "family": "Zosteropidae",
        "size": "8–10 cm",
        "weight": "7–12 g",
        "wingspan": "13–16 cm",
        "diet": "Nectar, insects, small fruits, berries, and flower parts",
        "habitat": "Gardens, forests, plantations, scrub, parks, and urban greenery",
        "behaviour": "Highly active and social, usually moving through foliage in small groups",
        "activity": "Diurnal",
        "nesting": "Builds a tiny cup-shaped nest suspended from a fork in vegetation",
        "breeding_season": "February to September",
        "clutch_size": "2–3 eggs",
        "call": "High-pitched, rapid twittering and chirping",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in forests, gardens and plantations across most states; Pakistan: local in foothills; Nepal: widespread; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: widespread; Myanmar, Thailand, Laos, Cambodia, Vietnam, Malaysia and Indonesia: widespread."
    }
},

{
    "name": "White-Browed Fantail",
    "scientific": "Rhipidura aureola",
    "description": "The White-Browed Fantail is a small insectivorous bird with a boldly patterned face, pale eyebrow, dark body, and a broad fan-shaped tail. It is an energetic bird that constantly flicks and spreads its tail while moving through foliage. It catches insects by making short aerial sallies from branches and is commonly found in forests, gardens, scrub, and woodland edges. Compared with the similar Common Tailorbird, it is distinguished by the combination of features described above. Its preference for forests, woodland, scrub, plantations, gardens, and forest edges also helps separate it from species that use different habitats. Its characteristic behaviour, including active and acrobatic, frequently spreading and flicking its fan-shaped tail, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "White-BrowedFantail1.jpg",
    "quick_facts": {
        "family": "Rhipiduridae",
        "size": "17–19 cm",
        "weight": "10–15 g",
        "wingspan": "20–24 cm",
        "diet": "Flying insects, caterpillars, spiders, and other small invertebrates",
        "habitat": "Forests, woodland, scrub, plantations, gardens, and forest edges",
        "behaviour": "Active and acrobatic, frequently spreading and flicking its fan-shaped tail",
        "activity": "Diurnal",
        "nesting": "Builds a small cup-shaped nest on a branch or in a fork",
        "breeding_season": "March to August",
        "clutch_size": "2–3 eggs",
        "call": "Sharp chirps, whistles, and rapid chattering",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in peninsular, central and northern woodland, including Rajasthan, Gujarat, Madhya Pradesh, Maharashtra, Odisha, West Bengal, Assam, Karnataka, Kerala and Tamil Nadu; Pakistan: local; Nepal: Terai and lower hills; Bangladesh: local; Sri Lanka: widespread; Bhutan: foothills; Myanmar and mainland Southeast Asia: widespread."
    }
},

{
    "name": "Yellow-Footed Green Pigeon",
    "scientific": "Treron phoenicopterus",
    "description": "The Yellow-Footed Green Pigeon is a colourful fruit-eating pigeon with predominantly green plumage, yellow feet, and distinctive patches of yellow, orange, and grey on the wings and body. It spends most of its time in trees, where it feeds on fruit, berries, and figs. It is generally quiet and can be difficult to spot among foliage despite its attractive colours. Compared with the similar Spotted Dove, it is distinguished by the combination of features described above. Its preference for forests, woodland, gardens, plantations, orchards, and large trees also helps separate it from species that use different habitats. Its characteristic behaviour, including arboreal and usually feeds quietly in fruiting trees, often in small groups, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Yellow-FootedGreenPigeon1.jpg",
    "quick_facts": {
        "family": "Columbidae",
        "size": "29–33 cm",
        "weight": "200–250 g",
        "wingspan": "45–50 cm",
        "diet": "Fruits, berries, figs, buds, and seeds",
        "habitat": "Forests, woodland, gardens, plantations, orchards, and large trees",
        "behaviour": "Arboreal and usually feeds quietly in fruiting trees, often in small groups",
        "activity": "Diurnal",
        "nesting": "Builds a flimsy platform of twigs in trees or shrubs",
        "breeding_season": "March to September, varying by region",
        "clutch_size": "Usually 2 eggs",
        "call": "Soft, low-pitched cooing calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across central, western and peninsular states, including Rajasthan, Gujarat, Madhya Pradesh, Maharashtra, Goa, Karnataka, Kerala, Tamil Nadu, Telangana and Andhra Pradesh; Pakistan: local; Nepal: Terai; Bangladesh: local; Sri Lanka: local; Bhutan: southern foothills."
    }
},

{
    "name": "Asian Brown Flycatcher",
    "scientific": "Muscicapa dauurica",
    "description": "The Asian Brown Flycatcher is a small, plain-looking insectivorous bird with brown upperparts, pale underparts, and a relatively large dark bill. It usually sits quietly on a branch before making short flights to catch insects in the air. It is a common migrant or passage bird in many parts of India and can be found in wooded habitats, gardens, plantations, and forest edges. Compared with the similar Indian Paradise Flycatcher, it is distinguished by the combination of features described above. Its preference for forests, woodland edges, gardens, plantations, and wooded parks also helps separate it from species that use different habitats. Its characteristic behaviour, including perches quietly before making short aerial sallies to catch insects, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "AsianBrownFlycatcher1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "13–15 cm",
        "weight": "10–15 g",
        "wingspan": "20–24 cm",
        "diet": "Flying insects, beetles, flies, moths, and other small invertebrates",
        "habitat": "Forests, woodland edges, gardens, plantations, and wooded parks",
        "behaviour": "Perches quietly before making short aerial sallies to catch insects",
        "activity": "Diurnal",
        "nesting": "Builds a small cup-shaped nest in a tree cavity or sheltered site",
        "breeding_season": "May to July in its northern breeding range",
        "clutch_size": "3–5 eggs",
        "call": "Soft whistles and short sharp notes",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in wooded habitats, with breeding in the Himalaya and Northeast and wintering through much of peninsular India; Pakistan: northern foothills; Nepal: widespread; Bhutan: widespread; Bangladesh: wintering populations; Sri Lanka: wintering populations; Myanmar, Thailand, Laos, Cambodia and Vietnam: widespread."
    }
},

{
    "name": "Pied Bushchat",
    "scientific": "Saxicola caprata",
    "description": "The Pied Bushchat is a small, upright insect-eating bird commonly seen perched on shrubs, fences, rocks, and other exposed points in open country. Males are predominantly black with white wing and rump markings, while females are brown. It catches insects from perches and is particularly common in grassland, farmland, scrub, and open woodland. Compared with the similar Common Stonechat, it is distinguished by the combination of features described above. Its preference for grassland, scrub, farmland, open woodland, and rocky areas also helps separate it from species that use different habitats. Its characteristic behaviour, including perches prominently and makes short flights to capture insects, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "PiedBushchat1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "13 cm",
        "weight": "12–17 g",
        "wingspan": "18–21 cm",
        "diet": "Insects, spiders, worms, and other small invertebrates",
        "habitat": "Grassland, scrub, farmland, open woodland, and rocky areas",
        "behaviour": "Perches prominently and makes short flights to capture insects",
        "activity": "Diurnal",
        "nesting": "Nests in cavities, holes, rock crevices, and sheltered spaces near the ground",
        "breeding_season": "February to August",
        "clutch_size": "2–4 eggs",
        "call": "Sharp chirps and short whistles",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across open country in most states; Pakistan: widespread; Nepal: widespread; Bangladesh: local; Bhutan: valleys; Sri Lanka: widespread; Myanmar: local; Central and South Asia: widespread."
    }
},

{
    "name": "Black Redstart",
    "scientific": "Phoenicurus ochruros",
    "description": "The Black Redstart is a small chat with a dark body, orange-red tail, and characteristic habit of frequently flicking its tail. Plumage varies between males, females, and different populations. It prefers rocky and open habitats and often uses buildings, walls, and cliffs as nesting sites. In India it is primarily encountered in suitable northern and highland habitats during the colder months. Compared with the similar Pied Bushchat, it is distinguished by the combination of features described above. Its preference for rocky slopes, cliffs, open woodland, scrub, villages, and buildings also helps separate it from species that use different habitats. Its characteristic behaviour, including frequently flicks its tail and makes short flights from exposed perches to catch insects, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "BlackRedstart1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "14–15 cm",
        "weight": "14–20 g",
        "wingspan": "23–26 cm",
        "diet": "Insects, spiders, worms, berries, and other small food",
        "habitat": "Rocky slopes, cliffs, open woodland, scrub, villages, and buildings",
        "behaviour": "Frequently flicks its tail and makes short flights from exposed perches to catch insects",
        "activity": "Diurnal",
        "nesting": "Builds a cup-shaped nest in rock crevices, buildings, cavities, or sheltered ledges",
        "breeding_season": "April to July in breeding areas",
        "clutch_size": "4–6 eggs",
        "call": "Short ticking notes and varied whistles",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: mainly Himalayan and northern regions, including Jammu and Kashmir, Himachal Pradesh, Uttarakhand, Sikkim and Arunachal Pradesh, with wintering farther south; Pakistan: northern mountains; Nepal: widespread in hills; Bhutan: widespread; Afghanistan, Central Asia, Europe and North Africa: widespread."
    }
},

{
    "name": "Spotted Owlet",
    "scientific": "Athene brama",
    "description": "The Spotted Owlet is a small owl with a rounded head, pale facial disc, yellow eyes, and prominent white spotting across its brown plumage. It is highly adaptable and commonly lives around villages, gardens, farmland, parks, and cities. Although mainly active at night, it often emerges during daylight and may sit near the entrance of its nesting cavity. Compared with the similar Barn Owl, it is distinguished by the combination of features described above. Its preference for farmland, villages, gardens, open woodland, parks, and urban areas also helps separate it from species that use different habitats. Its characteristic behaviour, including often sits near its roost during daylight and hunts actively after dusk, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "SpottedOwlet1.jpg",
    "quick_facts": {
        "family": "Strigidae",
        "size": "19–21 cm",
        "weight": "100–140 g",
        "wingspan": "44–48 cm",
        "diet": "Insects, rodents, lizards, frogs, small birds, and other small animals",
        "habitat": "Farmland, villages, gardens, open woodland, parks, and urban areas",
        "behaviour": "Often sits near its roost during daylight and hunts actively after dusk",
        "activity": "Mostly nocturnal and crepuscular",
        "nesting": "Uses tree cavities, holes in walls, buildings, and other sheltered cavities",
        "breeding_season": "November to April",
        "clutch_size": "3–5 eggs",
        "call": "Varied hoots, chuckles, whistles, and chattering calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across most states, especially open woodland, farmland and towns; Pakistan: widespread; Nepal: Terai; Bangladesh: widespread; Sri Lanka: local; Bhutan: southern foothills."
    }
},

{
    "name": "Black-Naped Oriole",
    "scientific": "Oriolus chinensis",
    "description": "The Black-Naped Oriole is a bright yellow-and-black songbird with a dark stripe through the eye and nape. It spends most of its time in trees and feeds on fruit, nectar, and insects. Its melodious whistles are often heard from the canopy before the bird is visible. It is associated with forests, plantations, gardens, and wooded urban areas. Compared with the similar Indian Golden Oriole, it is distinguished by the combination of features described above. Its preference for forests, gardens, plantations, woodland, and parks also helps separate it from species that use different habitats. Its characteristic behaviour, including arboreal and generally remains in the canopy while feeding, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Black-NapedOriole1.jpg",
    "quick_facts": {
        "family": "Oriolidae",
        "size": "23–28 cm",
        "weight": "65–100 g",
        "wingspan": "40–45 cm",
        "diet": "Fruits, berries, insects, caterpillars, and nectar",
        "habitat": "Forests, gardens, plantations, woodland, and parks",
        "behaviour": "Arboreal and generally remains in the canopy while feeding",
        "activity": "Diurnal",
        "nesting": "Builds a suspended cup-shaped nest in a tree",
        "breeding_season": "April to July",
        "clutch_size": "2–3 eggs",
        "call": "Clear, melodious whistles and fluting notes",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: mainly peninsular and eastern regions, especially Maharashtra, Goa, Karnataka, Kerala, Tamil Nadu, Telangana, Andhra Pradesh, Odisha, West Bengal and Northeast India; Bangladesh: widespread; Sri Lanka: local; Bhutan: southern foothills; Myanmar, Thailand, Laos, Cambodia, Vietnam and Malaysia: widespread."
    }
},

{
    "name": "Woolly-Necked Stork",
    "scientific": "Ciconia episcopus",
    "description": "The Woolly-Necked Stork is a large dark-and-white stork with a distinctive white head and neck contrasting with a dark body. It usually forages alone or in pairs in open wetlands, grasslands, and agricultural fields, searching for frogs, fish, insects, reptiles, and other prey. It is generally less colonial than some other Indian storks and often keeps its distance from human activity. Compared with the similar Painted Stork, it is distinguished by the combination of features described above. Its preference for wetlands, grasslands, farmland, marshes, and open woodland also helps separate it from species that use different habitats. Its characteristic behaviour, including usually forages alone or in pairs by walking through open habitats, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Woolly-NeckedStork1.jpg",
    "quick_facts": {
        "family": "Ciconiidae",
        "size": "75–90 cm",
        "weight": "2.5–4 kg",
        "wingspan": "150–170 cm",
        "diet": "Frogs, fish, insects, reptiles, small mammals, and other small animals",
        "habitat": "Wetlands, grasslands, farmland, marshes, and open woodland",
        "behaviour": "Usually forages alone or in pairs by walking through open habitats",
        "activity": "Diurnal",
        "nesting": "Builds a large stick nest in tall trees, usually away from dense colonies",
        "breeding_season": "June to September in many parts of India",
        "clutch_size": "2–4 eggs",
        "call": "Usually quiet; may produce bill-clattering and soft sounds at nesting sites",
        "lifespan": "Several years in the wild",
        "conservation_status": "Near Threatened",
        "where_to_find": "India: patchy but widespread in suitable wetlands and grasslands, especially Rajasthan, Gujarat, Madhya Pradesh, Maharashtra, Chhattisgarh, Odisha, West Bengal, Assam, Karnataka, Kerala and Tamil Nadu; Pakistan: local; Nepal: Terai; Bangladesh: local; Sri Lanka: local; Bhutan: southern foothills; Myanmar and Southeast Asia: widespread but patchy."
    }
},

{
    "name": "Common Iora",
    "scientific": "Aegithina tiphia",
    "description": "The Common Iora is a small, active songbird with bright greenish-yellow plumage and contrasting dark wings in breeding males. It is usually found in trees and shrubs, where it moves rapidly through foliage searching for insects and small invertebrates. Males perform energetic displays during the breeding season, sometimes spreading their wings and tail while singing. Compared with the similar Oriental White-Eye, it is distinguished by the combination of features described above. Its preference for gardens, forests, woodland, scrub, plantations, and parks also helps separate it from species that use different habitats. Its characteristic behaviour, including active foliage gleaner that moves rapidly among leaves while searching for prey, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "CommonIora1.jpg",
    "quick_facts": {
        "family": "Aegithinidae",
        "size": "12–13 cm",
        "weight": "12–15 g",
        "wingspan": "18–20 cm",
        "diet": "Insects, caterpillars, spiders, and other small invertebrates",
        "habitat": "Gardens, forests, woodland, scrub, plantations, and parks",
        "behaviour": "Active foliage gleaner that moves rapidly among leaves while searching for prey",
        "activity": "Diurnal",
        "nesting": "Builds a tiny cup-shaped nest in a fork of a tree or shrub",
        "breeding_season": "March to September",
        "clutch_size": "2–3 eggs",
        "call": "Musical whistles, trills, and varied notes",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in wooded and garden habitats, especially peninsular, central and eastern states; Pakistan: local Sindh populations; Nepal: Terai; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar, Thailand, Laos, Cambodia, Vietnam, Malaysia and Indonesia: widespread."
    }
},

{
    "name": "Jungle Owlet",
    "scientific": "Glaucidium radiatum",
    "description": "The Jungle Owlet is a small woodland owl with a rounded head, barred brown-and-white plumage, and yellow eyes. Unlike many owls, it can be active during daylight, especially around dawn and dusk. It hunts insects, small reptiles, rodents, and birds and usually remains within wooded habitats. Its calls can be heard from forest edges and dense vegetation. Compared with the similar Spotted Owlet, it is distinguished by the combination of features described above. Its preference for forests, woodland, plantations, scrub, and wooded hills also helps separate it from species that use different habitats. Its characteristic behaviour, including often active during daylight and hunts from low perches within dense vegetation, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "JungleOwlet1.jpg",
    "quick_facts": {
        "family": "Strigidae",
        "size": "20–23 cm",
        "weight": "100–150 g",
        "wingspan": "40–45 cm",
        "diet": "Insects, lizards, rodents, small birds, and other small animals",
        "habitat": "Forests, woodland, plantations, scrub, and wooded hills",
        "behaviour": "Often active during daylight and hunts from low perches within dense vegetation",
        "activity": "Diurnal, crepuscular, and sometimes nocturnal",
        "nesting": "Uses tree cavities, often taking advantage of old woodpecker holes",
        "breeding_season": "March to May",
        "clutch_size": "2–4 eggs",
        "call": "Repeated whistles, hoots, and sharp notes",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: Himalaya, central India, Northeast and peninsular forests, including Uttarakhand, West Bengal, Assam, Odisha, Chhattisgarh, Maharashtra, Karnataka, Kerala and Tamil Nadu; Nepal: foothills; Bhutan: widespread; Bangladesh: local; Sri Lanka: local; Myanmar: widespread."
    }
},

{
    "name": "Black-Hooded Oriole",
    "scientific": "Oriolus xanthornus",
    "description": "The Black-Hooded Oriole is a striking yellow-and-black bird with a strongly contrasting black head and bright yellow body. It is an arboreal species that spends much of its time in the canopy, feeding on fruits, nectar, and insects. Its melodious whistles are often heard from tall trees. It occurs in forests, plantations, gardens, and wooded urban areas. Compared with the similar Black-Naped Oriole, it is distinguished by the combination of features described above. Its preference for forests, gardens, plantations, parks, and wooded urban areas also helps separate it from species that use different habitats. Its characteristic behaviour, including arboreal and usually remains high in trees while feeding, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Black-HoodedOriole1.jpg",
    "quick_facts": {
        "family": "Oriolidae",
        "size": "23–25 cm",
        "weight": "60–90 g",
        "wingspan": "40–45 cm",
        "diet": "Fruits, berries, nectar, insects, and caterpillars",
        "habitat": "Forests, gardens, plantations, parks, and wooded urban areas",
        "behaviour": "Arboreal and usually remains high in trees while feeding",
        "activity": "Diurnal",
        "nesting": "Builds a suspended cup-shaped nest in a tree fork",
        "breeding_season": "April to August",
        "clutch_size": "2–3 eggs",
        "call": "Clear, melodious whistles and fluting notes",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: mainly peninsular and eastern regions, especially Maharashtra, Goa, Karnataka, Kerala, Tamil Nadu, Telangana, Andhra Pradesh, Odisha, West Bengal and Northeast India; Bangladesh: widespread; Sri Lanka: local; Bhutan: southern foothills; Myanmar, Thailand, Laos, Cambodia, Vietnam and Malaysia: widespread."
    }
},

{
    "name": "Brown Rock Chat",
    "scientific": "Oenanthe fusca",
    "description": "The Brown Rock Chat is a small, dark brown chat associated strongly with rocky landscapes and human structures. It is often seen perched on walls, rocks, roofs, and ruins before dropping down to catch insects. It is particularly well adapted to dry environments and is common around villages, forts, rocky hills, and open scrub. Compared with the similar Pied Bushchat, it is distinguished by the combination of features described above. Its preference for rocky hills, dry scrub, villages, ruins, cliffs, and open countryside also helps separate it from species that use different habitats. Its characteristic behaviour, including perches on rocks and buildings before making short flights to capture insects, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "BrownRockChat1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "18–20 cm",
        "weight": "35–45 g",
        "wingspan": "30–34 cm",
        "diet": "Insects, spiders, worms, and other small invertebrates",
        "habitat": "Rocky hills, dry scrub, villages, ruins, cliffs, and open countryside",
        "behaviour": "Perches on rocks and buildings before making short flights to capture insects",
        "activity": "Diurnal",
        "nesting": "Nests in cavities in walls, buildings, rock crevices, and similar sheltered sites",
        "breeding_season": "March to July",
        "clutch_size": "2–4 eggs",
        "call": "Short whistles, clicks, and chattering notes",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in rocky and dry country, especially Rajasthan, Gujarat, Madhya Pradesh, Maharashtra, Uttar Pradesh, Bihar, Karnataka, Telangana and Tamil Nadu; Pakistan: widespread; Nepal: Terai and lower hills; Bangladesh: local; Bhutan: foothills."
    }
},

{
    "name": "Blue-Tailed Bee-Eater",
    "scientific": "Merops philippinus",
    "description": "The Blue-Tailed Bee-eater is a colourful aerial insect hunter with a green body, blue tail, yellow throat, black eye stripe, and elongated central tail feathers. It spends much of its time catching flying insects from exposed perches or directly in the air. It is particularly associated with open habitats near water and often gathers in groups. Compared with the similar Asian-Green Bee-eater, it is distinguished by the combination of features described above. Its preference for open country, riverbanks, wetlands, farmland, grassland, and scrub also helps separate it from species that use different habitats. Its characteristic behaviour, including highly agile aerial hunter that catches insects in flight and returns to a perch, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Blue-TailedBee-Eater1.jpg",
    "quick_facts": {
        "family": "Meropidae",
        "size": "25–30 cm including elongated tail feathers",
        "weight": "30–45 g",
        "wingspan": "35–40 cm",
        "diet": "Bees, wasps, dragonflies, butterflies, beetles, and other flying insects",
        "habitat": "Open country, riverbanks, wetlands, farmland, grassland, and scrub",
        "behaviour": "Highly agile aerial hunter that catches insects in flight and returns to a perch",
        "activity": "Diurnal",
        "nesting": "Excavates a tunnel in sandy banks or soft ground, often in colonies",
        "breeding_season": "March to July",
        "clutch_size": "4–6 eggs",
        "call": "High-pitched, rapid and cheerful twittering calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: mainly eastern, northeastern and southern regions, including West Bengal, Odisha, Assam, Meghalaya, Tripura, Karnataka, Kerala, Tamil Nadu, Andhra Pradesh and Telangana; Pakistan: local; Nepal: Terai; Bangladesh: widespread; Sri Lanka: wintering and passage populations; Bhutan: southern foothills; Myanmar, Thailand, Laos, Cambodia, Vietnam, Malaysia and Indonesia: widespread."
    }
},

{
    "name": "Indian Pond Heron",
    "scientific": "Ardeola grayii",
    "description": "The Indian Pond Heron is a small, stocky heron that appears brown and streaked while standing but reveals striking white wings when it takes flight. It is one of the most familiar wetland birds in India and can be found around ponds, rice fields, marshes, canals, and even small water bodies in towns. It hunts by standing quietly and making rapid strikes at fish, frogs, insects, and other prey. Compared with the similar Cattle Egret, it is distinguished by the combination of features described above. Its preference for ponds, rice fields, marshes, canals, lakes, rivers, and wet grassland also helps separate it from species that use different habitats. Its characteristic behaviour, including usually stands motionless before making a rapid strike at prey, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "IndianPondHeron1.jpg",
    "quick_facts": {
        "family": "Ardeidae",
        "size": "40–50 cm",
        "weight": "230–350 g",
        "wingspan": "80–95 cm",
        "diet": "Fish, frogs, insects, crustaceans, lizards, and other small animals",
        "habitat": "Ponds, rice fields, marshes, canals, lakes, rivers, and wet grassland",
        "behaviour": "Usually stands motionless before making a rapid strike at prey",
        "activity": "Diurnal",
        "nesting": "Builds a stick nest in trees, shrubs, or reed beds, often in colonies",
        "breeding_season": "June to September in much of India",
        "clutch_size": "3–5 eggs",
        "call": "Usually quiet away from colonies, with harsh croaks around nesting sites",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in wetlands across nearly all states; Pakistan: widespread; Nepal: Terai; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar, Thailand, Laos, Cambodia, Vietnam and Malaysia: widespread."
    }
},
{
    "name": "Black-Crowned Night Heron",
    "scientific": "Nycticorax nycticorax",
    "description": "The Black-Crowned Night Heron is a stocky, medium-sized heron with a distinctive black crown and back, pale grey wings, and a white or pale grey body. Unlike many herons, it is most active around dusk and during the night. It often stands patiently at the edge of ponds, lakes, marshes, and wetlands before striking at fish, amphibians, insects, and other small prey. During the day, it commonly rests quietly among dense vegetation or in communal roosts. Its broad range and adaptable nature allow it to occupy a variety of wetland habitats. Compared with the similar Indian Pond Heron, it is distinguished by the combination of features described above. Its preference for freshwater wetlands, marshes, ponds, lakes, rivers, mangroves, and coastal wetlands also helps separate it from species that use different habitats. Its characteristic behaviour, including patient and stealthy hunter that often remains motionless before quickly striking at prey, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Black-CrownedNightHeron1.jpg",
    "quick_facts": {
        "family": "Ardeidae",
        "size": "58–66 cm",
        "weight": "500–1,000 g",
        "wingspan": "105–112 cm",
        "diet": "Fish, frogs, insects, crustaceans, small reptiles, and other small animals",
        "habitat": "Freshwater wetlands, marshes, ponds, lakes, rivers, mangroves, and coastal wetlands",
        "behaviour": "Patient and stealthy hunter that often remains motionless before quickly striking at prey",
        "activity": "Mostly crepuscular and nocturnal",
        "nesting": "Builds a platform nest of sticks and vegetation, often in trees, shrubs, or dense wetland colonies",
        "breeding_season": "Generally varies by region, often during the wet season or warmer months",
        "clutch_size": "3–5 eggs",
        "call": "A distinctive harsh, croaking or squawking call",
        "lifespan": "Up to around 20 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread but patchy in wetlands, especially northern plains, Northeast, central India and peninsular wetlands; Pakistan: Sindh and Punjab; Nepal: Terai; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: valleys; Myanmar, Thailand, Laos, Cambodia, Vietnam and Malaysia: widespread; Europe, Africa and the Americas: widespread."
    }
},
{
    "name": "Puff-Throated Babbler",
    "scientific": "Pellorneum ruficeps",
    "description": "The Puff-Throated Babbler is a small, ground-dwelling bird found in forests, woodland, scrub, and other areas with dense undergrowth. It has warm brown upperparts, a paler underside, and a characteristic pale throat that can appear puffed out when the bird calls or displays. It spends much of its time searching through leaf litter for insects and other small creatures, often moving through vegetation in small groups. Although it can be difficult to spot because of its secretive habits, its lively calls often reveal its presence. Compared with the similar Jungle Babbler, it is distinguished by the combination of features described above. Its preference for dense undergrowth, forests, woodland, bamboo, scrub, and plantations also helps separate it from species that use different habitats. Its characteristic behaviour, including active ground forager that searches through leaf litter and vegetation, often in small groups, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Puff-ThroatedBabbler1.jpg",
    "quick_facts": {
        "family": "Pellorneidae",
        "size": "17–18 cm",
        "weight": "30–40 g",
        "wingspan": "Approximately 20–23 cm",
        "diet": "Insects, larvae, spiders, small invertebrates, and occasionally seeds",
        "habitat": "Dense undergrowth, forests, woodland, bamboo, scrub, and plantations",
        "behaviour": "Active ground forager that searches through leaf litter and vegetation, often in small groups",
        "activity": "Diurnal",
        "nesting": "Builds a domed or ball-shaped nest close to the ground, usually among dense vegetation or leaf litter",
        "breeding_season": "Usually during the warmer and wetter months, varying across its range",
        "clutch_size": "2–4 eggs",
        "call": "A loud, repetitive and musical series of notes, often given by several birds in a group",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: mainly forested peninsular and northeastern regions, especially Maharashtra, Goa, Karnataka, Kerala, Tamil Nadu, Odisha, West Bengal, Assam and Northeast India; Nepal: foothills; Bhutan: southern forests; Bangladesh: local; Myanmar, Thailand, Laos and Cambodia: widespread."
    }
},
{
    "name": "Crimson Sunbird",
    "scientific": "Aethopyga siparaja",
    "description": "The Crimson Sunbird is a tiny, brilliantly coloured sunbird found in forests, gardens, and other areas with flowering plants. Males have vivid crimson and scarlet plumage with contrasting dark wings and a long, slender tail, while females are much duller and predominantly olive-green. It feeds mainly on nectar and small insects and is an active visitor to flowers. It can be distinguished from the similar Purple Sunbird by its brighter crimson coloration, more colourful male plumage, and generally smaller appearance. Compared with the similar Purple Sunbird, it is distinguished by the combination of features described above. Its preference for forests, forest edges, gardens, plantations, and flowering vegetation also helps separate it from species that use different habitats. Its characteristic behaviour, including active and agile; often moves rapidly between flowers and may hover briefly while feeding, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "CrimsonSunbird1.jpg",
    "quick_facts": {
        "family": "Nectariniidae",
        "size": "11–13 cm",
        "weight": "5–8 g",
        "wingspan": "15–18 cm",
        "diet": "Nectar, insects, spiders, and small fruits",
        "habitat": "Forests, forest edges, gardens, plantations, and flowering vegetation",
        "behaviour": "Active and agile; often moves rapidly between flowers and may hover briefly while feeding",
        "activity": "Diurnal",
        "nesting": "A small hanging pouch-shaped nest is built from plant fibres, moss, and other materials, usually suspended from a branch",
        "breeding_season": "Usually varies by region, often during the warmer or wetter months",
        "clutch_size": "1–3 eggs",
        "call": "A series of high-pitched, rapid and musical notes",
        "lifespan": "Up to about 8 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: Himalayan foothills and Northeast, including Uttarakhand, Sikkim, Arunachal Pradesh, Assam, Meghalaya, Nagaland, Manipur, Mizoram and Tripura, with local populations in peninsular hills; Nepal: foothills; Bhutan: widespread; Bangladesh: local; Myanmar, Thailand, Laos, Cambodia, Vietnam and Malaysia: widespread."
    }
},
{
    "name": "Golden-Fronted Leafbird",
    "scientific": "Chloropsis aurifrons",
    "description": "The Golden-Fronted Leafbird is a bright green forest bird named for the golden-yellow forehead found on many males. It has a green body, dark face markings, and a strong, slightly curved bill. These birds spend much of their time in the canopy, feeding on fruit, nectar, and insects. Their vivid plumage can make them surprisingly difficult to spot among leaves. It can be distinguished from other green leafbirds by its golden-yellow forehead and the characteristic combination of green plumage and dark facial markings. Compared with the similar Common Iora, it is distinguished by the combination of features described above. Its preference for tropical forests, forest edges, gardens, plantations, and wooded areas also helps separate it from species that use different habitats. Its characteristic behaviour, including active canopy-dweller that searches among leaves and flowers for food, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Golden-FrontedLeafbird1.jpg",
    "quick_facts": {
        "family": "Chloropseidae",
        "size": "18–20 cm",
        "weight": "25–35 g",
        "wingspan": "25–30 cm",
        "diet": "Fruit, nectar, insects, and other small invertebrates",
        "habitat": "Tropical forests, forest edges, gardens, plantations, and wooded areas",
        "behaviour": "Active canopy-dweller that searches among leaves and flowers for food",
        "activity": "Diurnal",
        "nesting": "Builds a small cup-shaped nest suspended from a thin branch",
        "breeding_season": "Mainly during the warmer and wetter months, varying geographically",
        "clutch_size": "2–3 eggs",
        "call": "A varied collection of whistles, chatters, and melodious notes",
        "lifespan": "Up to about 10 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: mainly Himalayan foothills, Northeast and peninsular forests, including Uttarakhand, West Bengal, Assam, Meghalaya, Arunachal Pradesh, Odisha, Karnataka, Kerala and Tamil Nadu; Nepal: foothills; Bhutan: widespread; Bangladesh: local; Myanmar, Thailand, Laos, Cambodia and Vietnam: widespread."
    }
},
{
    "name": "Black Bulbul",
    "scientific": "Hypsipetes leucocephalus",
    "description": "The Black Bulbul is a dark, medium-sized bulbul commonly associated with wooded hills and forests. Its plumage ranges from slate-grey to dark grey, and it has a prominent black crest and a red or orange bill and legs in many populations. It feeds on fruits and berries as well as insects and is often encountered in noisy groups moving through trees. It can be distinguished from other dark bulbuls by its prominent pointed crest, relatively large size, and bright reddish bill and legs. Compared with the similar Red-Whiskered Bulbul, it is distinguished by the combination of features described above. Its preference for hill forests, evergreen forests, forest edges, gardens, and plantations also helps separate it from species that use different habitats. Its characteristic behaviour, including social and vocal; often travels in pairs or small groups while searching through trees, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "BlackBulbul1.jpg",
    "quick_facts": {
        "family": "Pycnonotidae",
        "size": "24–25 cm",
        "weight": "30–45 g",
        "wingspan": "33–38 cm",
        "diet": "Fruits, berries, nectar, insects, and other small invertebrates",
        "habitat": "Hill forests, evergreen forests, forest edges, gardens, and plantations",
        "behaviour": "Social and vocal; often travels in pairs or small groups while searching through trees",
        "activity": "Diurnal",
        "nesting": "Builds a small cup-shaped nest using twigs, grass, moss, and plant fibres",
        "breeding_season": "Generally during spring and summer, varying by region",
        "clutch_size": "2–3 eggs",
        "call": "Loud, varied whistles and chattering calls",
        "lifespan": "Up to about 10 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: Himalayan and northeastern hill forests, including Uttarakhand, West Bengal, Sikkim, Assam, Meghalaya, Arunachal Pradesh, Nagaland, Manipur, Mizoram and Tripura, with local populations in peninsular hill ranges; Nepal: hills; Bhutan: widespread; Bangladesh: local; Myanmar: widespread."
    }
},
{
    "name": "Grey-Breasted Prinia",
    "scientific": "Prinia hodgsonii",
    "description": "The Grey-Breasted Prinia is a small, active warbler-like bird that inhabits grasslands, scrub, open woodland, and cultivated areas. It has a greyish breast, brown upperparts, and a long, narrow tail that is frequently cocked or moved as it searches for food. It usually stays close to vegetation and feeds on insects and other tiny invertebrates. Its greyish breast and relatively subdued plumage help distinguish it from the more strongly marked Ashy Prinia and the browner Plain Prinia. Compared with the similar Ashy Prinia, it is distinguished by the combination of features described above. Its preference for grasslands, scrub, open woodland, cultivated land, and forest edges also helps separate it from species that use different habitats. Its characteristic behaviour, including active and restless; moves through low vegetation and frequently flicks its tail, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Grey-BreastedPrinia1.jpg",
    "quick_facts": {
        "family": "Cisticolidae",
        "size": "11–12 cm",
        "weight": "7–10 g",
        "wingspan": "13–16 cm",
        "diet": "Insects and other small invertebrates",
        "habitat": "Grasslands, scrub, open woodland, cultivated land, and forest edges",
        "behaviour": "Active and restless; moves through low vegetation and frequently flicks its tail",
        "activity": "Diurnal",
        "nesting": "Builds a small cup-shaped nest among grasses or low vegetation",
        "breeding_season": "Usually during spring and summer, varying by region",
        "clutch_size": "3–4 eggs",
        "call": "Sharp, repetitive and rhythmic calls",
        "lifespan": "About 5 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in dry grassland and scrub, especially Rajasthan, Gujarat, Punjab, Haryana, Uttar Pradesh, Madhya Pradesh, Maharashtra, Karnataka, Telangana, Andhra Pradesh and Tamil Nadu; Pakistan: widespread; Nepal: Terai; Bangladesh: local; Sri Lanka: local."
    }
},
{
    "name": "Ashy Prinia",
    "scientific": "Prinia socialis",
    "description": "The Ashy Prinia is a familiar little bird of grasslands, gardens, scrub, farmland, and urban edges. It has greyish upperparts, pale underparts, a long tail, and a slender pointed bill. It is usually seen moving energetically through low vegetation in search of insects and is particularly noticeable because of its persistent calls. It can be distinguished from the Plain Prinia by its greyer plumage and, in breeding birds, the stronger contrast between its dark head and pale underparts. Compared with the similar Plain Prinia, it is distinguished by the combination of features described above. Its preference for grasslands, scrub, gardens, farmland, wetlands, and urban areas also helps separate it from species that use different habitats. Its characteristic behaviour, including active and restless; often moves through bushes and grasses with its tail held upright, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "AshyPrinia1.jpg",
    "quick_facts": {
        "family": "Cisticolidae",
        "size": "13–14 cm",
        "weight": "8–12 g",
        "wingspan": "14–17 cm",
        "diet": "Insects, larvae, and other small invertebrates",
        "habitat": "Grasslands, scrub, gardens, farmland, wetlands, and urban areas",
        "behaviour": "Active and restless; often moves through bushes and grasses with its tail held upright",
        "activity": "Diurnal",
        "nesting": "Builds a small nest woven into grasses or other low vegetation",
        "breeding_season": "Usually during the warmer and wetter months",
        "clutch_size": "3–5 eggs",
        "call": "A loud, repetitive and distinctive series of sharp notes",
        "lifespan": "About 5 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across most states; Pakistan: widespread; Nepal: Terai and lower hills; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar and mainland Southeast Asia: local to widespread."
    }
},
{
    "name": "Plain Prinia",
    "scientific": "Prinia inornata",
    "description": "The Plain Prinia is a small brownish bird of grasslands, marshes, agricultural fields, and scrub. Its relatively plain plumage helps it blend into dry vegetation, while its long tail and active movements make it easier to recognize. It feeds primarily on insects and frequently climbs through grasses and bushes searching for prey. It can be distinguished from the Ashy Prinia by its generally browner, less grey appearance and plainer overall plumage. Compared with the similar Ashy Prinia, it is distinguished by the combination of features described above. Its preference for grasslands, marshes, wetlands, farmland, scrub, and open woodland also helps separate it from species that use different habitats. Its characteristic behaviour, including active and secretive; searches through grasses and low vegetation and often flicks its long tail, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "PlainPrinia1.jpg",
    "quick_facts": {
        "family": "Cisticolidae",
        "size": "13–15 cm",
        "weight": "8–14 g",
        "wingspan": "14–18 cm",
        "diet": "Insects and other small invertebrates",
        "habitat": "Grasslands, marshes, wetlands, farmland, scrub, and open woodland",
        "behaviour": "Active and secretive; searches through grasses and low vegetation and often flicks its long tail",
        "activity": "Diurnal",
        "nesting": "Builds a small woven nest concealed among grass or other vegetation",
        "breeding_season": "Usually associated with the monsoon and warmer months",
        "clutch_size": "3–5 eggs",
        "call": "A repetitive, sharp and rhythmic call",
        "lifespan": "About 5 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across most states, especially grasslands, marshes and farmland; Pakistan: widespread; Nepal: Terai; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: southern foothills; Myanmar, Thailand, Laos, Cambodia and Vietnam: widespread."
    }
},
{
    "name": "Indian Bush Lark",
    "scientific": "Mirafra erythroptera",
    "description": "The Indian Bush Lark is a ground-dwelling lark of dry open country. Its brown, streaked plumage provides excellent camouflage among soil, grasses, and scrub. It spends much of its time on the ground feeding on seeds and insects, but males become especially conspicuous during the breeding season when they perform display flights and sing. It can be distinguished from similar brown larks by its compact appearance, relatively short tail, and preference for dry scrub and open ground. Compared with the similar Oriental Skylark, it is distinguished by the combination of features described above. Its preference for dry grassland, scrub, open fields, rocky plains, and semi-arid country also helps separate it from species that use different habitats. Its characteristic behaviour, including usually ground-dwelling; males perform aerial displays during breeding, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "IndianBushLark1.jpg",
    "quick_facts": {
        "family": "Alaudidae",
        "size": "15–16 cm",
        "weight": "25–35 g",
        "wingspan": "28–32 cm",
        "diet": "Seeds, grains, insects, and other small invertebrates",
        "habitat": "Dry grassland, scrub, open fields, rocky plains, and semi-arid country",
        "behaviour": "Usually ground-dwelling; males perform aerial displays during breeding",
        "activity": "Diurnal",
        "nesting": "A shallow cup-shaped nest is placed on the ground, often sheltered by grass",
        "breeding_season": "Often associated with the monsoon and local periods of increased rainfall",
        "clutch_size": "2–3 eggs",
        "call": "A melodious song delivered from the ground or during display flights",
        "lifespan": "Up to about 5 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in dry open country, especially Rajasthan, Gujarat, Maharashtra, Madhya Pradesh, Telangana, Andhra Pradesh, Karnataka and Tamil Nadu; Pakistan: Sindh and Punjab; Nepal: Terai; Sri Lanka: local; Bangladesh: local."
    }
},
{
    "name": "Oriental Skylark",
    "scientific": "Alauda gulgula",
    "description": "The Oriental Skylark is a small brown lark found in open grassland, agricultural land, and plains. Its streaked plumage provides excellent camouflage on the ground. Males are famous for their elaborate songs, often delivered during hovering or soaring display flights above the breeding territory. It can be distinguished from other small brown larks by its long, musical aerial song and characteristic crest and streaked plumage. Compared with the similar Indian Bush Lark, it is distinguished by the combination of features described above. Its preference for grasslands, agricultural fields, meadows, plains, and open country also helps separate it from species that use different habitats. Its characteristic behaviour, including usually forages on the ground; males sing during impressive aerial displays, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "OrientalSkylark1.jpg",
    "quick_facts": {
        "family": "Alaudidae",
        "size": "15–17 cm",
        "weight": "25–40 g",
        "wingspan": "28–34 cm",
        "diet": "Seeds, grains, insects, and other small invertebrates",
        "habitat": "Grasslands, agricultural fields, meadows, plains, and open country",
        "behaviour": "Usually forages on the ground; males sing during impressive aerial displays",
        "activity": "Diurnal",
        "nesting": "A cup-shaped nest is built on the ground and concealed among vegetation",
        "breeding_season": "Usually during spring and the rainy season, depending on region",
        "clutch_size": "2–4 eggs",
        "call": "A long, varied and musical song often given during flight",
        "lifespan": "Up to about 5 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in plains and open country, especially Rajasthan, Gujarat, Punjab, Haryana, Uttar Pradesh, Bihar, Madhya Pradesh, Maharashtra, West Bengal, Odisha, Karnataka, Telangana and Andhra Pradesh; Pakistan: widespread; Nepal: widespread; Bangladesh: widespread; Sri Lanka: widespread; Bhutan: valleys; Southeast and East Asia: widespread."
    }
},
{
    "name": "Common Hawk-Cuckoo",
    "scientific": "Hierococcyx varius",
    "description": "The Common Hawk-Cuckoo is a medium-sized cuckoo famous for its distinctive repeated call, which is often described as sounding like the phrase 'brain-fever'. It resembles a small hawk, with barred underparts and a long tail. It feeds mainly on insects and their larvae and is a brood parasite, laying its eggs in the nests of other birds. Its hawk-like shape and barred underparts distinguish it from many other cuckoos, while its powerful repeated call is one of its most reliable identification features. Compared with the similar Asian Koel, it is distinguished by the combination of features described above. Its preference for woodlands, gardens, plantations, forests, and tree-covered areas also helps separate it from species that use different habitats. Its characteristic behaviour, including often solitary; spends much of its time in trees and is more easily detected by its loud call, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "CommonHawk-Cuckoo1.jpg",
    "quick_facts": {
        "family": "Cuculidae",
        "size": "34–38 cm",
        "weight": "100–140 g",
        "wingspan": "50–60 cm",
        "diet": "Caterpillars, insects, larvae, and other small invertebrates",
        "habitat": "Woodlands, gardens, plantations, forests, and tree-covered areas",
        "behaviour": "Often solitary; spends much of its time in trees and is more easily detected by its loud call",
        "activity": "Diurnal",
        "nesting": "A brood parasite that lays its eggs in the nests of other bird species",
        "breeding_season": "Mainly spring and summer",
        "clutch_size": "Usually 1 egg per host nest",
        "call": "A loud, repeated 'brain-fever' call that becomes especially prominent during the breeding season",
        "lifespan": "About 6–8 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in wooded habitats, especially Himalaya, central India, Northeast and peninsular forests; Pakistan: northern foothills; Nepal: widespread; Bangladesh: widespread; Bhutan: widespread; Sri Lanka: local; Myanmar, Thailand, Laos, Cambodia and Vietnam: widespread."
    }
},
{
    "name": "Pied Cuckoo",
    "scientific": "Clamator jacobinus",
    "description": "The Pied Cuckoo is a striking black-and-white cuckoo and one of the best-known seasonal birds associated with the Indian monsoon. Its arrival and calls are traditionally linked with the beginning of the rains in many parts of India. It feeds mainly on insects and caterpillars and is a brood parasite, laying its eggs in the nests of other birds. Its bold black-and-white plumage, crest, and long tail make it easy to distinguish from the mostly brown or grey cuckoos commonly seen in India. Compared with the similar Common Hawk-Cuckoo, it is distinguished by the combination of features described above. Its preference for open woodland, scrub, gardens, farmland, and savanna-like habitats also helps separate it from species that use different habitats. Its characteristic behaviour, including often conspicuous and vocal during the monsoon; may perch openly on branches and wires, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "PiedCuckoo1.jpg",
    "quick_facts": {
        "family": "Cuculidae",
        "size": "33–35 cm",
        "weight": "100–130 g",
        "wingspan": "45–55 cm",
        "diet": "Caterpillars, insects, and other small invertebrates",
        "habitat": "Open woodland, scrub, gardens, farmland, and savanna-like habitats",
        "behaviour": "Often conspicuous and vocal during the monsoon; may perch openly on branches and wires",
        "activity": "Diurnal",
        "nesting": "A brood parasite that lays eggs in the nests of other birds, especially babblers and similar species",
        "breeding_season": "Mainly during the Indian monsoon",
        "clutch_size": "Usually 1 egg per host nest",
        "call": "A distinctive repeated call associated with the arrival of the monsoon",
        "lifespan": "About 6–8 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in the plains and open country, especially Rajasthan, Gujarat, Maharashtra, Madhya Pradesh, Uttar Pradesh, Bihar, West Bengal, Odisha, Telangana, Andhra Pradesh and Karnataka; Pakistan: widespread; Nepal: Terai; Bangladesh: widespread; Sri Lanka: local; Africa: widespread breeding and seasonal range in related populations."
    }
},
{
    "name": "Greater Flamingo",
    "scientific": "Phoenicopterus roseus",
    "description": "The Greater Flamingo is the largest flamingo species and a spectacular waterbird of shallow wetlands. Adults are predominantly pale pink and white with black wing tips, long pink legs, and a large downward-curved bill. They feed by filtering tiny organisms from shallow water and mud and often gather in large flocks. It can be distinguished from the smaller Lesser Flamingo by its much larger size, pale pink plumage, and large bill with a mostly pale base and dark tip. Compared with the similar Painted Stork, it is distinguished by the combination of features described above. Its preference for shallow lakes, lagoons, estuaries, mudflats, salt pans, and coastal wetlands also helps separate it from species that use different habitats. Its characteristic behaviour, including highly social; usually occurs in large flocks and feeds by sweeping its bill through shallow water, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "GreaterFlamingo1.jpg",
    "quick_facts": {
        "family": "Phoenicopteridae",
        "size": "120–145 cm",
        "weight": "2–4 kg",
        "wingspan": "140–165 cm",
        "diet": "Algae, small crustaceans, aquatic invertebrates, and other tiny organisms",
        "habitat": "Shallow lakes, lagoons, estuaries, mudflats, salt pans, and coastal wetlands",
        "behaviour": "Highly social; usually occurs in large flocks and feeds by sweeping its bill through shallow water",
        "activity": "Diurnal and sometimes nocturnal",
        "nesting": "Builds a raised mud mound nest in colonies, usually in shallow water or muddy areas",
        "breeding_season": "Varies geographically and depends on suitable water conditions",
        "clutch_size": "Usually 1 egg",
        "call": "Loud honking and grunting calls, especially when in large flocks",
        "lifespan": "Up to about 40 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: major wetlands and coastal lagoons, especially Gujarat, Rajasthan, Maharashtra, Goa, Karnataka, Kerala, Tamil Nadu, Andhra Pradesh, Telangana, Odisha and West Bengal; Pakistan: Sindh; Bangladesh: coastal wetlands; Sri Lanka: coastal lagoons; Nepal: occasional records; Middle East, Africa, southern Europe and Central Asia: widespread range."
    }
},
{
    "name": "Indian Courser",
    "scientific": "Cursorius coromandelicus",
    "description": "The Indian Courser is a distinctive ground-dwelling wader of dry open country. It has a slender body, long legs, a short bill, and warm brown and sandy plumage that blends into its surroundings. Unlike many waders, it is more often found far from water and runs rapidly across open ground while searching for insects. Its combination of sandy-brown plumage, long legs, short bill, and terrestrial habits helps distinguish it from more typical water-associated waders. Compared with the similar Red-Wattled Lapwing, it is distinguished by the combination of features described above. Its preference for dry plains, open scrub, sandy areas, rocky ground, and semi-arid grassland also helps separate it from species that use different habitats. Its characteristic behaviour, including fast-running and mainly terrestrial; usually searches for food while walking or running across open ground, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "IndianCourser1.jpg",
    "quick_facts": {
        "family": "Glareolidae",
        "size": "25–28 cm",
        "weight": "100–150 g",
        "wingspan": "55–65 cm",
        "diet": "Insects, beetles, grasshoppers, and other small invertebrates",
        "habitat": "Dry plains, open scrub, sandy areas, rocky ground, and semi-arid grassland",
        "behaviour": "Fast-running and mainly terrestrial; usually searches for food while walking or running across open ground",
        "activity": "Diurnal",
        "nesting": "Lays its eggs directly on bare or sparsely vegetated ground",
        "breeding_season": "Often during the warmer months and around the monsoon, depending on rainfall",
        "clutch_size": "Usually 2 eggs",
        "call": "A series of sharp whistles and calls, particularly during flight",
        "lifespan": "About 8 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: dry open country, especially Rajasthan, Gujarat, Maharashtra, Madhya Pradesh, Telangana, Andhra Pradesh, Karnataka and Tamil Nadu; Pakistan: Sindh and Punjab; Nepal: Terai; Sri Lanka: local; Bangladesh: local."
    }
},
{
    "name": "Long-Tailed Shrike",
    "scientific": "Lanius schach",
    "description": "The Long-Tailed Shrike is a striking predatory songbird with a grey head, dark eye mask, brown wings, and a long tail. It occupies open country with scattered bushes and trees, where it hunts insects, small reptiles, and occasionally small birds. Like other shrikes, it often watches from an exposed perch before dropping rapidly onto prey. Its exceptionally long tail, grey head, and dark facial mask help distinguish it from the smaller Bay-Backed Shrike and other Indian shrikes. Compared with the similar Bay-Backed Shrike, it is distinguished by the combination of features described above. Its preference for open woodland, scrub, grassland, farmland, and forest edges also helps separate it from species that use different habitats. Its characteristic behaviour, including perches conspicuously while scanning for prey and may impale food on thorns or sharp objects, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Long-TailedShrike1.jpg",
    "quick_facts": {
        "family": "Laniidae",
        "size": "25–28 cm",
        "weight": "45–70 g",
        "wingspan": "30–35 cm",
        "diet": "Insects, lizards, small birds, rodents, and other small animals",
        "habitat": "Open woodland, scrub, grassland, farmland, and forest edges",
        "behaviour": "Perches conspicuously while scanning for prey and may impale food on thorns or sharp objects",
        "activity": "Diurnal",
        "nesting": "Builds a cup-shaped nest in bushes or small trees",
        "breeding_season": "Usually spring and summer, varying by region",
        "clutch_size": "3–6 eggs",
        "call": "A mixture of harsh calls, chatters, whistles, and imitations",
        "lifespan": "Up to about 8 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in open country across most states; Pakistan: widespread; Nepal: widespread; Bangladesh: widespread; Bhutan: southern foothills; Sri Lanka: local; Myanmar, Thailand, Laos, Cambodia and Vietnam: widespread; China and Central Asia: widespread."
    }
},
{
    "name": "Bay-Backed Shrike",
    "scientific": "Lanius vittatus",
    "description": "The Bay-Backed Shrike is a small, boldly marked shrike of dry open habitats. It has a grey head, black facial mask, reddish-brown back, and pale underparts. Like other shrikes, it is an efficient predator despite its small size and often waits from a prominent perch before pursuing insects and other small animals. It can be distinguished from the Long-Tailed Shrike by its smaller size, shorter tail, and distinctive rich bay-coloured back. Compared with the similar Long-Tailed Shrike, it is distinguished by the combination of features described above. Its preference for dry scrub, thorn forest, open woodland, farmland, and semi-arid country also helps separate it from species that use different habitats. Its characteristic behaviour, including perches on exposed branches and searches for prey before making short hunting flights, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Bay-BackedShrike1.jpg",
    "quick_facts": {
        "family": "Laniidae",
        "size": "17–18 cm",
        "weight": "25–35 g",
        "wingspan": "25–30 cm",
        "diet": "Insects, lizards, small birds, and other small animals",
        "habitat": "Dry scrub, thorn forest, open woodland, farmland, and semi-arid country",
        "behaviour": "Perches on exposed branches and searches for prey before making short hunting flights",
        "activity": "Diurnal",
        "nesting": "Builds a small cup-shaped nest in thorny bushes or small trees",
        "breeding_season": "Usually spring and summer",
        "clutch_size": "3–5 eggs",
        "call": "Harsh calls, chattering notes, whistles, and imitations",
        "lifespan": "Up to about 7 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: mainly dry northern and western plains, including Rajasthan, Gujarat, Punjab, Haryana, Uttar Pradesh, Madhya Pradesh and Maharashtra; Pakistan: widespread; Nepal: Terai; Bangladesh: local; Afghanistan and parts of Central Asia: local."
    }
},
{
    "name": "Small Minivet",
    "scientific": "Pericrocotus cinnamomeus",
    "description": "The Small Minivet is a tiny, brightly coloured canopy-dwelling bird. Males have vivid orange-red markings contrasting with black and grey, while females are predominantly yellowish and grey. They are highly active and often travel through the treetops in small groups, catching insects among leaves and branches. Its small size and delicate build distinguish it from larger minivets, while the male's bright orange-red markings and the female's yellowish plumage are useful identification features. Compared with the similar Indian Paradise Flycatcher, it is distinguished by the combination of features described above. Its preference for forests, woodland, plantations, gardens, and tree-covered areas also helps separate it from species that use different habitats. Its characteristic behaviour, including active and social; often moves through the canopy in small mixed or single-species groups, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "SmallMinivet1.jpg",
    "quick_facts": {
        "family": "Campephagidae",
        "size": "15–16 cm",
        "weight": "10–15 g",
        "wingspan": "20–24 cm",
        "diet": "Insects and other small arthropods",
        "habitat": "Forests, woodland, plantations, gardens, and tree-covered areas",
        "behaviour": "Active and social; often moves through the canopy in small mixed or single-species groups",
        "activity": "Diurnal",
        "nesting": "Builds a small cup-shaped nest high in a tree, often well concealed among foliage",
        "breeding_season": "Generally spring and summer, varying geographically",
        "clutch_size": "2–3 eggs",
        "call": "High-pitched whistles and short, thin calls",
        "lifespan": "About 6 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: Himalaya, Northeast, central and peninsular forests, including Uttarakhand, West Bengal, Assam, Arunachal Pradesh, Odisha, Chhattisgarh, Maharashtra, Karnataka, Kerala and Tamil Nadu; Nepal: hills and foothills; Bhutan: widespread; Bangladesh: local; Myanmar, Thailand, Laos, Cambodia and Vietnam: widespread."
    }
},
{
    "name": "White-Browed Wagtail",
    "scientific": "Motacilla maderaspatensis",
    "description": "The White-Browed Wagtail is a striking black-and-white wagtail that is strongly associated with water and human settlements. It has a prominent white eyebrow, dark upperparts, white underparts, and a long wagging tail. It often walks along the edges of streams, ponds, and other wet areas while searching for insects. Its bold black-and-white pattern and conspicuous white eyebrow distinguish it from the Pied Bushchat and other black-and-white birds that may occur around similar habitats. Compared with the similar Indian Robin, it is distinguished by the combination of features described above. Its preference for streams, rivers, ponds, wetlands, gardens, bridges, and urban water bodies also helps separate it from species that use different habitats. Its characteristic behaviour, including frequently walks along the ground while constantly wagging its long tail, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "White-BrowedWagtail1.jpg",
    "quick_facts": {
        "family": "Motacillidae",
        "size": "21–23 cm",
        "weight": "25–35 g",
        "wingspan": "28–32 cm",
        "diet": "Insects, insect larvae, small aquatic invertebrates, and other tiny prey",
        "habitat": "Streams, rivers, ponds, wetlands, gardens, bridges, and urban water bodies",
        "behaviour": "Frequently walks along the ground while constantly wagging its long tail",
        "activity": "Diurnal",
        "nesting": "Nests in crevices, holes, ledges, bridges, buildings, or sheltered locations near water",
        "breeding_season": "Usually varies by region but often occurs during the warmer months",
        "clutch_size": "3–5 eggs",
        "call": "Sharp, ringing calls often given during flight",
        "lifespan": "About 6 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread near rivers, streams and urban water bodies, especially Kerala, Karnataka, Tamil Nadu, Maharashtra, Gujarat, Rajasthan, Uttar Pradesh, Bihar, West Bengal, Odisha, Telangana and Andhra Pradesh; Pakistan: local; Nepal: Terai; Bangladesh: local; Sri Lanka: local."
    }
},
{
    "name": "Red-Naped Ibis",
    "scientific": "Pseudibis papillosa",
    "description": "The Red-Naped Ibis is a large, dark ibis of open country, wetlands, agricultural land, and grassland. It has a long down-curved bill, long legs, and a distinctive bare red patch on the back of the neck. It often walks steadily across fields and open ground while probing the soil for insects and other food. The bare red patch on the nape, dark body, and reddish legs make it particularly easy to distinguish from other ibises found in India. Compared with the similar Black-Headed Ibis, it is distinguished by the combination of features described above. Its preference for grassland, farmland, wetlands, riverbanks, open scrub, and dry plains also helps separate it from species that use different habitats. Its characteristic behaviour, including usually forages on foot in pairs or small groups and probes soil with its long bill, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "Red-NapedIbis1.jpg",
    "quick_facts": {
        "family": "Threskiornithidae",
        "size": "60–68 cm",
        "weight": "700–900 g",
        "wingspan": "90–110 cm",
        "diet": "Insects, earthworms, frogs, small reptiles, grains, and other food items",
        "habitat": "Grassland, farmland, wetlands, riverbanks, open scrub, and dry plains",
        "behaviour": "Usually forages on foot in pairs or small groups and probes soil with its long bill",
        "activity": "Diurnal",
        "nesting": "Builds a platform nest of sticks in trees, often near water or open feeding areas",
        "breeding_season": "Usually during the monsoon and post-monsoon period",
        "clutch_size": "2–4 eggs",
        "call": "Harsh croaks and grunting calls, especially around nesting colonies",
        "lifespan": "Up to about 15 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in open country, especially Rajasthan, Gujarat, Punjab, Haryana, Uttar Pradesh, Madhya Pradesh, Maharashtra, Telangana, Andhra Pradesh and Karnataka; Pakistan: Sindh and Punjab; Nepal: Terai; Bangladesh: local; Sri Lanka: local."
    }
},
{
    "name": "White-Bellied Sea-Eagle",
    "scientific": "Icthyophaga leucogaster",
    "description": "The White-Bellied Sea-Eagle is a large and powerful raptor associated with coasts, rivers, lakes, and other water bodies. Adults have a striking white head, breast, belly, and tail contrasting with dark grey wings and back. It is an accomplished hunter that takes fish and other aquatic prey, often soaring high above its territory. Its bright white head, underparts, and tail contrasting with dark wings make it unmistakable among India's other large eagles. Compared with the similar Grey-Headed Fish Eagle, it is distinguished by the combination of features described above. Its preference for coasts, islands, rivers, lakes, reservoirs, estuaries, and large wetlands also helps separate it from species that use different habitats. Its characteristic behaviour, including often perches near water and soars on broad wings while searching for prey, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "White-BelliedSea-Eagle1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "75–85 cm",
        "weight": "2–4 kg",
        "wingspan": "180–220 cm",
        "diet": "Fish, waterbirds, reptiles, mammals, and carrion",
        "habitat": "Coasts, islands, rivers, lakes, reservoirs, estuaries, and large wetlands",
        "behaviour": "Often perches near water and soars on broad wings while searching for prey",
        "activity": "Diurnal",
        "nesting": "Builds a very large stick nest in a tall tree, cliff, or other elevated site",
        "breeding_season": "Usually varies by region, often during the dry season",
        "clutch_size": "1–3 eggs",
        "call": "High-pitched whistles and distinctive repeated calls",
        "lifespan": "Up to about 20 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: coasts and large water bodies across most coastal states, especially Gujarat, Maharashtra, Goa, Karnataka, Kerala, Tamil Nadu, Andhra Pradesh, Odisha, West Bengal, Andaman and Nicobar Islands and Lakshadweep; Pakistan: Sindh coast; Bangladesh: coastal regions; Sri Lanka: widespread; Maldives: widespread; Myanmar, Thailand, Malaysia, Indonesia, Philippines and Australia: widespread."
    }
},
{
    "name": "Lesser Adjutant",
    "scientific": "Leptoptilos javanicus",
    "description": "The Lesser Adjutant is a large stork with long legs, a long bill, and a mostly bare head and neck. It is generally less social than many other storks and is often seen standing quietly in wetlands, grasslands, or agricultural areas. It feeds on a wide range of animal matter and plays an important role as a scavenger as well as a predator. It can be distinguished from the larger Greater Adjutant by its smaller size, less massive bill, and different head and neck proportions. Compared with the similar Woolly-Necked Stork, it is distinguished by the combination of features described above. Its preference for wetlands, grasslands, marshes, riversides, agricultural land, and forest clearings also helps separate it from species that use different habitats. Its characteristic behaviour, including usually solitary or found in small groups; often stands motionless while searching for prey, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "LesserAdjutant1.jpg",
    "quick_facts": {
        "family": "Ciconiidae",
        "size": "110–120 cm",
        "weight": "4–5 kg",
        "wingspan": "210–250 cm",
        "diet": "Fish, frogs, reptiles, insects, small mammals, carrion, and other animal matter",
        "habitat": "Wetlands, grasslands, marshes, riversides, agricultural land, and forest clearings",
        "behaviour": "Usually solitary or found in small groups; often stands motionless while searching for prey",
        "activity": "Diurnal",
        "nesting": "Builds a large stick nest high in a tree, often in colonies or loose groups",
        "breeding_season": "Generally during the dry season, varying by region",
        "clutch_size": "2–4 eggs",
        "call": "Usually quiet, with occasional bill-clattering and other low sounds around colonies",
        "lifespan": "Up to about 20 years in the wild",
        "conservation_status": "Vulnerable",
        "where_to_find": "India: Northeast, eastern and peninsular wetlands, especially Assam, West Bengal, Odisha, Bihar, Jharkhand, Chhattisgarh, Maharashtra, Karnataka, Kerala and Tamil Nadu; Nepal: Terai; Bangladesh: widespread; Bhutan: southern valleys; Myanmar, Thailand, Laos, Cambodia, Vietnam and Malaysia: widespread but patchy."
    }
},
{
    "name": "Malabar Pied Hornbill",
    "scientific": "Anthracoceros coronatus",
    "description": "The Malabar Pied Hornbill is a large black-and-white hornbill of the forests of the Indian subcontinent. Its enormous bill and casque give it a distinctive appearance, while its loud calls can reveal its presence before the bird is seen. It feeds mainly on fruit but also takes insects and other small animals and plays an important role in dispersing seeds. Its large black-and-white body, massive pale bill, and prominent casque distinguish it from smaller pied hornbills and other forest hornbills. Compared with the similar Indian Grey Hornbill, it is distinguished by the combination of features described above. Its preference for tropical forests, forest edges, plantations, and wooded landscapes also helps separate it from species that use different habitats. Its characteristic behaviour, including usually found in pairs or small groups; spends much of its time in the canopy searching for fruit, provides another useful field clue. Taken together, these differences make it easier to distinguish from similar species when the bird is seen clearly.",
    "image": "MalabarPiedHornbill1.jpg",
    "quick_facts": {
        "family": "Bucerotidae",
        "size": "65–70 cm",
        "weight": "900–1,200 g",
        "wingspan": "100–120 cm",
        "diet": "Fruits, figs, insects, small reptiles, and other small animals",
        "habitat": "Tropical forests, forest edges, plantations, and wooded landscapes",
        "behaviour": "Usually found in pairs or small groups; spends much of its time in the canopy searching for fruit",
        "activity": "Diurnal",
        "nesting": "The female seals herself inside a tree cavity during incubation, leaving a narrow opening through which the male delivers food",
        "breeding_season": "Generally during the dry or early wet season, varying by region",
        "clutch_size": "1–3 eggs",
        "call": "Loud cackling, honking, and raucous calls",
        "lifespan": "Up to about 20 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: Western Ghats and associated forests, especially Maharashtra, Goa, Karnataka, Kerala and Tamil Nadu, with additional populations in central and eastern forests; Sri Lanka: local; Nepal: very local foothills; Bangladesh: local; Bhutan: southern foothills; Myanmar and mainland Southeast Asia: local to widespread."
    }
},
{
    "name": "Black-winged Stilt",
    "scientific": "Himantopus himantopus",
    "description": "The Black-winged Stilt is a slender wader with extremely long pink legs, a thin black bill, and a striking black-and-white body. It is commonly found around shallow wetlands, lakes, marshes, flooded fields, mudflats, and other areas of shallow water, where it searches for small aquatic animals. Its unusually long legs allow it to wade through water that is deeper than that used by many other small waders. Compared with the Pied Avocet, the Black-winged Stilt has a straight bill rather than the Avocet's strongly upturned bill. The Little Ringed Plover is much smaller, has much shorter legs, and has a prominent eye-ring that the Black-winged Stilt lacks. The Common Sandpiper is also considerably smaller and has a brown-and-white plumage pattern rather than the Stilt's sharply contrasting black-and-white appearance. The Black-winged Stilt is also more slender and much taller than most small shorebirds that occur in the same wetlands. Its exceptionally long pink legs, narrow straight bill, and upright shape are therefore excellent identification features. Its habit of wading through shallow water further helps distinguish it from smaller shorebirds that usually remain closer to the water's edge.",
    "image": "Black-wingedStilt1.jpg",
    "quick_facts": {
        "family": "Recurvirostridae",
        "size": "35–40 cm",
        "weight": "150–200 g",
        "wingspan": "67–83 cm",
        "diet": "Aquatic insects, crustaceans, small molluscs, worms, tadpoles, and other small aquatic invertebrates",
        "habitat": "Freshwater wetlands, marshes, lakes, flooded fields, mudflats, lagoons, and shallow coastal waters",
        "behaviour": "Active and social; often seen wading through shallow water while searching for prey",
        "activity": "Diurnal",
        "nesting": "Builds a shallow nest on the ground, usually close to shallow water",
        "breeding_season": "March–August",
        "clutch_size": "3–5 eggs",
        "call": "Sharp, repeated yapping or barking notes",
        "lifespan": "Up to around 10 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across suitable wetlands, including Rajasthan, Gujarat, Maharashtra, Goa, Karnataka, Kerala, Tamil Nadu, Andhra Pradesh, Telangana, Odisha, West Bengal, Assam, Uttar Pradesh, Bihar, Punjab, Haryana and other regions; Pakistan; Nepal; Bangladesh; Sri Lanka; Myanmar; and parts of Southeast Asia."
    }
},

{
    "name": "Eurasian Coot",
    "scientific": "Fulica atra",
    "description": "The Eurasian Coot is a dark waterbird with almost entirely black plumage, a white bill, and a distinctive white frontal shield above the bill. It is commonly found on lakes, ponds, reservoirs, marshes, and slow-moving waters, where it swims strongly and often dives for food. It has broad lobed toes rather than fully webbed feet, allowing it to walk across muddy vegetation as well as swim efficiently. Compared with the Common Moorhen, the Eurasian Coot is generally larger and darker, while the Moorhen has a red-and-yellow bill and a conspicuous white flank stripe. The Coot's white frontal shield is also much larger and more prominent than the markings of the Moorhen. Compared with the Grey-headed Swamphen, the Coot is smaller and almost entirely black rather than having the Swamphen's blue-purple plumage and massive red bill. Unlike ducks, the Coot has a rounded body, lobed toes, and a distinctive white frontal shield rather than a typical duck-shaped bill. The Little Grebe is much smaller and has a pointed bill and a different compact body shape. The combination of black plumage, white bill and frontal shield, and strong swimming ability makes the Eurasian Coot readily distinguishable from other common wetland birds.",
    "image": "EurasianCoot1.jpg",
    "quick_facts": {
        "family": "Rallidae",
        "size": "36–42 cm",
        "weight": "600–1,000 g",
        "wingspan": "75–85 cm",
        "diet": "Aquatic vegetation, algae, seeds, grasses, aquatic insects, molluscs, and other small aquatic animals",
        "habitat": "Lakes, ponds, reservoirs, marshes, wetlands, slow-moving rivers, and urban water bodies",
        "behaviour": "Strong swimmer; often dives for food and may gather in large groups on open water",
        "activity": "Diurnal",
        "nesting": "Builds a floating or waterside nest from aquatic vegetation",
        "breeding_season": "March–September",
        "clutch_size": "5–10 eggs",
        "call": "Loud, sharp, explosive calls and short repeated notes",
        "lifespan": "Up to around 15 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread, especially in northern, central and eastern wetlands, including Jammu and Kashmir, Himachal Pradesh, Uttarakhand, Punjab, Haryana, Rajasthan, Uttar Pradesh, Bihar, West Bengal, Assam, Odisha, Gujarat, Maharashtra, Karnataka, Kerala and Tamil Nadu; also found across much of Europe, North Africa and Asia."
    }
},

{
    "name": "Indian Spot-billed Duck",
    "scientific": "Anas poecilorhyncha",
    "description": "The Indian Spot-billed Duck is a large dabbling duck with a brown body, pale head and neck, and a distinctive yellow-tipped bill marked with dark patches. It is commonly found in freshwater wetlands, rivers, lakes, ponds, marshes, flooded fields, and other areas with shallow water. It feeds by dabbling in water and by grazing on vegetation, seeds, and other food on land. Compared with the Lesser Whistling Duck, the Indian Spot-billed Duck is larger and heavier, with a differently shaped bill and a more elongated body. The Lesser Whistling Duck has a more rounded head and generally warmer brown plumage, while the Spot-billed Duck has stronger contrasting markings. Compared with the Mallard, the Indian Spot-billed Duck has a distinctive spotted bill and does not show the adult male Mallard's bright green head and white neck ring. It also differs from the Gadwall, which has a more finely patterned grey body and a different bill coloration. The Indian Spot-billed Duck's yellow-tipped, dark-spotted bill is one of its most useful identification features. Its relatively large size, brown plumage, and contrasting wing markings further help distinguish it from other ducks found in Indian wetlands.",
    "image": "IndianSpot-billedDuck1.jpg",
    "quick_facts": {
        "family": "Anatidae",
        "size": "55–63 cm",
        "weight": "790–1,500 g",
        "wingspan": "83–94 cm",
        "diet": "Aquatic plants, grasses, seeds, grains, insects, molluscs, and other small aquatic animals",
        "habitat": "Freshwater lakes, ponds, rivers, marshes, flooded fields, reservoirs, and agricultural wetlands",
        "behaviour": "Usually seen singly, in pairs, or in small groups; feeds by dabbling and grazing",
        "activity": "Diurnal",
        "nesting": "Builds a concealed nest of grass and vegetation near water, often among reeds or dense vegetation",
        "breeding_season": "June–October, varying with rainfall and region",
        "clutch_size": "7–12 eggs",
        "call": "Males give soft whistles while females produce louder quacking calls",
        "lifespan": "Up to around 10 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread across much of the country, including Rajasthan, Gujarat, Maharashtra, Madhya Pradesh, Uttar Pradesh, Bihar, West Bengal, Odisha, Assam, Karnataka, Kerala, Tamil Nadu, Andhra Pradesh, Telangana and other suitable wetland regions; also found in Pakistan, Nepal, Bangladesh, Sri Lanka and parts of Myanmar."
    }
},

{
    "name": "House Sparrow",
    "scientific": "Passer domesticus",
    "description": "The House Sparrow is a small, familiar bird with a compact body, short tail, and thick conical bill adapted for eating seeds and other foods. Males have a grey crown, black bib, chestnut-brown markings, and pale cheeks, while females are more uniformly brown and lack the male's bold black markings. It is strongly associated with human settlements and commonly occurs around houses, buildings, gardens, markets, farms, and city streets. Compared with the Eurasian Tree Sparrow, the House Sparrow lacks the Tree Sparrow's prominent black cheek spot. The adult male House Sparrow also has a grey crown and black bib that give it a different head pattern from the Tree Sparrow. Compared with the Indian Silverbill, the House Sparrow has a heavier bill and lacks the Silverbill's pale rump and more delicate appearance. It also differs from the Scaly-breasted Munia, which has distinctive scale-like markings on its underparts and a smaller, more compact appearance. The House Sparrow's strong association with buildings and human settlements is another useful clue when identifying it in urban areas. Its compact body, thick bill, and characteristic male plumage make it one of the easiest small passerines to distinguish from other common seed-eating birds.",
    "image": "HouseSparrow1.jpg",
    "quick_facts": {
        "family": "Passeridae",
        "size": "14–18 cm",
        "weight": "24–40 g",
        "wingspan": "19–25 cm",
        "diet": "Seeds, grains, fruits, insects, food scraps, and other plant and animal matter",
        "habitat": "Cities, towns, villages, farmland, gardens, parks, buildings, and other human-dominated habitats",
        "behaviour": "Highly social; usually seen in pairs or groups around buildings and feeding areas",
        "activity": "Diurnal",
        "nesting": "Nests in cavities, holes, roof spaces, buildings, and other sheltered locations, using grass, feathers, and other material",
        "breeding_season": "Throughout much of the year, varying with local conditions",
        "clutch_size": "3–7 eggs",
        "call": "Repeated chirping and chattering calls",
        "lifespan": "Up to around 10 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread around towns, villages and agricultural areas across much of the country, including Kerala, Tamil Nadu, Karnataka, Maharashtra, Gujarat, Rajasthan, Uttar Pradesh, West Bengal, Assam, Punjab, Haryana, Delhi and many other regions; native across much of Europe, North Africa and Asia and introduced in several other parts of the world."
    }
},

{
    "name": "Laughing Dove",
    "scientific": "Spilopelia senegalensis",
    "description": "The Laughing Dove is a small, slender dove with a warm pinkish-brown body, a long tail, and a distinctive black-and-white spotted patch on the sides of the neck. It is commonly found in dry woodland, scrub, farmland, gardens, parks, and urban areas, where it usually feeds on seeds and grains on the ground. Its soft, rhythmic call is often heard from trees, buildings, or other elevated perches. Compared with the Spotted Dove, the Laughing Dove is smaller and more slender, and its neck markings form a relatively small black-and-white patch rather than the Spotted Dove's larger spotted collar. The Laughing Dove also has a warmer pinkish-brown appearance and a more delicate build. Compared with the Eurasian Collared Dove, it is much smaller and has a spotted neck rather than a simple black collar. It also differs from the Red Collared Dove, which is smaller and has a more distinctly reddish body with a narrow black collar. Compared with the Rock Pigeon, the Laughing Dove is slimmer, longer-tailed, and lacks the heavier body and broad wings of the pigeon. Its small size, warm coloration, spotted neck, and long tail therefore provide several reliable identification features.",
    "image": "LaughingDove1.jpg",
    "quick_facts": {
        "family": "Columbidae",
        "size": "25–27 cm",
        "weight": "90–120 g",
        "wingspan": "40–45 cm",
        "diet": "Seeds, grains, small fruits, and other plant material",
        "habitat": "Dry woodland, scrub, farmland, gardens, parks, villages, and urban areas",
        "behaviour": "Usually seen singly or in pairs while feeding on the ground; often perches on wires and trees",
        "activity": "Diurnal",
        "nesting": "Builds a small platform nest of twigs in trees, shrubs, buildings, or other sheltered locations",
        "breeding_season": "Throughout much of the year, varying by region",
        "clutch_size": "2 eggs",
        "call": "Soft, rhythmic cooing with a characteristic laughing quality",
        "lifespan": "Up to around 10 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread, especially in dry and semi-arid regions and around human settlements, including Rajasthan, Gujarat, Maharashtra, Madhya Pradesh, Uttar Pradesh, Delhi, Haryana, Punjab, Karnataka, Andhra Pradesh, Telangana, Tamil Nadu and Kerala; also found across much of the Middle East, Africa and parts of South Asia."
    }
},

{
    "name": "Blue-eared Kingfisher",
    "scientific": "Alcedo meninting",
    "description": "The Blue-eared Kingfisher is a small, brilliantly coloured kingfisher with deep blue upperparts, rich orange underparts, and a dark blue ear-covering area that gives the species its name. It is strongly associated with shaded forest streams, clear rivers, and other quiet freshwater habitats, particularly in heavily wooded areas. It usually hunts from low perches close to the water and dives quickly to capture small fish and aquatic prey. Compared with the Common Kingfisher, the Blue-eared Kingfisher generally has deeper blue upperparts and a darker ear region, while the Common Kingfisher shows a more obvious bright orange-and-blue contrast. The Blue-eared Kingfisher is also more strongly associated with shaded forest streams, whereas the Common Kingfisher frequently occurs in more open waterways. Compared with the White-throated Kingfisher, it is much smaller and lacks the large red bill, white throat, and contrasting brown-and-blue pattern of that species. It is also dramatically smaller than the Stork-billed Kingfisher, which has a massive red bill and much heavier body. Its small size, deep blue coloration, dark ear patch, and preference for shaded forest streams make it distinctive among Asian kingfishers.",
    "image": "Blue-earedKingfisher1.jpg",
    "quick_facts": {
        "family": "Alcedinidae",
        "size": "15–18 cm",
        "weight": "20–30 g",
        "wingspan": "Approximately 25–30 cm",
        "diet": "Small fish, aquatic insects, crustaceans, tadpoles, and other small aquatic animals",
        "habitat": "Shaded forest streams, clear rivers, wooded wetlands, and quiet freshwater habitats",
        "behaviour": "Usually solitary; sits quietly on low shaded perches before diving rapidly into water for prey",
        "activity": "Diurnal",
        "nesting": "Nests in tunnels excavated in earthen stream banks",
        "breeding_season": "March–July, varying by region",
        "clutch_size": "2–5 eggs",
        "call": "High-pitched, sharp and rapidly repeated notes",
        "lifespan": "Up to around 5–7 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: mainly in forested areas of the northeastern states and parts of the Western Ghats, including West Bengal, Assam, Arunachal Pradesh, Meghalaya, Nagaland, Manipur, Mizoram, Tripura, Karnataka, Kerala and Tamil Nadu; also found in Bangladesh, Myanmar, Thailand, Malaysia, Indonesia and other parts of Southeast Asia."
    }
},

{
    "name": "Little Grebe",
    "scientific": "Tachybaptus ruficollis",
    "description": "The Little Grebe is a tiny waterbird with a compact body, short neck, rounded head, and short pointed bill. During the breeding season it develops a rich chestnut throat and cheeks, while non-breeding birds are generally paler and browner. It spends much of its time swimming and diving in ponds, lakes, marshes, and other freshwater habitats, often disappearing underwater when alarmed. Compared with the Eurasian Coot, the Little Grebe is much smaller, has a pointed bill rather than a white frontal shield, and has a completely different body shape. Compared with the Indian Pond Heron, it is more compact and spends much more time swimming and diving rather than standing along the water's edge. The Little Grebe also differs from larger grebes by its much smaller size and proportionally shorter bill and neck. Unlike ducks, it has a narrow pointed bill and a streamlined body adapted for diving rather than dabbling. Its rounded body and tiny size also separate it from many other swimming birds that appear on the same ponds. Its small size, short bill, compact profile, and frequent diving behaviour therefore make it distinctive among India's freshwater birds.",
    "image": "LittleGrebe1.jpg",
    "quick_facts": {
        "family": "Podicipedidae",
        "size": "23–29 cm",
        "weight": "120–250 g",
        "wingspan": "40–45 cm",
        "diet": "Small fish, aquatic insects, crustaceans, tadpoles, molluscs, and other small aquatic animals",
        "habitat": "Freshwater ponds, lakes, marshes, reservoirs, slow-moving waterways, and vegetated wetlands",
        "behaviour": "Excellent diver; usually swims quietly and disappears underwater when disturbed",
        "activity": "Diurnal",
        "nesting": "Builds a floating platform nest from aquatic vegetation, usually hidden among reeds or other plants",
        "breeding_season": "Throughout much of the year, often influenced by rainfall and water conditions",
        "clutch_size": "3–6 eggs",
        "call": "High-pitched trilling, whistling, and repeated calls",
        "lifespan": "Up to around 10 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: widespread in suitable freshwater wetlands, including Kerala, Karnataka, Tamil Nadu, Andhra Pradesh, Telangana, Maharashtra, Gujarat, Rajasthan, Madhya Pradesh, Uttar Pradesh, Bihar, West Bengal, Assam and other regions; also found widely across Europe, Africa and Asia."
    }
},

{
    "name": "Chestnut-bellied Sandgrouse",
    "scientific": "Pterocles exustus",
    "description": "The Chestnut-bellied Sandgrouse is a medium-sized ground-dwelling bird adapted to hot, dry landscapes, with cryptic sandy-brown plumage and a distinctive chestnut-coloured belly. It is usually found in arid and semi-arid regions, including desert plains, dry scrub, rocky areas, and open grassland. It spends much of its time walking or resting on the ground and may gather in flocks, particularly around water sources. Compared with the Painted Sandgrouse, the Chestnut-bellied Sandgrouse has a different overall plumage pattern and lacks the Painted Sandgrouse's more strongly marked facial and body pattern. It is generally more uniformly sandy and cryptic, helping it blend into dry ground and desert vegetation. Compared with pigeons and doves, it has a more compact ground-bird shape, longer pointed wings, and behaviour strongly associated with open arid country. It also has short legs and a largely terrestrial lifestyle rather than the frequent tree-perching behaviour of many doves. The Chestnut-bellied Sandgrouse's cryptic plumage is particularly useful for camouflage in its dry habitat. Its combination of sandy-brown coloration, chestnut belly, compact body, and desert habitat makes it distinctive among India's dry-country birds.",
    "image": "Chestnut-belliedSandgrouse1.jpg",
    "quick_facts": {
        "family": "Pteroclidae",
        "size": "30–35 cm",
        "weight": "250–350 g",
        "wingspan": "50–60 cm",
        "diet": "Seeds, grains, grasses, and other plant material",
        "habitat": "Arid and semi-arid plains, deserts, dry scrub, rocky country, open grassland, and cultivated areas",
        "behaviour": "Usually terrestrial; often travels in flocks and visits water sources, especially during hot weather",
        "activity": "Diurnal",
        "nesting": "Lays eggs in a shallow scrape or depression on bare ground, relying on camouflage for protection",
        "breeding_season": "Varies with rainfall and local conditions, often during periods when food is available",
        "clutch_size": "2–3 eggs",
        "call": "Short, nasal or rapidly repeated flight calls",
        "lifespan": "Up to around 8 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: mainly in arid and semi-arid regions including Rajasthan, Gujarat, Haryana, Punjab, Delhi, Uttar Pradesh, Madhya Pradesh, Maharashtra, Karnataka, Andhra Pradesh and Tamil Nadu; also found in Pakistan, Afghanistan, Iran and parts of the Arabian Peninsula."
    }
},

{
    "name": "Oriental Turtle Dove",
    "scientific": "Streptopelia orientalis",
    "description": "The Oriental Turtle Dove is a medium-sized dove with a relatively long tail, pinkish-brown body, and distinctive black-and-white barred markings on the sides of the neck. It is generally associated with woodland, forest edges, farmland, scrub, gardens, and other areas with trees and open ground. It feeds mainly on seeds and grains and often forages on the ground, sometimes in small groups. Compared with the Laughing Dove, the Oriental Turtle Dove is substantially larger and has a longer, fuller body and more extensive black-and-white neck markings. The Laughing Dove has a smaller spotted neck patch and a warmer, more delicate overall appearance. Compared with the Spotted Dove, the Oriental Turtle Dove is generally larger and has more extensive barred neck markings rather than the Spotted Dove's smaller spotted collar. It also differs from the Eurasian Collared Dove, which has a cleaner pale body and a simple black neck collar rather than complex barred markings. Compared with the Red Collared Dove, the Oriental Turtle Dove is larger and less distinctly reddish, with much stronger patterned markings on the neck. Its large size, long tail, barred neck pattern, and brown overall plumage therefore provide useful identification features when several doves occur together.",
    "image": "OrientalTurtleDove1.jpg",
    "quick_facts": {
        "family": "Columbidae",
        "size": "33–35 cm",
        "weight": "200–300 g",
        "wingspan": "55–65 cm",
        "diet": "Seeds, grains, fruits, berries, and other plant material",
        "habitat": "Woodland, forest edges, farmland, scrub, gardens, parks, and open areas with scattered trees",
        "behaviour": "Usually seen singly or in pairs while feeding on the ground; may gather in small groups outside the breeding season",
        "activity": "Diurnal",
        "nesting": "Builds a simple platform nest of twigs in trees, shrubs, or other elevated locations",
        "breeding_season": "April–September, varying with region",
        "clutch_size": "2 eggs",
        "call": "Deep, rhythmic and repeated cooing",
        "lifespan": "Up to around 10 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: mainly in northern, central and northeastern regions and suitable hill and woodland habitats, including Jammu and Kashmir, Himachal Pradesh, Uttarakhand, Punjab, Haryana, Rajasthan, Uttar Pradesh, Bihar, West Bengal, Sikkim, Assam, Arunachal Pradesh and parts of the Western Ghats; also found across much of Asia, including Nepal, Bhutan, Bangladesh, China, Mongolia, Korea, Japan and Southeast Asia."
    }
},
{
"name": "House Crow",
"scientific": "Corvus splendens",
"description": "The House Crow is a highly adaptable member of the crow family that is closely associated with people and human settlements across the Indian subcontinent. It has a greyish neck and upper breast contrasting with its black head, wings, and body, giving it a distinctive two-toned appearance. It is commonly found in towns, cities, villages, agricultural areas, markets, coastal settlements, and around sources of food and human waste. Compared with the similar Large-billed Crow, the House Crow is noticeably smaller and has a much slimmer bill and body shape. Its grey neck and breast are also an important identifying feature, whereas the Large-billed Crow has a more uniformly dark appearance. The House Crow is generally more closely associated with densely populated human environments than many other crow species. Its active, opportunistic behaviour and tendency to gather around food sources further distinguish it from less urban-adapted corvids. Its characteristic calls are harsh and familiar, often heard from rooftops, trees, poles, and other structures in populated areas. Taken together, its grey neck, relatively slender build, black head and wings, and strong association with human settlements make the House Crow one of the easiest crows to identify in much of its range.",
"image": "HouseCrow1.jpg",
"quick_facts": {
"family": "Corvidae",
"size": "40–42 cm",
"weight": "250–400 g",
"wingspan": "Approximately 75–90 cm",
"diet": "Omnivorous; insects, grains, fruits, seeds, small animals, carrion, food scraps, and other human-associated food",
"habitat": "Cities, towns, villages, agricultural areas, coastal settlements, gardens, markets, and other human-dominated habitats",
"behaviour": "Highly social and adaptable; often seen in pairs or groups while feeding, roosting, or moving around human settlements",
"activity": "Diurnal",
"nesting": "Builds a bulky stick nest, usually in trees, but sometimes on buildings, poles, or other structures",
"breeding_season": "March to July, varying geographically",
"clutch_size": "3–5 eggs",
"call": "Harsh, loud and repeated cawing calls",
"lifespan": "Up to around 15 years in the wild",
"conservation_status": "Least Concern",
"where_to_find": "India: widespread across most of the country, including Punjab, Haryana, Delhi, Uttar Pradesh, Bihar, Jharkhand, West Bengal, Odisha, Assam, Gujarat, Rajasthan, Maharashtra, Goa, Karnataka, Kerala, Tamil Nadu, Andhra Pradesh, Telangana, and other populated regions; Pakistan: Punjab Province, Sindh, Khyber Pakhtunkhwa, Balochistan, and Islamabad Capital Territory; Bangladesh: Dhaka, Chattogram, Rajshahi, Khulna, Sylhet, Rangpur, Mymensingh, and Barishal divisions; Nepal: Terai and other populated lowland areas; Sri Lanka: Western, Southern, Northern, Eastern, North Western, North Central, Uva, Sabaragamuwa, and Central provinces; Maldives: Malé and other inhabited islands; also established in parts of the Middle East, East Africa, and Southeast Asia."
}
},
{
"name": "Grey Francolin",
"scientific": "Francolinus pondicerianus",
"description": "The Grey Francolin is a medium-sized ground-dwelling bird of the pheasant family found mainly in dry and open landscapes across the Indian subcontinent. It has finely barred grey and brown plumage, a reddish-brown face, and a distinctive dark-and-white pattern around the throat and neck. It is commonly seen in grasslands, scrub, agricultural fields, dry woodland, and areas of cultivated land, where it usually walks or runs through vegetation rather than flying for long distances. Compared with the similar Black Francolin, the Grey Francolin is generally paler and more finely patterned, lacking the Black Francolin's striking black-and-white male plumage. Its overall grey-brown coloration provides better camouflage in dry grasslands and scrub than the darker appearance of the Black Francolin. The Grey Francolin also has a more uniformly barred appearance across much of its body, while the Black Francolin shows stronger contrasts and distinctive white markings. Compared with the similar Painted Francolin, the Grey Francolin is less richly coloured and lacks the Painted Francolin's prominent reddish and chestnut patterning. Its preference for relatively dry open habitats also helps distinguish it from francolins that are more strongly associated with wetter grasslands or denser vegetation. Its characteristic loud, repeated calls are often heard from scrub and fields before the bird itself is spotted. These differences in plumage, habitat, behaviour, and vocalisation make the Grey Francolin relatively straightforward to separate from other similar francolins when seen or heard in suitable habitat.",
"image": "GreyFrancolin1.jpg",
"quick_facts": {
"family": "Phasianidae",
"size": "30–34 cm",
"weight": "230–340 g",
"wingspan": "Approximately 45–50 cm",
"diet": "Seeds, grains, grasses, shoots, berries, insects, and other small invertebrates",
"habitat": "Dry grasslands, scrub, agricultural fields, open woodland, plantations, and cultivated areas",
"behaviour": "Usually terrestrial and often seen in pairs or small groups; runs readily through vegetation and flies mainly when disturbed",
"activity": "Diurnal",
"nesting": "Nests in a shallow scrape on the ground, usually concealed among grass or low vegetation",
"breeding_season": "Generally March to September, varying by region",
"clutch_size": "6–9 eggs",
"call": "Loud, repeated and distinctive calls, often given by males from the ground or low vegetation",
"lifespan": "Up to around 6 years in the wild",
"conservation_status": "Least Concern",
"where_to_find": "India: widespread across much of northern, central, western, and southern India, including Punjab, Haryana, Rajasthan, Gujarat, Uttar Pradesh, Madhya Pradesh, Maharashtra, Telangana, Andhra Pradesh, Karnataka, Tamil Nadu, Kerala, Bihar, Jharkhand, Odisha, West Bengal, and other suitable dry and open regions; Pakistan: Punjab Province, Sindh, Khyber Pakhtunkhwa, and Balochistan; Nepal: mainly the Terai and lower foothills; Bangladesh: mainly western and northern regions; Sri Lanka: northern, eastern, and dry-zone regions; also present in parts of the Middle East where introduced populations have become established."
   }
},
{
"name": "European Robin",
"scientific": "Erithacus rubecula",
"description": "The European Robin is a small, familiar songbird recognized by its bright orange-red breast, brown upperparts, and pale underside. It occurs in woodland, gardens, parks, hedgerows, scrub, and other habitats with dense vegetation and suitable ground for foraging. In Britain and Ireland it is especially familiar around gardens and human settlements, while elsewhere in Europe it is strongly associated with cool, damp woodland and thick undergrowth. It feeds mainly on insects, worms, spiders, and other small invertebrates during the warmer months, while seeds and berries become more important during winter. European Robins are highly territorial and can be surprisingly aggressive toward other robins despite their small size. Compared with the similar Bluethroat, the European Robin has a much more obvious orange-red breast and lacks the Bluethroat's blue throat pattern. It can also be distinguished from the Nightingale by its orange breast, shorter tail, and more compact appearance. The female usually builds the nest in a cavity, bank, recess, or other sheltered location, sometimes surprisingly close to the ground.",
"image": "EuropeanRobin1.jpg",
"quick_facts": {
"family": "Muscicapidae",
"size": "12.5–14 cm",
"weight": "Approximately 19 g",
"wingspan": "20–22 cm",
"diet": "Insects, worms, spiders, other small invertebrates, seeds, and berries",
"habitat": "Deciduous and mixed woodland, gardens, parks, scrub, hedgerows, and shaded areas with dense undergrowth",
"behaviour": "Highly territorial; often forages on the ground and may follow people while they disturb insects and worms",
"activity": "Diurnal",
"nesting": "Cup-shaped nest built by the female in cavities, banks, recesses, roots, or other sheltered locations",
"breeding_season": "Generally March to July, varying by region",
"clutch_size": "4–5 eggs",
"call": "A varied, clear, and melodious song with sharp alarm calls",
"lifespan": "Typically around 2 years after reaching breeding age; maximum recorded age in ringing data is over 8 years",
"conservation_status": "Least Concern",
"where_to_find": "United Kingdom: England, Scotland, Wales, and Northern Ireland; Ireland; France: Brittany, Normandy, Île-de-France, Occitanie, and other suitable regions; Germany: Bavaria, Saxony, Hesse, and North Rhine-Westphalia; Spain: Galicia, Catalonia, Andalusia, and other wooded regions; Italy: Lombardy, Tuscany, Lazio, and other suitable areas; Poland: Masovia, Lesser Poland, and other wooded regions; Sweden: Götaland, Svealand, and southern Norrland; widespread across much of Europe and parts of western Asia and North Africa."
}
},

{
"name": "European Goldfinch",
"scientific": "Carduelis carduelis",
"description": "The European Goldfinch is a small and colorful finch distinguished by its bright red face, black-and-white head, brown body, and vivid yellow wing panels. It is commonly associated with lightly wooded landscapes, farmland, gardens, parks, scrub, and areas containing tall seed-producing plants. Its long, pointed bill is particularly well suited to extracting seeds from thistles, teasels, burdocks, and similar plants. Goldfinches often form flocks outside the breeding season and may gather in large numbers where abundant food is available. Compared with the European Greenfinch, the Goldfinch is smaller and much more boldly patterned, with a red face and yellow wing markings instead of the Greenfinch's predominantly green plumage. It also differs from the Common Chaffinch, which has stronger sexual differences and lacks the Goldfinch's red facial mask and yellow wing stripe. The species is widespread and adaptable and has benefited in some areas from garden feeding.",
"image": "EuropeanGoldfinch1.jpg",
"quick_facts": {
"family": "Fringillidae",
"size": "12–13.5 cm",
"weight": "Approximately 16 g",
"wingspan": "21–25.5 cm",
"diet": "Seeds, especially thistle, teasel, burdock, sunflower, and other plant seeds; insects when feeding young",
"habitat": "Open woodland, farmland, gardens, parks, scrub, villages, and areas with seed-producing plants",
"behaviour": "Social and often forms flocks outside the breeding season; frequently feeds in vegetation and at garden feeders",
"activity": "Diurnal",
"nesting": "Small cup-shaped nest built in trees or shrubs and usually concealed among foliage",
"breeding_season": "Generally April to August, varying by region",
"clutch_size": "Usually 5 eggs",
"call": "Tinkling and twittering calls; song is a rapid, musical series of notes",
"lifespan": "Typically around 2 years after reaching breeding age; maximum recorded age is over 10 years",
"conservation_status": "Least Concern",
"where_to_find": "United Kingdom: England, Scotland, Wales, and Northern Ireland; Ireland; France: Brittany, Normandy, Île-de-France, Provence, and other suitable regions; Germany: Bavaria, Hesse, Saxony, and other regions; Spain: Catalonia, Galicia, Andalusia, and other suitable areas; Italy: Lombardy, Tuscany, Sicily, and other regions; Poland: Masovia, Lesser Poland, and other regions; Sweden: Götaland, Svealand, and southern Sweden; widespread across much of Europe, western Asia, and parts of North Africa."
}
},

{
"name": "Eurasian Jay",
"scientific": "Garrulus glandarius",
"description": "The Eurasian Jay is a colorful member of the crow family, with pinkish-brown plumage, a black-and-white face, a pale rump, and a striking blue-and-black barred patch on the wings. It is primarily a woodland bird but also occurs in parks, large gardens, farmland, and other areas containing mature trees. Jays are intelligent and adaptable birds with a varied diet that includes acorns, insects, fruits, seeds, eggs, and small animals. They are particularly important in the dispersal of oak trees because they carry acorns away from parent trees and bury them for later use. Compared with the Eurasian Magpie, the Jay is shorter-tailed and more compact, with much more colorful brown, blue, and black plumage. It differs from the Western Jackdaw by its larger size, pinkish-brown body, and blue wing panel. Jays are often heard before they are seen because of their loud, harsh calls.",
"image": "EurasianJay1.jpg",
"quick_facts": {
"family": "Corvidae",
"size": "32–35 cm",
"weight": "Approximately 167 g",
"wingspan": "52–58 cm",
"diet": "Acorns, seeds, insects, fruits, eggs, nestlings, small animals, and carrion",
"habitat": "Deciduous and mixed woodland, wooded farmland, parks, large gardens, and forest edges",
"behaviour": "Intelligent, cautious, territorial, and well known for caching food such as acorns",
"activity": "Diurnal",
"nesting": "Cup-shaped nest built from twigs and lined with finer plant material, usually placed in a tree",
"breeding_season": "Generally March to July",
"clutch_size": "4–5 eggs",
"call": "Loud, harsh, rasping alarm calls; also produces quieter calls and vocal imitations",
"lifespan": "Typically around 4 years after reaching breeding age; maximum recorded age is over 16 years",
"conservation_status": "Least Concern",
"where_to_find": "United Kingdom: England, Scotland, Wales, and Northern Ireland; Ireland; France: Normandy, Brittany, Île-de-France, and other wooded regions; Germany: Bavaria, Saxony, Hesse, and other forested areas; Spain: Catalonia, Galicia, and other wooded regions; Italy: Lombardy, Tuscany, Lazio, and other regions; Poland: Masovia, Lesser Poland, and other forested areas; Sweden: Götaland, Svealand, and southern Norrland; widespread across much of Europe and parts of western Asia and North Africa."
}
},

{
"name": "Great Spotted Woodpecker",
"scientific": "Dendrocopos major",
"description": "The Great Spotted Woodpecker is a striking black-and-white woodpecker with bold red markings and a strong, chisel-shaped bill. Adults have a black back, white shoulder patches, white underparts, and red markings around the lower belly, while juveniles have a prominent red crown. It is most strongly associated with mature deciduous and mixed woodland, particularly areas containing dead or decaying trees where insects are abundant. It also eats tree seeds, nuts, and occasionally eggs or young birds. Its loud drumming is an important territorial and breeding signal and can often be heard before the bird is seen. Compared with the smaller Lesser Spotted Woodpecker, the Great Spotted Woodpecker has much more extensive black-and-white plumage and stronger red markings. It is also considerably larger than the Middle Spotted Woodpecker and has a different head pattern. Its ability to use garden feeders has helped it become a familiar bird in parts of Europe.",
"image": "GreatSpottedWoodpecker1.jpg",
"quick_facts": {
"family": "Picidae",
"size": "23–26 cm",
"weight": "Approximately 79 g",
"wingspan": "38–44 cm",
"diet": "Insects, insect larvae, tree seeds, nuts, eggs, and occasionally young birds",
"habitat": "Deciduous and mixed woodland, parks, gardens, wooded farmland, and areas with dead wood",
"behaviour": "Climbs tree trunks and branches while searching for food; drums on wood during territorial displays",
"activity": "Diurnal",
"nesting": "Cavity excavated in a tree, usually in dead or softened wood",
"breeding_season": "Generally April to June",
"clutch_size": "4–6 eggs",
"call": "Sharp calls and rapid, loud drumming",
"lifespan": "Several years; maximum recorded age in ringing data is almost 12 years",
"conservation_status": "Least Concern",
"where_to_find": "United Kingdom: England, Scotland, Wales, and Northern Ireland; Ireland; France: Brittany, Normandy, Île-de-France, and other wooded regions; Germany: Bavaria, Saxony, Hesse, and other forested areas; Spain: Galicia, Catalonia, Asturias, and other wooded regions; Italy: Lombardy, Tuscany, Veneto, and other regions; Poland: Masovia, Lesser Poland, and other forested areas; Sweden: Götaland, Svealand, and Norrland; widespread across much of Europe, North Africa, and northern Asia."
}
},

{
"name": "Common Kestrel",
"scientific": "Falco tinnunculus",
"description": "The Common Kestrel is a small falcon famous for hovering almost motionless while searching the ground for prey. It has long, pointed wings and a long tail, with males generally showing a grey head and tail while females have more extensively barred brown plumage. Kestrels mainly hunt small mammals such as voles but also take insects, reptiles, and small birds. They occur in open habitats including farmland, grassland, scrub, cliffs, and urban areas where suitable hunting grounds and nesting sites are available. Compared with the larger and more powerful Peregrine Falcon, the Common Kestrel is slimmer, smaller, and more specialized for hovering and hunting small ground prey. It also differs from the Merlin by its longer tail, broader wings, and characteristic hovering behaviour. Kestrels commonly use cavities, buildings, cliffs, and old nests rather than constructing a conventional nest of their own.",
"image": "CommonKestrel1.jpg",
"quick_facts": {
"family": "Falconidae",
"size": "32–39 cm",
"weight": "Approximately 160–290 g",
"wingspan": "65–82 cm",
"diet": "Small mammals, especially voles; insects, reptiles, and small birds",
"habitat": "Grassland, farmland, scrub, open woodland, cliffs, villages, towns, and cities",
"behaviour": "Frequently hovers while hunting and often perches on poles, trees, buildings, or other elevated positions",
"activity": "Diurnal",
"nesting": "Usually nests in cavities, buildings, cliffs, nest boxes, or abandoned nests of other birds rather than building its own nest",
"breeding_season": "Generally April to July",
"clutch_size": "Usually 4–5 eggs",
"call": "Repeated sharp 'kee-kee-kee' calls, particularly around the nest",
"lifespan": "Typical life expectancy after reaching breeding age is around 4 years; maximum recorded age is almost 16 years",
"conservation_status": "Least Concern",
"where_to_find": "United Kingdom: England, Scotland, Wales, and Northern Ireland; France: Normandy, Brittany, Provence, and other regions; Germany: Bavaria, Saxony, Hesse, and other regions; Spain: Catalonia, Andalusia, Castile, and other open regions; Italy: Lombardy, Tuscany, Sicily, and other regions; Poland: Masovia, Lesser Poland, and other regions; Sweden: Götaland, Svealand, and Norrland; Greece: Attica, Central Macedonia, and other regions; widespread across Europe, Africa, and much of Asia."
}
},

{
"name": "Common Nightingale",
"scientific": "Luscinia megarhynchos",
"description": "The Common Nightingale is a relatively plain brown songbird whose extraordinary vocal ability has made it one of Europe's most famous songbirds. It has warm brown upperparts, a reddish-brown tail, and pale underparts, with little of the bright plumage associated with many other European songbirds. Nightingales prefer dense scrub, woodland edges, hedgerows, river valleys, and other habitats with thick vegetation close to the ground. Males are famous for singing both during the day and at night during the breeding season, often from concealed positions. Compared with the European Robin, the Nightingale lacks the robin's orange-red breast and has a more reddish-brown tail. It is also much more difficult to see than the similarly sized robin because it spends much of its time hidden in dense vegetation. The species migrates between Europe and sub-Saharan Africa, making its long-distance seasonal movements an important part of its life cycle.",
"image": "CommonNightingale1.jpg",
"quick_facts": {
"family": "Muscicapidae",
"size": "15–16.5 cm",
"weight": "Approximately 21 g",
"wingspan": "Approximately 23–26 cm",
"diet": "Insects, spiders, worms, and other small invertebrates; fruit is also eaten later in the year",
"habitat": "Dense scrub, woodland edges, hedgerows, riverine vegetation, thickets, and overgrown areas",
"behaviour": "Secretive and difficult to see; males sing prominently during the breeding season",
"activity": "Diurnal and nocturnal during the breeding season",
"nesting": "Open cup nest built low to the ground among dense vegetation and leaf litter",
"breeding_season": "Generally April to July",
"clutch_size": "Usually 4–5 eggs",
"call": "A powerful, varied song containing whistles, trills, repeated phrases, and rich musical notes",
"lifespan": "Typically around 2 years after reaching breeding age; maximum recorded age is over 8 years",
"conservation_status": "Least Concern",
"where_to_find": "United Kingdom: mainly southern and eastern England; France: Île-de-France, Nouvelle-Aquitaine, Occitanie, and other suitable regions; Spain: Galicia, Castile, Andalusia, and other regions; Portugal: Lisbon, Alentejo, and other regions; Italy: Tuscany, Lazio, Lombardy, and other regions; Germany: Brandenburg, Saxony, and other suitable areas; Poland: Masovia, Lesser Poland, and other regions; migrates to sub-Saharan Africa during the non-breeding season."
}
},

{
"name": "Northern Lapwing",
"scientific": "Vanellus vanellus",
"description": "The Northern Lapwing is a distinctive plover with glossy dark green-black upperparts, white underparts, broad rounded wings, and a long, thin crest. Its striking appearance is especially noticeable during the breeding season, when males perform spectacular tumbling display flights. It breeds mainly in open grassland, farmland, moorland, and other open habitats, while outside the breeding season it may gather in large flocks on wetlands, mudflats, coastal fields, and agricultural land. It feeds mainly on earthworms, insects, larvae, and other small invertebrates. Compared with the smaller Little Ringed Plover, the Northern Lapwing is much larger, has a long crest, broader wings, and a strongly contrasting black-and-white appearance. It can also be separated from the Red-wattled Lapwing by its shorter legs, darker glossy upperparts, and long crest. Changes in land management and increased predation have contributed to breeding declines in parts of Europe.",
"image": "NorthernLapwing1.jpg",
"quick_facts": {
"family": "Charadriidae",
"size": "28–31 cm",
"weight": "Approximately 250 g",
"wingspan": "67–72 cm",
"diet": "Earthworms, insects, larvae, beetles, and other small invertebrates",
"habitat": "Grassland, farmland, moorland, wetlands, mudflats, coastal fields, and open agricultural areas",
"behaviour": "Often forms large flocks outside the breeding season and performs tumbling aerial displays during courtship",
"activity": "Diurnal",
"nesting": "Shallow scrape on the ground, usually placed in short vegetation",
"breeding_season": "Generally March to July",
"clutch_size": "Usually 4 eggs",
"call": "Distinctive nasal 'pee-wit' calls, particularly during display flights",
"lifespan": "Several years; individuals may survive considerably longer under favourable conditions",
"conservation_status": "Near Threatened",
"where_to_find": "United Kingdom: England, Scotland, Wales, and Northern Ireland; Ireland; France: Normandy, Brittany, Hauts-de-France, and other regions; Germany: Lower Saxony, Bavaria, Brandenburg, and other open regions; Netherlands: Friesland, Groningen, and other provinces; Poland: Masovia, Greater Poland, and other regions; Sweden: Götaland and Svealand; Spain: Castilla y León, Aragón, and other suitable regions; also widespread across much of central and northern Europe and parts of western Asia."
}
},

{
"name": "Eurasian Magpie",
"scientific": "Pica pica",
"description": "The Eurasian Magpie is a highly recognizable member of the crow family, with contrasting black-and-white plumage, a very long graduated tail, and glossy blue-green iridescence on its wings and tail. It is highly adaptable and occurs in farmland, woodland edges, grassland, parks, gardens, villages, and cities. Magpies are omnivorous and eat insects, seeds, fruits, small animals, eggs, carrion, and food around human settlements. Their intelligence and curiosity have made them prominent in European folklore and culture. Compared with the Eurasian Jay, the Magpie is much more strongly black and white, has a far longer tail, and lacks the Jay's blue wing patch and pinkish-brown body. It also differs from the Rook and Carrion Crow by its white belly and shoulders and its extremely long tail. Magpies construct large, distinctive domed nests and are often heard giving their repetitive, harsh calls when alarmed.",
"image": "EurasianMagpie1.jpg",
"quick_facts": {
"family": "Corvidae",
"size": "40–51 cm",
"weight": "Approximately 213 g",
"wingspan": "52–60 cm",
"diet": "Insects, seeds, fruits, small animals, eggs, nestlings, carrion, and human food",
"habitat": "Farmland, woodland edges, grassland, parks, gardens, villages, and urban areas",
"behaviour": "Intelligent, adaptable, inquisitive, and often forages on the ground; may gather in pairs or small groups",
"activity": "Diurnal",
"nesting": "Large domed nest constructed from twigs, usually with a mud-lined cup and a roof of branches",
"breeding_season": "Generally March to July",
"clutch_size": "Usually 5–6 eggs",
"call": "Loud repetitive 'chac-chac-chac' calls and other harsh vocalizations",
"lifespan": "Typical life expectancy after reaching breeding age is around 5 years; maximum recorded age is over 21 years",
"conservation_status": "Least Concern",
"where_to_find": "United Kingdom: England, Scotland, Wales, and Northern Ireland; Ireland; France: Île-de-France, Normandy, Occitanie, and other regions; Germany: Bavaria, Saxony, Hesse, and other regions; Spain: Catalonia, Madrid, Castile, and other regions; Italy: Lombardy, Piedmont, Veneto, and other regions; Poland: Masovia, Lesser Poland, and other regions; Sweden: Götaland, Svealand, and southern Norrland; widespread across much of Europe, North Africa, and Asia."
}
},

{
"name": "European Greenfinch",
"scientific": "Chloris chloris",
"description": "The European Greenfinch is a stocky finch with predominantly green and yellow plumage, a stout pale bill, and bright yellow markings on the wings and tail. It is a familiar bird of gardens, farmland, hedgerows, parks, villages, and open woodland. Greenfinches feed mainly on seeds and plant material, using their powerful bills to handle relatively large seeds. They may gather in flocks outside the breeding season and frequently visit garden feeders. Compared with the European Goldfinch, the Greenfinch is larger and lacks the Goldfinch's red face and black-and-white head, instead showing mostly green plumage with yellow wing and tail patches. It can also be distinguished from the Common Chaffinch by its greener body, heavier bill, and yellow wing markings. Greenfinch populations in some European regions have been affected by the disease trichomonosis, particularly around garden feeding sites.",
"image": "EuropeanGreenfinch1.jpg",
"quick_facts": {
"family": "Fringillidae",
"size": "14–15 cm",
"weight": "Approximately 24–34 g",
"wingspan": "24–28 cm",
"diet": "Seeds, grains, buds, berries, and some insects",
"habitat": "Gardens, farmland, hedgerows, villages, parks, scrub, and open woodland",
"behaviour": "Social and often gathers in feeding flocks; commonly visits bird feeders",
"activity": "Diurnal",
"nesting": "Cup-shaped nest made from grass, moss, roots, and other plant material, usually placed in shrubs or trees",
"breeding_season": "Generally April to August",
"clutch_size": "Usually 4–5 eggs",
"call": "Twittering calls and a characteristic long, wheezing note",
"lifespan": "Typically several years; survival can be reduced by disease in some populations",
"conservation_status": "Least Concern",
"where_to_find": "United Kingdom: England, Scotland, Wales, and Northern Ireland; Ireland; France: Brittany, Normandy, Provence, and other regions; Germany: Bavaria, Hesse, Saxony, and other regions; Spain: Galicia, Catalonia, Andalusia, and other regions; Italy: Lombardy, Tuscany, Sicily, and other regions; Poland: Masovia, Lesser Poland, and other regions; Sweden: Götaland and Svealand; widespread across much of Europe, North Africa, and western Asia."
}
},

{
"name": "Common Chaffinch",
"scientific": "Fringilla coelebs",
"description": "The Common Chaffinch is one of Europe's most familiar finches and is especially common in woodland, gardens, parks, farmland, and villages. Adult males have a blue-grey crown, pinkish-red underparts, chestnut back, and conspicuous white wing bars, while females and juveniles are more subdued brown and olive. Chaffinches feed mainly on seeds and other plant material, with insects becoming particularly important when adults feed their young. Their distinctive descending song is one of the characteristic sounds of spring in many parts of Europe. Compared with the European Greenfinch, the Chaffinch has a slimmer bill and much more strongly contrasting male plumage, while the Greenfinch is predominantly green and yellow. It differs from the European Goldfinch by lacking the red facial mask and yellow wing panels. Chaffinches often forage on the ground and can form mixed flocks with other finches outside the breeding season.",
"image": "CommonChaffinch1.jpg",
"quick_facts": {
"family": "Fringillidae",
"size": "14–16 cm",
"weight": "Approximately 22 g",
"wingspan": "24.5–28.5 cm",
"diet": "Seeds, grains, buds, plant material, and insects, especially when feeding nestlings",
"habitat": "Woodland, gardens, farmland, parks, villages, hedgerows, and areas with mature trees",
"behaviour": "Often feeds on the ground; may form mixed flocks with other finches outside the breeding season",
"activity": "Diurnal",
"nesting": "Deep cup-shaped nest decorated with moss and lichen, usually built in a fork of a tree or shrub",
"breeding_season": "Generally April to July",
"clutch_size": "Usually 4–5 eggs",
"call": "Distinctive descending song ending in a flourish, with several short contact and alarm calls",
"lifespan": "Typical life expectancy after reaching breeding age is around 3 years; maximum recorded age is almost 14 years",
"conservation_status": "Least Concern",
"where_to_find": "United Kingdom: England, Scotland, Wales, and Northern Ireland; Ireland; France: Brittany, Normandy, Île-de-France, and other regions; Germany: Bavaria, Hesse, Saxony, and other regions; Spain: Galicia, Catalonia, Andalusia, and other regions; Italy: Lombardy, Tuscany, Lazio, and other regions; Poland: Masovia, Lesser Poland, and other regions; Sweden: Götaland, Svealand, and Norrland; widespread across Europe, North Africa, and western Asia."
}
},

{
"name": "European Roller",
"scientific": "Coracias garrulus",
"description": "The European Roller is a brightly coloured migratory bird with vivid blue to turquoise plumage, a brownish back, a dark head, and striking blue and black wings. It is associated mainly with warm open landscapes such as grasslands, agricultural areas, open woodland, steppes, and forest edges, where it hunts large insects from exposed perches. The species breeds across parts of southern, central, and eastern Europe and western Asia before migrating south to sub-Saharan Africa for the non-breeding season. Compared with the Indian Roller, the European Roller has a more uniformly blue head and body and lacks the Indian Roller's darker head and neck patterning. It can also be distinguished from the Dollarbird by its different wing pattern and more extensive blue coloration. European Rollers are cavity nesters and commonly use holes in trees, cliffs, or buildings, as well as artificial nest boxes. The species has experienced substantial population declines in parts of its range, although its current global IUCN category is Least Concern.",
"image": "EuropeanRoller1.jpg",
"quick_facts": {
"family": "Coraciidae",
"size": "Approximately 29–32 cm",
"weight": "Approximately 140–190 g",
"wingspan": "Approximately 52–58 cm",
"diet": "Large insects, especially beetles, grasshoppers, crickets, and other arthropods; occasionally small reptiles, amphibians, or small mammals",
"habitat": "Open woodland, grassland, farmland, steppes, forest edges, pasture, and other warm open landscapes with suitable perches",
"behaviour": "Often hunts from exposed perches, dropping to the ground to capture prey; strongly migratory",
"activity": "Diurnal",
"nesting": "Uses natural or artificial cavities in trees, cliffs, banks, or buildings; usually does not construct a substantial nest",
"breeding_season": "Generally April to July, with egg-laying often occurring from late May to mid-June",
"clutch_size": "Usually 4–5 eggs",
"call": "Harsh, crow-like calls and repeated rasping or grating notes",
"lifespan": "Several years; generation time is estimated at around 5.6 years",
"conservation_status": "Least Concern",
"where_to_find": "Spain: Extremadura, Andalusia, Castilla y León, and other suitable regions; Portugal; France: southern regions and Mediterranean areas; Italy: Tuscany, Lazio, Sicily, and other regions; Croatia; Hungary; Romania; Bulgaria; Greece; Ukraine; Russia: southern and western regions; Turkey; Kazakhstan and other parts of western and central Asia; migrates to sub-Saharan Africa during the non-breeding season. In India it occurs mainly as a passage migrant and localized summer migrant, with records from regions including Punjab, Gujarat, Rajasthan, Maharashtra, Karnataka, Tamil Nadu, Kerala, and other suitable areas."
}
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
        "diet": "Insects, spiders, larvae, small seeds and some fruit",
        "habitat": "Open eucalypt woodland, forest edges, dense understorey, parks and gardens",
        "behaviour": "Highly social and usually seen in pairs or small family groups; forages mainly on or near the ground",
        "activity": "Diurnal",
        "nesting": "A small domed nest with a side entrance, made from grasses and spider webbing and usually placed low in dense vegetation",
        "breeding_season": "Usually September to January",
        "clutch_size": "3-4 eggs",
        "call": "Sharp, repeated contact and alarm calls",
        "lifespan": "Usually several years, with survival strongly affected by predators and environmental conditions",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: New South Wales, Victoria, Tasmania, South Australia and southeastern Queensland"
    }
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
        "diet": "Insects, reptiles, amphibians, rodents, small birds and other small animals",
        "habitat": "Open woodland, forests, forest edges, parks and areas with suitable trees",
        "behaviour": "Perch-hunts by watching from a high position before dropping onto prey; lives in family groups",
        "activity": "Diurnal",
        "nesting": "A bare chamber in a natural tree hollow or occasionally an arboreal termite mound",
        "breeding_season": "August to January",
        "clutch_size": "Usually 2-3 eggs",
        "call": "The famous loud, rolling 'laughing' call, along with shorter calls used for communication",
        "lifespan": "Can live for many years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: Queensland, New South Wales, Victoria, South Australia and eastern Tasmania; introduced populations also occur in parts of Western Australia and Tasmania"
    }
},
{
    "name": "Australian Magpie",
    "scientific": "Gymnorhina tibicen",
    "description": "The Australian Magpie is a large black-and-white songbird found across much of Australia. Despite its common name, it is not closely related to the Eurasian Magpie. Its plumage varies geographically, but adults generally have striking black-and-white patterns and a chestnut-brown eye. It is particularly famous for its complex and musical calls, which can vary considerably in pitch. Australian Magpies usually live in permanent territorial groups and spend much of their time walking across open ground searching for food. During the breeding season, some birds become strongly defensive around their nesting areas. Compared with the Eurasian Magpie, the Australian Magpie has a very different body shape, lifestyle and taxonomic family.",
    "image": "AustralianMagpie1.jpg",
    "quick_facts": {
        "family": "Artamidae",
        "size": "36-44 cm",
        "weight": "About 220-350 g",
        "wingspan": "About 55-85 cm",
        "diet": "Insects, worms, spiders, small reptiles, small mammals, seeds and other food found on the ground",
        "habitat": "Open woodland, grassland, farmland, parks, playing fields and suburban areas with nearby trees",
        "behaviour": "Territorial and highly vocal; usually forages by walking across open ground",
        "activity": "Diurnal",
        "nesting": "A platform of sticks and twigs with a bowl lined with grass and hair, usually placed in a tree",
        "breeding_season": "Mainly August to November",
        "clutch_size": "3-5 eggs",
        "call": "Complex, melodious warbling and a variety of alarm and contact calls",
        "lifespan": "Often more than 10 years, with some individuals living considerably longer",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: widespread across most states and territories except the densest forests and the most arid desert regions"
    }
},
{
    "name": "Rainbow Lorikeet",
    "scientific": "Trichoglossus haematodus",
    "description": "The Rainbow Lorikeet is a brilliantly coloured parrot with a blue head, orange-red breast, green wings and back, and a bright red bill. Its colourful plumage makes it one of the easiest Australian parrots to recognise. Rainbow Lorikeets usually travel in noisy, fast-moving flocks and gather in large communal roosts. Unlike parrots that depend heavily on seeds, they are specialised feeders on nectar and pollen, using their brush-tipped tongues to collect food from flowers. They also eat fruit, seeds and some insects. They are well adapted to urban environments and are frequently seen in gardens and tree-lined suburbs. Their vivid colours and noisy flocking behaviour make them particularly conspicuous.",
    "image": "RainbowLorikeet1.jpg",
    "quick_facts": {
        "family": "Psittaculidae",
        "size": "25-30 cm",
        "weight": "About 100-150 g",
        "wingspan": "About 40-45 cm",
        "diet": "Nectar, pollen, fruit, seeds and some insects",
        "habitat": "Rainforest, woodland, coastal forests, gardens and well-treed urban areas",
        "behaviour": "Highly social and usually travels in noisy flocks; gathers at flowering trees and communal roosts",
        "activity": "Diurnal",
        "nesting": "Uses hollows in trees, usually laying eggs on decayed wood inside the cavity",
        "breeding_season": "June to January",
        "clutch_size": "Usually 2 eggs",
        "call": "Loud screeches, chattering and rapid flock calls",
        "lifespan": "Often around 15-20 years in suitable conditions",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: Queensland, New South Wales, Victoria, northern New South Wales and northeastern Australia; introduced population around Perth, Western Australia"
    }
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
        "diet": "Mainly fallen fruit, with fungi, snails and other small animals occasionally eaten",
        "habitat": "Dense tropical rainforest, swamp forest, mangroves and nearby woodland",
        "behaviour": "Usually solitary; spends much of its time walking through forest in search of fallen fruit",
        "activity": "Diurnal, with activity varying according to conditions",
        "nesting": "A shallow scrape on the ground lined with plant material; the male incubates the eggs and raises the chicks",
        "breeding_season": "Usually June to October",
        "clutch_size": "About 4 large green eggs",
        "call": "Deep rumbling and booming sounds, often surprisingly difficult to locate",
        "lifespan": "Approximately 30 years in the wild",
        "conservation_status": "Vulnerable",
        "where_to_find": "Australia: northern Queensland, especially the Wet Tropics and Cape York Peninsula; also New Guinea and eastern Indonesia"
    }
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
        "diet": "Seeds, grains, insects and other small invertebrates",
        "habitat": "Towns, villages, farmland, open countryside and areas around buildings",
        "behaviour": "Social and often seen in groups; frequently forages on the ground and around human settlements",
        "activity": "Diurnal",
        "nesting": "Uses cavities and sheltered recesses in buildings, walls, roof spaces, posts and occasionally tree cavities",
        "breeding_season": "Usually begins in March and may continue through several successive clutches",
        "clutch_size": "3-6 eggs",
        "call": "A series of chirps and chattering contact calls typical of sparrows",
        "lifespan": "Usually a few years in the wild",
        "conservation_status": "Vulnerable",
        "where_to_find": "Italy: widespread, especially northern, central and southern Italy and Sicily; also parts of neighbouring Mediterranean regions including Malta and nearby islands"
    }
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
        "diet": "Insects, spiders, larvae and other small invertebrates",
        "habitat": "Heathland, grassland, coastal scrub, moorland and open areas with scattered bushes",
        "behaviour": "Perches prominently and makes short flights to capture prey; often seen flicking its wings and tail",
        "activity": "Diurnal",
        "nesting": "A small cup nest hidden low in vegetation, often close to the ground",
        "breeding_season": "Mainly March to June, with later broods possible",
        "clutch_size": "5-6 eggs",
        "call": "Short, sharp calls; the song is a rapid series of clicking and musical notes",
        "lifespan": "Usually a few years after reaching breeding age",
        "conservation_status": "Least Concern",
        "where_to_find": "Europe: widespread across western, central and southern Europe; also North Africa and western Asia"
    }
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
        "diet": "Bees, wasps, dragonflies and other flying insects",
        "habitat": "Warm open country, river banks, sandy cliffs, gravel pits, grassland and farmland with scattered trees",
        "behaviour": "Highly aerial; catches flying insects from the air and often returns to the same perch",
        "activity": "Diurnal",
        "nesting": "Digs a long tunnel into sandy banks, cliffs or similar exposed ground; often nests in colonies",
        "breeding_season": "May to August",
        "clutch_size": "Usually 6-7 eggs",
        "call": "A lively, rolling and frequently repeated 'pruu-pruu' type call",
        "lifespan": "Around 6 years is a commonly reported figure, though individuals can live longer",
        "conservation_status": "Least Concern",
        "where_to_find": "Europe: mainly southern and central Europe; also parts of western Asia and northern Africa. Migrates to sub-Saharan Africa for winter"
    }
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
        "diet": "Insects, amphibians, reptiles, small mammals, fish, carrion and other small animals",
        "habitat": "Grasslands, wetlands, agricultural fields, river valleys and open countryside",
        "behaviour": "Walks slowly while searching for prey; often soars using thermal currents during migration",
        "activity": "Diurnal",
        "nesting": "Large stick nest built on trees, buildings, chimneys, pylons or other elevated structures",
        "breeding_season": "Usually March to July in European breeding areas",
        "clutch_size": "Usually 3-5 eggs",
        "call": "Mostly silent; famously communicates at the nest by bill-clattering",
        "lifespan": "Can live up to about 40 years",
        "conservation_status": "Least Concern",
        "where_to_find": "Europe: widespread in southern, central and eastern Europe; also western Asia and North Africa. Migratory populations winter mainly in sub-Saharan Africa"
    }
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
        "diet": "Small seeds, buds, grasses and other plant material; insects may also be taken",
        "habitat": "Open woodland, orchards, farmland, scrub, gardens and urban green spaces",
        "behaviour": "Active and social, often foraging in small groups outside the breeding season",
        "activity": "Diurnal",
        "nesting": "A small cup nest built in shrubs or trees, usually concealed among dense vegetation",
        "breeding_season": "Usually spring and summer, with two broods commonly possible",
        "clutch_size": "3-4 eggs",
        "call": "High, rapid and somewhat buzzing notes; males produce a fast, continuous song",
        "lifespan": "Typical life expectancy around 3 years after reaching breeding age",
        "conservation_status": "Least Concern",
        "where_to_find": "Europe: especially southern and central Europe; also parts of western Asia and North Africa"
    }
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
        "diet": "Insects, worms, slugs, snails, small mammals, reptiles, frogs and birds",
        "habitat": "Woodland, forest, heathland, farmland, parks and urban areas",
        "behaviour": "Usually remains motionless during the day, relying on camouflage; hunts from perches at night",
        "activity": "Nocturnal",
        "nesting": "A small platform of sticks placed on a horizontal tree branch",
        "breeding_season": "Usually August to December",
        "clutch_size": "Usually 2-3 eggs",
        "call": "A deep, repeated booming or grunting call",
        "lifespan": "Can live for many years; captive birds have exceeded 10 years",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: widespread across mainland Australia and Tasmania, except the densest rainforests and treeless deserts"
    }
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
        "diet": "Insects and other small invertebrates",
        "habitat": "Woodland, grassland, wetlands, farmland, parks, gardens and urban areas",
        "behaviour": "Highly active insect hunter that frequently fans and flicks its tail while making short aerial flights",
        "activity": "Diurnal",
        "nesting": "A small cup-shaped nest made from grass, bark and spider web, usually placed on a horizontal branch",
        "breeding_season": "Usually July to January, with breeding possible during other periods in suitable conditions",
        "clutch_size": "Usually 2-4 eggs",
        "call": "A varied series of musical, chattering and alarm notes",
        "lifespan": "Usually several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: widespread across mainland Australia, including most states and territories; also occurs in parts of New Guinea, the Moluccas and Solomon Islands"
    }
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
        "diet": "Nectar, fruit, insects and other small invertebrates",
        "habitat": "Open forest, woodland, monsoon forest, mangroves, coastal heath, orchards and gardens",
        "behaviour": "Noisy and social, usually travelling in pairs or small groups",
        "activity": "Diurnal",
        "nesting": "A cup-shaped nest made from grass, bark and other plant fibres, usually placed in a tree or shrub",
        "breeding_season": "Usually August to January, varying with location",
        "clutch_size": "Usually 2-3 eggs",
        "call": "Loud, varied and chattering calls",
        "lifespan": "Usually several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: Queensland, New South Wales, northern Victoria and parts of the Northern Territory and Western Australia; also New Guinea and nearby islands"
    }
},
{
    "name": "Eastern Rosella",
    "scientific": "Platycercus eximius",
    "description": "The Eastern Rosella is a colourful parrot of southeastern Australia, easily recognised by its red head and breast, white cheek patches, yellow-green body and bright blue shoulders. Its striking plumage makes it one of the most recognisable rosellas. Eastern Rosellas are often seen feeding on the ground, where they use their strong bills to collect seeds, grasses and other plant material. They can also climb through trees and feed on fruits, buds and flowers. The species has adapted well to human-modified environments and is commonly seen in farmland, parks, gardens and golf courses. It is somewhat similar to the Pale-headed Rosella, but the Eastern Rosella has a strongly red head and distinctive white cheek patches.",
    "image": "EasternRosella1.jpg",
    "quick_facts": {
        "family": "Psittacidae",
        "size": "28-32 cm",
        "weight": "About 90-125 g",
        "wingspan": "About 42-48 cm",
        "diet": "Seeds, grasses, fruits, flowers, buds and insects",
        "habitat": "Open woodland, grassland, farmland, remnant bushland, parks and gardens",
        "behaviour": "Usually occurs in pairs or small groups and often feeds on the ground",
        "activity": "Diurnal",
        "nesting": "A natural tree hollow, usually containing a bed of decayed wood",
        "breeding_season": "August to January",
        "clutch_size": "Usually 4-6 eggs",
        "call": "Clear, repeated whistles and chattering calls",
        "lifespan": "Often several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: southeastern Queensland, New South Wales, Victoria and southeastern South Australia"
    }
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
        "diet": "Seeds, grains, roots, bulbs, fruits and other plant material",
        "habitat": "Open woodland, grassland, farmland, scrub, parks and urban areas",
        "behaviour": "Highly social and usually seen in pairs, family groups or large flocks",
        "activity": "Diurnal",
        "nesting": "A tree hollow lined with leaves or other material",
        "breeding_season": "Usually July to December",
        "clutch_size": "Usually 2-5 eggs",
        "call": "Loud, harsh screeches and repeated contact calls",
        "lifespan": "Can live for several decades",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: widespread across much of the continent, including all mainland states and territories"
    }
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
        "diet": "Seeds, nuts, fruits, roots, bulbs, insects and other plant material",
        "habitat": "Forest, woodland, farmland, parks and urban areas",
        "behaviour": "Highly social and intelligent; forms large flocks and uses its powerful bill for feeding and manipulating objects",
        "activity": "Diurnal",
        "nesting": "A tree hollow, often lined with decayed wood",
        "breeding_season": "Usually August to January",
        "clutch_size": "Usually 2-3 eggs",
        "call": "Very loud, harsh screeches and repeated contact calls",
        "lifespan": "Can reach about 80 years in captivity",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: mainly eastern and northern Australia, including Queensland, New South Wales and Victoria; also introduced populations in parts of Western Australia"
    }
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
        "diet": "Fish, crustaceans, tadpoles and other aquatic animals",
        "habitat": "Freshwater lakes, rivers, swamps, estuaries, coastal waters and islands",
        "behaviour": "Often feeds cooperatively in groups and is an excellent soaring bird",
        "activity": "Diurnal",
        "nesting": "A shallow scrape on the ground lined with small amounts of vegetation or feathers",
        "breeding_season": "Can breed at any time of year depending on rainfall and water conditions",
        "clutch_size": "1-3 eggs",
        "call": "Generally quiet away from breeding colonies; adults use various visual and low vocal signals",
        "lifespan": "About 10-25 years or more",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: widespread throughout the continent; also Papua New Guinea and western Indonesia"
    }
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
        "diet": "Grasses, clover, herbs and occasionally insects",
        "habitat": "Grassland, open woodland, wetlands, flooded pasture, farmland, rice fields and urban parks",
        "behaviour": "Often walks and feeds on land rather than spending long periods on open water",
        "activity": "Diurnal",
        "nesting": "Uses tree hollows, nest boxes and other cavities, often some distance from water",
        "breeding_season": "Mainly during the wetter and cooler parts of the year, varying by region",
        "clutch_size": "Usually 8-12 eggs",
        "call": "Females give a loud rising call while males have shorter, higher-pitched calls",
        "lifespan": "Usually several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: widespread, including Tasmania"
    }
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
        "diet": "Aquatic plants, seeds, molluscs, crayfish, aquatic insects and larvae",
        "habitat": "Freshwater wetlands, rivers, lakes, forest pools, tidal mudflats and coastal wetlands",
        "behaviour": "Usually feeds by dabbling and may forage on land in damp grassy areas",
        "activity": "Diurnal",
        "nesting": "Usually nests in dense vegetation near water, sometimes using tree hollows or old nests",
        "breeding_season": "Varies with rainfall and local conditions",
        "clutch_size": "Usually 8-12 eggs",
        "call": "Females produce loud quacking calls while males have quieter whistles and calls",
        "lifespan": "Usually several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: widespread throughout the continent except the most arid regions; also Tasmania and nearby islands"
    }
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
        "diet": "Insects, worms and other small invertebrates",
        "habitat": "Grassland, wetlands, farmland, mudflats, parks and open urban areas",
        "behaviour": "Highly territorial during breeding and aggressively defends nests and chicks",
        "activity": "Diurnal, with some nocturnal activity",
        "nesting": "A shallow scrape on open ground, sometimes with little or no nest lining",
        "breeding_season": "Throughout much of the year, depending on rainfall and local conditions",
        "clutch_size": "Usually 3-4 eggs",
        "call": "Loud repeated calls, especially when alarmed or defending a nest",
        "lifespan": "Usually several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: widespread, including Tasmania and many offshore islands; also New Guinea and nearby islands"
    }
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
        "diet": "Insects, seeds and fallen fruit",
        "habitat": "Rainforest, wet sclerophyll forest and drier scrub",
        "behaviour": "Forages by scratching through leaf litter; males construct and maintain large incubation mounds",
        "activity": "Diurnal",
        "nesting": "Eggs are buried in a large mound of decomposing vegetation; several females may lay in one mound",
        "breeding_season": "Mainly spring and summer, with breeding varying by region",
        "clutch_size": "Individual females lay multiple eggs over the breeding season",
        "call": "Deep booming and clucking calls",
        "lifespan": "Can live for many years",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: eastern Queensland south to New South Wales, including Cape York Peninsula and the Illawarra region"
    }
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
        "diet": "Fruits, seeds, plant shoots, insects and other small animals",
        "habitat": "Savanna woodland, sclerophyll forest, grassland and open country",
        "behaviour": "Generally solitary; can travel long distances in search of food and water",
        "activity": "Diurnal",
        "nesting": "A thick platform of grass and vegetation built on the ground",
        "breeding_season": "April to June",
        "clutch_size": "5-15 eggs",
        "call": "Deep booming, drumming and grunting sounds",
        "lifespan": "Usually around 10-20 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: widespread across much of the mainland, from coastal regions to inland areas and the Snowy Mountains"
    }
},
{
    "name": "Wedge-tailed Eagle",
    "scientific": "Aquila audax",
    "description": "The Wedge-tailed Eagle is Australia's largest living bird of prey and one of the world's largest eagles. It has long wings, fully feathered legs and a distinctive long wedge-shaped tail that gives the species its name. Adults are generally dark brown to blackish-brown, while younger birds are lighter reddish-brown and become darker as they mature. Wedge-tailed Eagles are powerful hunters but are also important scavengers, feeding on carrion when available. They spend long periods soaring on thermal air currents while searching the landscape below. Compared with the White-bellied Sea-Eagle, the Wedge-tailed Eagle has a longer, wedge-shaped tail and longer wings suited to soaring over open country.",
    "image": "Wedge-TailedEagle1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "87-105 cm",
        "weight": "Males about 3.2-4.0 kg; females about 4.2-5.3 kg",
        "wingspan": "Up to about 230 cm",
        "diet": "Rabbits, mammals, birds, reptiles and carrion",
        "habitat": "Open woodland, grassland, farmland, savanna and arid country",
        "behaviour": "Soars for long periods while searching for prey and carrion; often hunts alone or in pairs",
        "activity": "Diurnal",
        "nesting": "A very large stick nest built in a tall tree or sometimes on a cliff",
        "breeding_season": "Usually May to September",
        "clutch_size": "Usually 1-2 eggs",
        "call": "A range of whistles and high-pitched calls, especially around the nest",
        "lifespan": "Can live for more than 20 years",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: widespread across mainland Australia and Tasmania; also occurs in southern New Guinea"
    }
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
        "diet": "Small mammals, voles, lemmings, shrews, hares, grouse and other birds",
        "habitat": "Open boreal forest, forest edges, burned areas, muskeg and open coniferous woodland",
        "behaviour": "Perches prominently and hunts by sight during the day, often making rapid low flights after prey",
        "activity": "Primarily diurnal",
        "nesting": "Uses tree cavities, dead tree stubs and abandoned woodpecker holes",
        "breeding_season": "March to June",
        "clutch_size": "Usually 3-13 eggs",
        "call": "Rapid whistles and sharp repeated calls; males give prolonged series during courtship",
        "lifespan": "About 10 years is a reported average",
        "conservation_status": "Least Concern",
        "where_to_find": "Canada: most northern regions; United States: Alaska and occasionally northern states; Europe: Scandinavia and northern Russia; Asia: Siberia and adjacent northern regions"
    }
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
        "diet": "Mainly fish, with aquatic insects, crustaceans and other small aquatic animals",
        "habitat": "Freshwater lakes, rivers, swamps, lagoons, estuaries and sheltered coastal waters",
        "behaviour": "Excellent underwater swimmer; often perches with wings spread to dry after swimming",
        "activity": "Diurnal",
        "nesting": "A stick nest built in trees or shrubs over or near water, often in colonies",
        "breeding_season": "Usually variable according to rainfall and water conditions",
        "clutch_size": "Usually 2-4 eggs",
        "call": "Generally quiet; produces low grunts and other calls around breeding colonies",
        "lifespan": "Usually several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: northern, eastern and southern Australia, including Tasmania; also New Guinea and nearby islands"
    }
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
        "diet": "Fruit, insects, small reptiles, small mammals, eggs and young birds",
        "habitat": "Forest, woodland, coastal scrub, farmland, parks and suburban areas",
        "behaviour": "Intelligent and opportunistic; often forages alone or in small groups",
        "activity": "Diurnal",
        "nesting": "A bulky stick nest lined with grass and other soft material, usually placed in a tree",
        "breeding_season": "August to January",
        "clutch_size": "Usually 2-4 eggs",
        "call": "Loud, ringing and far-carrying whistles and calls",
        "lifespan": "Can live for more than 10 years",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: eastern Australia from northern Queensland to Victoria; absent from Tasmania"
    }
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
        "diet": "Nectar, fruit, insects and other small invertebrates",
        "habitat": "Open woodland, open forest, parks, gardens and suburban areas",
        "behaviour": "Extremely social and territorial; colonies aggressively mob predators and competing birds",
        "activity": "Diurnal",
        "nesting": "A small cup-shaped nest built from grass, bark and spider web in a tree or shrub",
        "breeding_season": "Usually August to January, with breeding influenced by local conditions",
        "clutch_size": "Usually 2-4 eggs",
        "call": "Loud, varied and repeated chattering calls",
        "lifespan": "Usually several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: mainly eastern and southeastern Australia, including Queensland, New South Wales, Victoria and South Australia"
    }
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
        "diet": "Insects, spiders and other small arthropods",
        "habitat": "Dry woodland, wet forest, rainforest, parks and gardens",
        "behaviour": "Often perches low and pounces onto prey on the ground; generally seen alone, in pairs or family groups",
        "activity": "Diurnal",
        "nesting": "A woven cup of bark, grass and spider web placed in a tree fork",
        "breeding_season": "July to January",
        "clutch_size": "Usually 2 eggs, with up to three clutches possible",
        "call": "High bell-like piping notes and repeated calls",
        "lifespan": "Usually several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: eastern and southeastern mainland, especially coastal and adjacent inland regions from Queensland through New South Wales to Victoria and South Australia"
    }
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
        "diet": "Insects, spiders, other arthropods and berries",
        "habitat": "Rainforest, woodland, mallee, dense scrub, parks and orchards",
        "behaviour": "Usually forages alone, searching through lower and middle vegetation for food",
        "activity": "Diurnal",
        "nesting": "A shallow bowl of twigs, grass and bark bound with spider web, placed in a shrub or tree fork",
        "breeding_season": "September to January",
        "clutch_size": "2-3 eggs",
        "call": "Strong, musical whistles including repeated high notes",
        "lifespan": "Usually several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: eastern, southern and parts of southwestern Australia, including Tasmania; also New Guinea, Indonesia, Fiji and the Solomon Islands"
    }
},
{
    "name": "Australian King-Parrot",
    "scientific": "Alisterus scapularis",
    "description": "The Australian King-Parrot is a colourful eastern Australian parrot in which the sexes are strikingly different. Adult males have a completely red head and underparts with green wings and back, while females have a green head and breast but retain red underparts. The species is usually found in rainforest and wet forest but can also visit well-treed suburbs, where it feeds on seeds and fruit. Australian King-Parrots are generally encountered in pairs or family groups and are relatively quiet compared with many cockatoos. They nest deep inside tree hollows, sometimes with the entrance high above the ground while the eggs are laid much deeper inside the cavity.",
    "image": "AustralianKing-Parrot1.jpg",
    "quick_facts": {
        "family": "Psittacidae",
        "size": "41-43 cm",
        "weight": "About 180-260 g",
        "wingspan": "About 50-60 cm",
        "diet": "Seeds, fruit, berries, flowers and other plant material",
        "habitat": "Rainforest, wet sclerophyll forest, woodland and well-treed urban areas",
        "behaviour": "Usually seen in pairs or family groups; spends much of its time foraging in trees",
        "activity": "Diurnal",
        "nesting": "A deep tree hollow containing decayed wood dust",
        "breeding_season": "September to January",
        "clutch_size": "Usually 5 eggs",
        "call": "Loud high-pitched whistles and rolling calls in flight",
        "lifespan": "Often lives for many years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: eastern coast and ranges from Queensland through New South Wales and Victoria to southeastern South Australia"
    }
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
        "diet": "Acorns, nuts, seeds, fruit, insects and small animals",
        "habitat": "Deciduous and mixed forests, woodland edges, parks, gardens and suburbs",
        "behaviour": "Intelligent and social; often carries and stores food for later use",
        "activity": "Diurnal",
        "nesting": "An open cup of twigs, roots, grass and other plant material placed in a tree or shrub",
        "breeding_season": "April to July",
        "clutch_size": "Usually 3-7 eggs",
        "call": "Loud jay calls, harsh jeers, whistles and other varied vocalisations",
        "lifespan": "Often 7-10 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Canada: southern and central provinces; United States: most eastern, central and northern states; Mexico: northern and eastern regions"
    }
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
        "diet": "Seeds, grains, berries, fruit and insects",
        "habitat": "Woodland edges, thickets, gardens, parks and suburbs",
        "behaviour": "Usually forages on the ground or in low vegetation and often occurs in pairs",
        "activity": "Diurnal",
        "nesting": "An open cup of twigs, bark, grass and plant fibres placed in dense shrubs or low trees",
        "breeding_season": "March to September",
        "clutch_size": "Usually 2-5 eggs",
        "call": "Clear whistles and sharp metallic chip calls",
        "lifespan": "Often lives 10 years or more in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Canada: southern provinces; United States: eastern, central and parts of southwestern states; Mexico: northern and eastern regions"
    }
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
        "diet": "Earthworms, insects, berries and other fruit",
        "habitat": "Woodlands, parks, lawns, gardens and urban areas",
        "behaviour": "Runs across open ground while searching for prey and often forages in flocks outside the breeding season",
        "activity": "Diurnal",
        "nesting": "A cup-shaped nest made from grass, twigs and mud, usually placed in a tree or shrub",
        "breeding_season": "April to August",
        "clutch_size": "Usually 3-5 eggs",
        "call": "Clear musical phrases and sharp alarm calls",
        "lifespan": "Often 2-6 years, with much longer lifespans recorded",
        "conservation_status": "Least Concern",
        "where_to_find": "Canada: most provinces and territories; United States: most states; Mexico: northern and mountainous regions"
    }
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
        "diet": "Seeds, especially those of thistles and sunflowers, plus some insects",
        "habitat": "Fields, meadows, woodland edges, gardens and roadsides",
        "behaviour": "Often feeds acrobatically while clinging to seedheads",
        "activity": "Diurnal",
        "nesting": "A small cup of plant fibres and down, usually placed in a shrub or low tree",
        "breeding_season": "June to August",
        "clutch_size": "Usually 4-6 eggs",
        "call": "Bright twittering calls and a distinctive flight call",
        "lifespan": "Up to about 11 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Canada: southern provinces; United States: most states; Mexico: mainly northern and central regions"
    }
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
        "diet": "Insects, caterpillars, fruit and nectar",
        "habitat": "Mature woodland, forest edges, parks and gardens",
        "behaviour": "Agile canopy forager that can hang upside down while searching for food",
        "activity": "Diurnal",
        "nesting": "A deep hanging pouch woven from plant fibres and suspended from a tree branch",
        "breeding_season": "April to August",
        "clutch_size": "Usually 3-7 eggs",
        "call": "Rich whistled song and sharp chattering calls",
        "lifespan": "Often several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Canada: southern provinces; United States: eastern and central states; Mexico and Central America during winter"
    }
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
        "diet": "Insects, spiders, berries and other fruit",
        "habitat": "Mature deciduous and mixed forests",
        "behaviour": "Usually forages in the canopy and catches insects from foliage",
        "activity": "Diurnal",
        "nesting": "A loose open cup of twigs and grass placed on a horizontal branch",
        "breeding_season": "May to July",
        "clutch_size": "Usually 3-5 eggs",
        "call": "A rich robin-like song and a distinctive harsh call",
        "lifespan": "Often several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Canada: southern Ontario, Quebec and Atlantic provinces; United States: eastern and northern states; winters mainly in northern and western South America"
    }
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
        "diet": "Berries, fruit and insects",
        "habitat": "Woodlands, orchards, farms, parks and gardens",
        "behaviour": "Highly social and often feeds in large flocks; may pass berries between individuals",
        "activity": "Diurnal",
        "nesting": "A loose cup of twigs, grass and plant fibres placed in a tree or shrub",
        "breeding_season": "June to August",
        "clutch_size": "Usually 2-6 eggs",
        "call": "High, thin and lisping whistles",
        "lifespan": "Up to about 8 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Canada: southern and central provinces; United States: most states; Mexico and Central America during winter"
    }
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
        "diet": "Seeds, insects, berries and fruit",
        "habitat": "Deciduous forests, woodland edges and shrubby areas",
        "behaviour": "Forages in foliage and on the ground; males sing conspicuously during breeding",
        "activity": "Diurnal",
        "nesting": "A loose open cup of twigs and plant material placed in a shrub or low tree",
        "breeding_season": "May to July",
        "clutch_size": "Usually 3-5 eggs",
        "call": "Rich robin-like song and sharp chink calls",
        "lifespan": "Up to about 13 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Canada: southern and central provinces; United States: northern and eastern states; winters mainly in Mexico, Central America and the Caribbean"
    }
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
        "diet": "Seeds, grains, insects and other invertebrates",
        "habitat": "Marshes, wetlands, wet meadows, grasslands and agricultural areas",
        "behaviour": "Males are strongly territorial during breeding and gather in large flocks outside the breeding season",
        "activity": "Diurnal",
        "nesting": "A cup-shaped nest woven from grasses and reeds, usually attached to vegetation",
        "breeding_season": "March to August",
        "clutch_size": "Usually 2-4 eggs",
        "call": "Distinctive nasal 'konk-a-ree' song",
        "lifespan": "Up to about 15 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Canada: most provinces; United States: most states; Mexico: northern and central regions"
    }
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
        "diet": "Mainly fish, with some crustaceans and other aquatic prey",
        "habitat": "Coasts, bays, estuaries, mangroves and coastal islands",
        "behaviour": "Often glides in groups and plunge-dives into water to catch fish",
        "activity": "Diurnal",
        "nesting": "Colonial nests made from sticks and vegetation, usually in trees, bushes or on islands",
        "breeding_season": "Varies geographically",
        "clutch_size": "Usually 2-4 eggs",
        "call": "Adults are generally quiet; young produce begging calls",
        "lifespan": "Can live for more than 30 years",
        "conservation_status": "Least Concern",
        "where_to_find": "United States: Atlantic, Gulf and Pacific coastal states; Mexico: Pacific and Gulf coasts; Central America, northern South America and Caribbean islands"
    }
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
        "diet": "Insects, spiders, worms and other small invertebrates",
        "habitat": "Moist forests, rainforests and dense woodland",
        "behaviour": "Males perform elaborate displays and both sexes scratch through leaf litter while feeding",
        "activity": "Diurnal",
        "nesting": "A large domed nest built by the female, usually close to the ground or on a bank",
        "breeding_season": "May to August",
        "clutch_size": "Usually 1 egg",
        "call": "Remarkable mimicry of birds, mammals and mechanical sounds, along with whistles and alarm calls",
        "lifespan": "Often lives for more than 15 years",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: New South Wales, Victoria and southeastern Queensland"
    }
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
        "diet": "Nectar, insects and other small invertebrates",
        "habitat": "Heathland, woodland, forest and flowering gardens",
        "behaviour": "Often hovers at flowers while using its long bill to obtain nectar",
        "activity": "Diurnal",
        "nesting": "A small cup of twigs, grass, bark and spider web placed in a tree or shrub",
        "breeding_season": "August to January",
        "clutch_size": "Usually 2 eggs",
        "call": "Short high-pitched piping notes and other soft calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: Queensland, New South Wales, Victoria, South Australia, Tasmania and Australian Capital Territory"
    }
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
        "diet": "Seeds, fruit, flowers, nectar and insects",
        "habitat": "Forests, woodlands, riverine woodland, farmland and urban areas",
        "behaviour": "Usually feeds in trees or on the ground and may occur singly, in pairs or in small groups",
        "activity": "Diurnal",
        "nesting": "A tree hollow containing decayed wood material",
        "breeding_season": "September to January",
        "clutch_size": "Usually 3-8 eggs",
        "call": "Loud whistles and harsh chattering calls",
        "lifespan": "Often lives for 10-15 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: Queensland, New South Wales, Victoria, South Australia, Western Australia and Australian Capital Territory"
    }
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
        "diet": "Nectar, insects, fruit and other plant material",
        "habitat": "Woodland, forest, coastal scrub, parks and gardens",
        "behaviour": "Active and noisy; often chases other birds away from flowering trees",
        "activity": "Diurnal",
        "nesting": "A cup-shaped nest made from twigs, grass and other vegetation, usually placed in a tree or shrub",
        "breeding_season": "July to December",
        "clutch_size": "Usually 2-3 eggs",
        "call": "Loud harsh and nasal calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: Queensland, New South Wales, Victoria, South Australia, Western Australia and Tasmania"
    }
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
        "diet": "Carrion, insects, small animals, seeds, fruit and human-associated food",
        "habitat": "Woodland, open country, farmland, parks and urban areas",
        "behaviour": "Intelligent and adaptable; often forages on the ground and occurs in pairs or small groups",
        "activity": "Diurnal",
        "nesting": "A large stick nest usually placed high in a tree",
        "breeding_season": "July to December",
        "clutch_size": "Usually 3-6 eggs",
        "call": "Deep, resonant calls often described as a drawn-out 'ah-ah-ah'",
        "lifespan": "Can live for more than 20 years",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: Western Australia, South Australia, Victoria, New South Wales and southern Queensland"
    }
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
        "diet": "Molluscs, worms, crustaceans and other intertidal invertebrates",
        "habitat": "Sandy beaches, mudflats, estuaries and coastal islands",
        "behaviour": "Uses its powerful bill to prise open or hammer shellfish",
        "activity": "Diurnal, with some feeding at night depending on tides",
        "nesting": "A simple scrape on sand, shell or gravel above the high-tide line",
        "breeding_season": "Winter to spring",
        "clutch_size": "Usually 2-3 eggs",
        "call": "Loud piping and whistling calls",
        "lifespan": "Can live for more than 20 years",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: Queensland, New South Wales, Victoria, Tasmania, South Australia, Western Australia and Northern Territory"
    }
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
        "diet": "Fish, marine invertebrates, insects, carrion and human-associated food",
        "habitat": "Coasts, beaches, estuaries, harbours, rivers, lakes and urban areas",
        "behaviour": "Highly adaptable and often gathers in large flocks",
        "activity": "Diurnal",
        "nesting": "A shallow nest made from vegetation, usually on islands, cliffs or sheltered ground",
        "breeding_season": "August to November",
        "clutch_size": "Usually 1-3 eggs",
        "call": "Loud gull-like cries and yelps",
        "lifespan": "Often lives for more than 10 years",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: all states and territories; Tasmania; New Zealand and surrounding islands"
    }
},

{
    "name": "Australian Ibis",
    "scientific": "Threskiornis molucca",
    "description": "The Australian Ibis, also known as the Australian White Ibis, is a large long-legged ibis with a mostly white body, black head and neck, and a long curved bill. It occurs naturally in wetlands, floodplains and grasslands but is also highly successful in parks and urban areas where it searches for food.",
    "image": "AustralianIbis1.jpg",
    "quick_facts": {
        "family": "Threskiornithidae",
        "size": "65-75 cm",
        "weight": "About 1.4-1.9 kg",
        "wingspan": "About 110-125 cm",
        "diet": "Insects, worms, crustaceans, frogs, fish, seeds and other food found in soil or shallow water",
        "habitat": "Wetlands, grasslands, floodplains, farmland, parks and urban areas",
        "behaviour": "Probes soil and soft mud with its long bill and is highly adaptable around people",
        "activity": "Diurnal",
        "nesting": "A stick and vegetation nest usually built in trees or wetland vegetation, often in colonies",
        "breeding_season": "Varies with rainfall and locality",
        "clutch_size": "Usually 2-4 eggs",
        "call": "Generally quiet, with grunts and low calls around colonies",
        "lifespan": "Often lives for 10-15 years",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: all states and territories; New Guinea and nearby islands"
    }
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
        "diet": "Grains, seeds, aquatic plants, insects, frogs, reptiles and small vertebrates",
        "habitat": "Wetlands, marshes, flooded fields, grasslands and agricultural areas near water",
        "behaviour": "Usually occurs in pairs or family groups and performs spectacular dancing displays",
        "activity": "Diurnal",
        "nesting": "A large mound of vegetation constructed in or beside shallow water",
        "breeding_season": "Usually during the monsoon and wet season",
        "clutch_size": "Usually 2 eggs",
        "call": "Very loud trumpeting calls often given by pairs in duet",
        "lifespan": "Can live for more than 20 years",
        "conservation_status": "Vulnerable",
        "where_to_find": "India: Uttar Pradesh, Rajasthan, Gujarat, Madhya Pradesh, Maharashtra, Bihar, Haryana, Punjab, West Bengal and other suitable regions; Nepal: Terai; Cambodia; Myanmar; northern Australia"
    }
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
        "diet": "Snakes, lizards, insects, small mammals and other small vertebrates",
        "habitat": "Open grassland, savanna and lightly wooded country",
        "behaviour": "Walks long distances while hunting and can kill prey with powerful kicks",
        "activity": "Diurnal",
        "nesting": "A large stick nest constructed in a tree or thorny shrub",
        "breeding_season": "Varies geographically, often during the dry or early wet season",
        "clutch_size": "Usually 1-3 eggs",
        "call": "Generally quiet; produces croaks, hisses and other low calls around the nest",
        "lifespan": "Can live for 10-20 years",
        "conservation_status": "Endangered",
        "where_to_find": "Africa: South Africa, Namibia, Botswana, Zimbabwe, Zambia, Kenya, Tanzania, Uganda, Ethiopia, Sudan and other sub-Saharan countries"
    }
},

{
    "name": "Orange-headed Thrush",
    "scientific": "Zoothera citrina",
    "description": "The Orange-headed Thrush is a colourful forest thrush with a bright orange head and underparts contrasting with darker wings and back. It is generally secretive and spends much of its time foraging among leaf litter on the forest floor for insects and other small prey.",
    "image": "Orange-HeadedThrush1.jpg",
    "quick_facts": {
        "family": "Turdidae",
        "size": "20-23 cm",
        "weight": "About 45-60 g",
        "wingspan": "About 33-38 cm",
        "diet": "Insects, earthworms, snails, berries and other small invertebrates",
        "habitat": "Moist forests, evergreen woodland, plantations and dense undergrowth",
        "behaviour": "Secretive ground forager that moves through leaf litter in search of prey",
        "activity": "Diurnal, especially active around dawn and dusk",
        "nesting": "A cup-shaped nest placed in a tree, shrub or other sheltered vegetation",
        "breeding_season": "Varies by region, generally during warmer or wetter months",
        "clutch_size": "Usually 2-3 eggs",
        "call": "Musical whistles and soft notes",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: Himalayan foothills, northeastern states and parts of central and southern India; Sri Lanka; Bangladesh; Bhutan; Nepal"
    }
},

{
    "name": "Malabar Whistling Thrush",
    "scientific": "Myophonus horsfieldii",
    "description": "The Malabar Whistling Thrush is a dark blue-black forest thrush of the Indian subcontinent, especially associated with the Western Ghats. It is famous for its beautiful flute-like song and is often heard before it is seen. It commonly forages around streams and shaded forest floors.",
    "image": "MalabarWhistlingThrush1.jpg",
    "quick_facts": {
        "family": "Turdidae",
        "size": "25-29 cm",
        "weight": "About 110-160 g",
        "wingspan": "About 38-42 cm",
        "diet": "Insects, worms, snails, small frogs, crustaceans and fruit",
        "habitat": "Evergreen and moist deciduous forests, streams, shaded valleys and plantations",
        "behaviour": "Often forages near streams and spends considerable time on the ground",
        "activity": "Diurnal, especially active around dawn and dusk",
        "nesting": "A cup-shaped nest built in rock crevices, tree hollows, banks or other sheltered sites",
        "breeding_season": "March to August",
        "clutch_size": "Usually 2 eggs",
        "call": "Beautiful clear whistles and flute-like phrases",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: Maharashtra, Goa, Karnataka, Kerala and Tamil Nadu, especially the Western Ghats"
    }
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
        "diet": "Mainly fruits and berries, with some insects",
        "habitat": "Evergreen forest, secondary woodland, plantations and forest edges",
        "behaviour": "Usually feeds in the canopy and may occur alone, in pairs or in small groups",
        "activity": "Diurnal",
        "nesting": "A cup-shaped nest constructed in a tree",
        "breeding_season": "Varies geographically, generally during local wet or warmer seasons",
        "clutch_size": "Usually 2 eggs",
        "call": "Clear whistles and melodious notes",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: Himalayan foothills, northeastern states and parts of the Western Ghats; Bangladesh; Bhutan; Myanmar; Thailand; Malaysia; Indonesia and the Philippines"
    }
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
        "diet": "Insects and other small arthropods",
        "habitat": "Forests, woodland, plantations, gardens and forest edges",
        "behaviour": "Actively sallies from perches to catch insects and frequently flicks its tail",
        "activity": "Diurnal",
        "nesting": "A small cup-shaped nest attached to a branch or fork, often held together with spider web",
        "breeding_season": "Generally spring and summer, varying by region",
        "clutch_size": "Usually 2-3 eggs",
        "call": "Clear high-pitched whistles and short calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: most wooded regions including Kerala, Karnataka, Tamil Nadu, Maharashtra, Odisha, West Bengal and northeastern states; Sri Lanka; Bangladesh; Nepal; Bhutan; Myanmar; Thailand; Malaysia; Indonesia and the Philippines"
    }
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
        "diet": "Insects, beetles, grasshoppers, small reptiles and other small animals",
        "habitat": "Dry scrub, open woodland, grassland, rocky ground and agricultural landscapes",
        "behaviour": "Mostly terrestrial and relies on camouflage when disturbed",
        "activity": "Crepuscular and nocturnal",
        "nesting": "A simple scrape on bare ground",
        "breeding_season": "March to July",
        "clutch_size": "Usually 2 eggs",
        "call": "Loud repeated nocturnal calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: Rajasthan, Gujarat, Maharashtra, Madhya Pradesh, Uttar Pradesh, Bihar, Odisha, Telangana, Andhra Pradesh, Karnataka, Kerala and Tamil Nadu; Nepal; Sri Lanka"
    }
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
        "diet": "Grass seeds, grains and insects",
        "habitat": "Grassland, reedbeds, agricultural fields and wetland margins",
        "behaviour": "Often moves through grasses in small groups while feeding on seeds",
        "activity": "Diurnal",
        "nesting": "A woven hanging nest made from grass and plant fibres, usually attached to tall vegetation",
        "breeding_season": "Usually during the monsoon and wet season",
        "clutch_size": "Usually 2-4 eggs",
        "call": "Short chattering and buzzing calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: northern and northeastern states including Rajasthan, Gujarat, Punjab, Haryana, Uttar Pradesh, Bihar, West Bengal and Assam; Nepal; Bangladesh"
    }
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
        "diet": "Fish, frogs, crustaceans, reptiles, birds and small mammals",
        "habitat": "Rivers, lakes, streams, wetlands and wooded areas near water",
        "behaviour": "Often hunts from a waterside perch and may plunge into shallow water for prey",
        "activity": "Mostly nocturnal and crepuscular",
        "nesting": "Uses tree hollows, rock ledges, cavities or abandoned nests",
        "breeding_season": "November to April",
        "clutch_size": "Usually 1-3 eggs",
        "call": "Deep hoots, grunts and harsh calls",
        "lifespan": "Often lives for many years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: northern, central, western, southern and northeastern regions; Sri Lanka; Nepal; Bangladesh; Pakistan and parts of Southeast Asia"
    }
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
        "diet": "Insects and other small arthropods",
        "habitat": "Open woodland, forest edges, plantations and dry scrub",
        "behaviour": "Aggressive toward intruding birds and adept at catching insects in flight",
        "activity": "Diurnal",
        "nesting": "A small cup nest placed in a tree fork",
        "breeding_season": "March to June",
        "clutch_size": "Usually 2-4 eggs",
        "call": "Varied whistles, harsh notes and imitations of other birds",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: Maharashtra, Goa, Karnataka, Kerala and Tamil Nadu; Sri Lanka"
    }
},

{
    "name": "Azure-winged Magpie",
    "scientific": "Cyanopica cooki",
    "description": "The Azure-winged Magpie is a distinctive Iberian corvid with a black cap, pale body, blue wings and a blue tail. It is highly social and often travels in noisy groups through open woodland and Mediterranean landscapes. It feeds on a wide variety of plant and animal foods.",
    "image": "Azure-WingedMagpie1.jpg",
    "quick_facts": {
        "family": "Corvidae",
        "size": "31-35 cm",
        "weight": "About 70-100 g",
        "wingspan": "About 40-45 cm",
        "diet": "Insects, fruit, seeds, grains and small animals",
        "habitat": "Open woodland, oak woodland, agricultural areas and Mediterranean landscapes",
        "behaviour": "Highly social and often forages in groups",
        "activity": "Diurnal",
        "nesting": "An open cup of twigs and plant material placed in a tree",
        "breeding_season": "April to June",
        "clutch_size": "Usually 5-7 eggs",
        "call": "Loud high-pitched chattering calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Spain: Castilla y León, Castilla-La Mancha, Extremadura, Andalusia, Madrid and other central and western regions; Portugal: central and southern regions"
    }
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
        "diet": "Insects, spiders, berries and small fruits",
        "habitat": "Mediterranean scrub, maquis, gardens, woodland edges and coastal vegetation",
        "behaviour": "Active and secretive, usually moving rapidly through dense vegetation",
        "activity": "Diurnal",
        "nesting": "A small cup nest placed low in dense shrubs",
        "breeding_season": "March to June",
        "clutch_size": "Usually 3-5 eggs",
        "call": "Fast scratchy song with harsh alarm calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Spain: Mediterranean regions and Balearic Islands; Portugal; southern France; Italy; Greece; North Africa"
    }
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
        "diet": "Rabbits, hares, marmots, birds, reptiles and other medium-sized animals",
        "habitat": "Mountains, cliffs, moorlands, open countryside and tundra",
        "behaviour": "Soars extensively and uses powerful dives and strikes to capture prey",
        "activity": "Diurnal",
        "nesting": "A large stick nest often built on cliffs or in tall trees and reused for many years",
        "breeding_season": "February to July",
        "clutch_size": "Usually 1-4 eggs",
        "call": "Usually quiet; produces high whistles and other calls around the nest",
        "lifespan": "Can live for more than 20 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Spain: Pyrenees, Cantabria, Castilla y León, Aragón, Catalonia, Andalusia and other mountainous regions; much of Europe, Asia and North America"
    }
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
        "diet": "Carrion, particularly the remains of medium and large mammals",
        "habitat": "Mountain cliffs, open countryside, dry hills and Mediterranean landscapes",
        "behaviour": "Highly social around carcasses and often soars in large groups",
        "activity": "Diurnal",
        "nesting": "A large stick nest placed on cliffs, usually in colonies",
        "breeding_season": "December to July",
        "clutch_size": "Usually 1 egg",
        "call": "Generally quiet away from colonies; produces hisses and grunts around nesting sites",
        "lifespan": "Can live for more than 30 years",
        "conservation_status": "Least Concern",
        "where_to_find": "Spain: Andalusia, Extremadura, Castilla y León, Castilla-La Mancha, Aragón and Catalonia; Portugal; France; Italy; Balkans; Turkey; Middle East and North Africa"
    }
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
        "diet": "Flying insects",
        "habitat": "Riverbanks, lakeshores, sandy cliffs, quarries and open country near water",
        "behaviour": "Highly aerial and social, often feeding in flocks over water",
        "activity": "Diurnal",
        "nesting": "A tunnel excavated in a sandy or earthen bank, ending in a nest chamber",
        "breeding_season": "April to August in much of its northern breeding range",
        "clutch_size": "Usually 3-7 eggs",
        "call": "Rapid dry chattering calls",
        "lifespan": "Can live for several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Europe, northern Asia and North America; winters mainly in Africa, South Asia and South America depending on population"
    }
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
        "diet": "Seeds, grains, shoots, leaves and insects",
        "habitat": "Dry farmland, scrub, grassland, vineyards and open Mediterranean countryside",
        "behaviour": "Mostly terrestrial and usually walks or runs when moving between feeding areas",
        "activity": "Diurnal",
        "nesting": "A shallow ground scrape lined with grass and plant material",
        "breeding_season": "April to June",
        "clutch_size": "Usually 10-16 eggs",
        "call": "Loud repeated 'chuk-chuk' and other harsh calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Spain: most regions; Portugal; southwestern France; introduced populations in parts of the United Kingdom and elsewhere"
    }
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
        "diet": "Roots, tubers, seeds, berries, insects and other invertebrates",
        "habitat": "Mountain forests, alpine meadows and rhododendron and conifer zones",
        "behaviour": "Usually forages on the ground by digging through soil and leaf litter",
        "activity": "Diurnal",
        "nesting": "A simple ground nest concealed among vegetation",
        "breeding_season": "April to August",
        "clutch_size": "Usually 4-6 eggs",
        "call": "Loud whistles and harsh alarm calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: Jammu and Kashmir, Himachal Pradesh, Uttarakhand, Sikkim and Arunachal Pradesh; Nepal; Bhutan; northern Myanmar; Pakistan"
    }
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
        "diet": "Seeds, grains and insects",
        "habitat": "Grassland, scrub, agricultural fields and open woodland",
        "behaviour": "Often feeds on the ground and perches prominently during the breeding season",
        "activity": "Diurnal",
        "nesting": "A cup-shaped nest placed on or close to the ground in vegetation",
        "breeding_season": "April to July",
        "clutch_size": "Usually 3-5 eggs",
        "call": "Short metallic notes and a simple song",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: northern and northeastern regions including Himachal Pradesh, Uttarakhand, Rajasthan, Gujarat, Madhya Pradesh and Uttar Pradesh; Nepal; Bhutan; Bangladesh; Myanmar"
    }
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
        "diet": "Bees, wasps, dragonflies, butterflies and other flying insects",
        "habitat": "Open woodland, forest edges, scrub, plantations and grassland near suitable nesting banks",
        "behaviour": "Perches conspicuously before making aerial sallies to catch insects",
        "activity": "Diurnal",
        "nesting": "Excavates a tunnel in a sandy bank or other soft substrate",
        "breeding_season": "Varies geographically",
        "clutch_size": "Usually 2-5 eggs",
        "call": "High-pitched rapid chattering calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "India: mainly northeastern regions; Bangladesh; Myanmar; Thailand; Cambodia; Vietnam; Malaysia; Indonesia and the Philippines"
    }
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
        "diet": "Seeds, grains, leaves, berries and insects",
        "habitat": "Mountain forests, woodland edges, dense scrub and bamboo thickets",
        "behaviour": "Mostly terrestrial and feeds by scratching through leaf litter and vegetation",
        "activity": "Diurnal",
        "nesting": "A ground nest hidden among dense vegetation",
        "breeding_season": "April to June",
        "clutch_size": "Usually 8-12 eggs",
        "call": "Short whistles and harsh alarm calls",
        "lifespan": "Often lives for several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "China: Sichuan, Gansu, Shaanxi, Hubei and other central and western provinces; introduced populations occur in parts of the United Kingdom and elsewhere"
    }
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
        "diet": "Seeds, grains and other plant material",
        "habitat": "Open woodland, grassland, farmland, scrubland, parks and urban areas",
        "behaviour": "Usually forages on the ground and may gather around water sources",
        "activity": "Diurnal",
        "nesting": "A small platform of twigs placed in a tree or shrub",
        "breeding_season": "Usually throughout much of the year when conditions are favourable",
        "clutch_size": "Usually 2 eggs",
        "call": "Soft cooing calls and a distinctive whistling wing sound during flight",
        "lifespan": "Often several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: widespread across most mainland states and territories, including Queensland, New South Wales, Victoria, South Australia, Western Australia and the Northern Territory"
    }
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
        "diet": "Insects, worms and other small invertebrates",
        "habitat": "Wetlands, grassland, farmland, open woodland, parks and gardens",
        "behaviour": "Territorial and usually seen alone or in pairs while foraging on the ground",
        "activity": "Diurnal",
        "nesting": "A distinctive bowl-shaped mud nest built on a tree branch",
        "breeding_season": "Usually throughout much of the year, depending on conditions",
        "clutch_size": "Usually 3-5 eggs",
        "call": "Clear, ringing calls often given by both members of a pair",
        "lifespan": "Often several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: widespread across Queensland, New South Wales, Victoria, South Australia, Western Australia and the Northern Territory; also found in Tasmania"
    }
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
        "diet": "Insects, caterpillars, fruits and other small food items",
        "habitat": "Open woodland, forest edges, farmland, parks and gardens",
        "behaviour": "Often perches upright on exposed branches and forages among foliage",
        "activity": "Diurnal",
        "nesting": "A small, shallow nest constructed from plant material and spider web",
        "breeding_season": "Usually spring and summer",
        "clutch_size": "Usually 2-4 eggs",
        "call": "Soft, musical and chattering calls",
        "lifespan": "Often several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: widespread across Queensland, New South Wales, Victoria, South Australia, Western Australia, the Northern Territory and Tasmania"
    }
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
        "diet": "Insects, small reptiles, small birds and other small animals",
        "habitat": "Woodland, open forest, farmland, parks and suburban gardens",
        "behaviour": "Hunts from exposed perches and often returns to regular lookout points",
        "activity": "Diurnal",
        "nesting": "A cup-shaped nest made from twigs, grass and other plant material",
        "breeding_season": "Usually July to January",
        "clutch_size": "Usually 2-4 eggs",
        "call": "Rich whistles, warbling notes and varied musical calls",
        "lifespan": "Often several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: widespread across Queensland, New South Wales, Victoria, South Australia and Western Australia, with additional populations in Tasmania"
    }
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
        "diet": "Grass seeds and other seeds, with occasional plant material",
        "habitat": "Grassland, open woodland, scrubland and dry interior landscapes",
        "behaviour": "Highly social and often gathers in large flocks around food and water",
        "activity": "Diurnal",
        "nesting": "A natural tree hollow or similar cavity",
        "breeding_season": "Mainly after rainfall when food is plentiful",
        "clutch_size": "Usually 4-6 eggs",
        "call": "Continuous cheerful chirping and chattering calls in flight and around feeding areas",
        "lifespan": "Often 5-10 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: widespread across Queensland, New South Wales, Victoria, South Australia, Western Australia and the Northern Territory, particularly across the interior"
    }
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
        "diet": "Grass seeds, grains, fruits and other plant material",
        "habitat": "Open woodland, grassland, scrubland and dry inland areas",
        "behaviour": "Highly social and often travels in pairs or large flocks",
        "activity": "Diurnal",
        "nesting": "A tree hollow containing little or no nesting material",
        "breeding_season": "Usually after rainfall when food is abundant",
        "clutch_size": "Usually 4-7 eggs",
        "call": "Loud whistles, contact calls and chattering",
        "lifespan": "Often several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: widespread across Queensland, New South Wales, South Australia, Western Australia and the Northern Territory, especially in inland regions"
    }
},

{
    "name": "Black Swan",
    "scientific": "Cygnus atratus",
    "description": "The Black Swan is a large Australian waterbird with predominantly black plumage, a long elegant neck and contrasting white flight feathers that become particularly obvious in flight. Its deep red bill has a pale band near the tip. Black Swans inhabit wetlands, lakes, rivers, estuaries and coastal lagoons and feed mainly on aquatic vegetation. They are strong swimmers and can gather in large flocks where suitable wetlands provide abundant food. Unlike many large waterbirds, they are comfortable in both freshwater and saltwater environments.",
    "image": "BlackSwan1.jpg",
    "quick_facts": {
        "family": "Anatidae",
        "size": "110-142 cm",
        "weight": "About 3.7-9 kg",
        "wingspan": "About 160-200 cm",
        "diet": "Aquatic vegetation, algae and other plant material",
        "habitat": "Lakes, rivers, wetlands, estuaries, coastal lagoons and shallow waterways",
        "behaviour": "Usually swims while feeding and may gather in large flocks",
        "activity": "Diurnal",
        "nesting": "A large floating or ground nest made from aquatic vegetation",
        "breeding_season": "Variable, often following favourable rainfall and water conditions",
        "clutch_size": "Usually 5-9 eggs",
        "call": "Soft bugling, trumpeting and musical calls",
        "lifespan": "Often 10-15 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: widespread in suitable wetlands across all mainland states and territories and Tasmania"
    }
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
        "diet": "Roots, tubers, seeds, grasses, insects and other small animals",
        "habitat": "Freshwater wetlands, floodplains, grasslands and open woodland",
        "behaviour": "Forages in wetlands and grasslands and performs elaborate courtship displays",
        "activity": "Diurnal",
        "nesting": "A platform of vegetation built on a shallow wetland or nearby ground",
        "breeding_season": "Usually during the wet season, varying geographically",
        "clutch_size": "Usually 2 eggs",
        "call": "Loud trumpeting calls that carry over long distances",
        "lifespan": "Often many years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: mainly Queensland, New South Wales, Victoria, the Northern Territory and northern Western Australia"
    }
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
        "diet": "Grass seeds, other seeds and small insects",
        "habitat": "Grassland, forest edges, woodland, wetlands, farmland and gardens",
        "behaviour": "Social and usually seen in pairs or small flocks while feeding",
        "activity": "Diurnal",
        "nesting": "A domed grass nest with a side entrance, usually placed in dense vegetation",
        "breeding_season": "Usually spring and summer",
        "clutch_size": "Usually 4-6 eggs",
        "call": "High-pitched twittering and soft contact calls",
        "lifespan": "Often several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: eastern Queensland, New South Wales, Victoria and southeastern South Australia; also Tasmania"
    }
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
        "diet": "Flying insects",
        "habitat": "Wetlands, grassland, farmland, open woodland, parks, towns and coastal areas",
        "behaviour": "Highly aerial and often catches insects while flying low over open ground or water",
        "activity": "Diurnal",
        "nesting": "A mud cup nest attached to a wall, building, bridge or other structure",
        "breeding_season": "Usually August to February",
        "clutch_size": "Usually 3-5 eggs",
        "call": "Rapid twittering and soft chattering calls",
        "lifespan": "Often several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Australia: widespread across Queensland, New South Wales, Victoria, South Australia, Western Australia, the Northern Territory and Tasmania"
    }
},

    ]

birds = sorted(birds, key = lambda bird: bird["name"].lower())

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
    page = page.replace("{{CONSERVATION_STATUS}}", bird["quick_facts"]                ["conservation_status"])
    page = page.replace("{{CALL}}", bird["quick_facts"]["call"])
    page = page.replace("{{LIFESPAN}}", bird["quick_facts"]["lifespan"])
    page = page.replace("{{NESTING}}",bird["quick_facts"]["nesting"])
    page = page.replace("{{HABITAT}}", bird["quick_facts"]["habitat"])
    page = page.replace("{{WHERE_TO_FIND}}",bird["quick_facts"]["where_to_find"])
    page = page.replace("{{SIZE}}",bird["quick_facts"]["size"])
    page = page.replace("{{WEIGHT}}",bird["quick_facts"]["weight"])
    page = page.replace("{{DIET}}",bird["quick_facts"]["diet"])
    page = page.replace("{{BEHAVIOUR}}",bird["quick_facts"]["behaviour"])
    
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
