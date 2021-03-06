from django.core.management.base import BaseCommand

from TWLight.resources.models import Partner


class Command(BaseCommand):
    def handle(self, *args, **options):
        partner_24 = Partner.objects.filter(pk=24, company_name="AAAS").first()
        if partner_24:
            partner_24.new_tags = {
                "tags": [
                    "life-sciences_tag",
                    "physical-sciences_tag",
                    "health-sciences_tag",
                    "earth-sciences_tag",
                ]
            }
            partner_24.save()

        partner_49 = Partner.objects.filter(pk=49, company_name="Adam Matthew").first()
        if partner_49:
            partner_49.new_tags = {"tags": ["culture_tag", "history_tag"]}
            partner_49.save()

        partner_101 = Partner.objects.filter(pk=101, company_name="Al Manhal").first()
        if partner_101:
            partner_101.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_101.save()

        partner_60 = Partner.objects.filter(
            pk=60, company_name="Alexander Street Press"
        ).first()
        if partner_60:
            partner_60.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_60.save()

        partner_84 = Partner.objects.filter(
            pk=84, company_name="American National Biography Online"
        ).first()
        if partner_84:
            partner_84.new_tags = {"tags": ["history_tag"]}
            partner_84.save()

        partner_62 = Partner.objects.filter(
            pk=62, company_name="American Psychiatric Association"
        ).first()
        if partner_62:
            partner_62.new_tags = {"tags": ["health-sciences_tag"]}
            partner_62.save()

        partner_48 = Partner.objects.filter(
            pk=48, company_name="American Psychological Association"
        ).first()
        if partner_48:
            partner_48.new_tags = {"tags": ["social-sciences_tag"]}
            partner_48.save()

        partner_102 = Partner.objects.filter(pk=102, company_name="Ancestry").first()
        if partner_102:
            partner_102.new_tags = {"tags": ["history_tag"]}
            partner_102.save()

        partner_32 = Partner.objects.filter(
            pk=32, company_name="Annual Reviews"
        ).first()
        if partner_32:
            partner_32.new_tags = {"tags": ["life-sciences_tag", "health-sciences_tag"]}
            partner_32.save()

        partner_11 = Partner.objects.filter(pk=11, company_name="ASHA").first()
        if partner_11:
            partner_11.new_tags = {"tags": ["health-sciences_tag"]}
            partner_11.save()

        partner_47 = Partner.objects.filter(
            pk=47, company_name="Baylor University Press"
        ).first()
        if partner_47:
            partner_47.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_47.save()

        partner_73 = Partner.objects.filter(
            pk=73, company_name="Berg Fashion Library"
        ).first()
        if partner_73:
            partner_73.new_tags = {"tags": ["culture_tag"]}
            partner_73.save()

        partner_63 = Partner.objects.filter(pk=63, company_name="BioOne").first()
        if partner_63:
            partner_63.new_tags = {"tags": ["life-sciences_tag"]}
            partner_63.save()

        partner_61 = Partner.even_not_available.filter(
            pk=61, company_name="Bloomsbury"
        ).first()
        if partner_61:
            partner_61.new_tags = {"tags": ["culture_tag", "history_tag"]}
            partner_61.save()

        partner_31 = Partner.objects.filter(pk=31, company_name="BMJ").first()
        if partner_31:
            partner_31.new_tags = {"tags": ["health-sciences_tag"]}
            partner_31.save()

        partner_59 = Partner.even_not_available.filter(
            pk=59, company_name="Brill"
        ).first()
        if partner_59:
            partner_59.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_59.save()

        partner_14 = Partner.even_not_available.filter(
            pk=14, company_name="British Newspaper Archive"
        ).first()
        if partner_14:
            partner_14.new_tags = {"tags": ["history_tag"]}
            partner_14.save()

        partner_46 = Partner.objects.filter(pk=46, company_name="Cairn").first()
        if partner_46:
            partner_46.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_46.save()

        partner_58 = Partner.objects.filter(
            pk=58, company_name="Cambridge University Press"
        ).first()
        if partner_58:
            partner_58.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_58.save()

        partner_64 = Partner.objects.filter(pk=64, company_name="CEEOL").first()
        if partner_64:
            partner_64.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_64.save()

        partner_79 = Partner.objects.filter(pk=79, company_name="Civilica").first()
        if partner_79:
            partner_79.new_tags = {
                "tags": ["physical-sciences_tag", "life-sciences_tag"]
            }
            partner_79.save()

        partner_15 = Partner.objects.filter(pk=15, company_name="Cochrane").first()
        if partner_15:
            partner_15.new_tags = {"tags": ["health-sciences_tag"]}
            partner_15.save()

        partner_105 = Partner.objects.filter(pk=105, company_name="De Gruyter").first()
        if partner_105:
            partner_105.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_105.save()

        partner_83 = Partner.objects.filter(pk=83, company_name="Die Zeit").first()
        if partner_83:
            partner_83.new_tags = {
                "tags": ["culture_tag", "business-and-economics_tag"]
            }
            partner_83.save()

        partner_74 = Partner.objects.filter(pk=74, company_name="Drama Online").first()
        if partner_74:
            partner_74.new_tags = {
                "tags": ["culture_tag", "languages-and-literature_tag"]
            }
            partner_74.save()

        partner_57 = Partner.objects.filter(pk=57, company_name="EBSCO").first()
        if partner_57:
            partner_57.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_57.save()

        partner_71 = Partner.objects.filter(
            pk=71, company_name="Economic & Political Weekly"
        ).first()
        if partner_71:
            partner_71.new_tags = {
                "tags": ["social-sciences_tag", "business-and-economics_tag"]
            }
            partner_71.save()

        partner_45 = Partner.objects.filter(
            pk=45, company_name="Edinburgh University Press"
        ).first()
        if partner_45:
            partner_45.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_45.save()

        partner_9 = Partner.objects.filter(pk=9, company_name="EDP Sciences").first()
        if partner_9:
            partner_9.new_tags = {
                "tags": ["physical-sciences_tag", "life-sciences_tag", "technology_tag"]
            }
            partner_9.save()

        partner_85 = Partner.objects.filter(
            pk=85, company_name="Electronic Enlightenment"
        ).first()
        if partner_85:
            partner_85.new_tags = {"tags": ["history_tag"]}
            partner_85.save()

        partner_23 = Partner.even_not_available.filter(
            pk=23, company_name="Elsevier ScienceDirect"
        ).first()
        if partner_23:
            partner_23.new_tags = {
                "tags": [
                    "life-sciences_tag",
                    "health-sciences_tag",
                    "physical-sciences_tag",
                ]
            }
            partner_23.save()

        partner_56 = Partner.objects.filter(pk=56, company_name="Emerald").first()
        if partner_56:
            partner_56.new_tags = {
                "tags": [
                    "education_tag",
                    "technology_tag",
                    "business-and-economics_tag",
                    "social-sciences_tag",
                ]
            }
            partner_56.save()

        partner_44 = Partner.objects.filter(pk=44, company_name="Érudit").first()
        if partner_44:
            partner_44.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_44.save()

        partner_43 = Partner.objects.filter(pk=43, company_name="Fold3").first()
        if partner_43:
            partner_43.new_tags = {"tags": ["history_tag"]}
            partner_43.save()

        partner_8 = Partner.objects.filter(pk=8, company_name="Foreign Affairs").first()
        if partner_8:
            partner_8.new_tags = {"tags": ["social-sciences_tag"]}
            partner_8.save()

        partner_22 = Partner.objects.filter(
            pk=22, company_name="Future Science Group"
        ).first()
        if partner_22:
            partner_22.new_tags = {
                "tags": [
                    "life-sciences_tag",
                    "health-sciences_tag",
                    "physical-sciences_tag",
                ]
            }
            partner_22.save()

        partner_55 = Partner.objects.filter(pk=55, company_name="Gale").first()
        if partner_55:
            partner_55.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_55.save()

        partner_33 = Partner.objects.filter(pk=33, company_name="HeinOnline").first()
        if partner_33:
            partner_33.new_tags = {"tags": ["law_tag"]}
            partner_33.save()

        partner_29 = Partner.even_not_available.filter(
            pk=29, company_name="HighBeam"
        ).first()
        if partner_29:
            partner_29.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_29.save()

        partner_78 = Partner.objects.filter(
            pk=78, company_name="ICE Publishing"
        ).first()
        if partner_78:
            partner_78.new_tags = {"tags": ["physical-sciences_tag", "technology_tag"]}
            partner_78.save()

        partner_42 = Partner.even_not_available.filter(
            pk=42, company_name="International Monetary Fund"
        ).first()
        if partner_42:
            partner_42.new_tags = {"tags": ["business-and-economics_tag"]}
            partner_42.save()

        partner_68 = Partner.objects.filter(pk=68, company_name="Invaluable").first()
        if partner_68:
            partner_68.new_tags = {"tags": ["art_tag"]}
            partner_68.save()

        partner_77 = Partner.objects.filter(
            pk=77, company_name="IWA Publishing"
        ).first()
        if partner_77:
            partner_77.new_tags = {"tags": ["earth-sciences_tag"]}
            partner_77.save()

        partner_54 = Partner.objects.filter(pk=54, company_name="JSTOR").first()
        if partner_54:
            partner_54.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_54.save()

        partner_28 = Partner.even_not_available.filter(
            pk=28, company_name="Keesings"
        ).first()
        if partner_28:
            partner_28.new_tags = {"tags": ["history_tag"]}
            partner_28.save()

        partner_72 = Partner.objects.filter(pk=72, company_name="Kinige").first()
        if partner_72:
            partner_72.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_72.save()

        partner_18 = Partner.objects.filter(pk=18, company_name="L'Harmattan").first()
        if partner_18:
            partner_18.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_18.save()

        partner_41 = Partner.objects.filter(
            pk=41, company_name="Loeb Classical Library"
        ).first()
        if partner_41:
            partner_41.new_tags = {
                "tags": [
                    "history_tag",
                    "philosophy-and-religion_tag",
                    "languages-and-literature_tag",
                ]
            }
            partner_41.save()

        partner_80 = Partner.objects.filter(pk=80, company_name="Magiran").first()
        if partner_80:
            partner_80.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_80.save()

        partner_16 = Partner.objects.filter(pk=16, company_name="McFarland").first()
        if partner_16:
            partner_16.new_tags = {
                "tags": [
                    "culture_tag",
                    "history_tag",
                    "languages-and-literature_tag",
                    "social-sciences_tag",
                ]
            }
            partner_16.save()

        partner_40 = Partner.objects.filter(pk=40, company_name="Miramar").first()
        if partner_40:
            partner_40.new_tags = {"tags": ["history_tag"]}
            partner_40.save()

        partner_53 = Partner.objects.filter(pk=53, company_name="MIT").first()
        if partner_53:
            partner_53.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_53.save()

        partner_27 = Partner.objects.filter(
            pk=27, company_name="NewspaperARCHIVE.com"
        ).first()
        if partner_27:
            partner_27.new_tags = {"tags": ["history_tag", "culture_tag"]}
            partner_27.save()

        partner_26 = Partner.objects.filter(
            pk=26, company_name="Newspapers.com"
        ).first()
        if partner_26:
            partner_26.new_tags = {"tags": ["history_tag", "culture_tag"]}
            partner_26.save()

        partner_106 = Partner.objects.filter(pk=106, company_name="Nomos").first()
        if partner_106:
            partner_106.new_tags = {"tags": ["law_tag", "social-sciences_tag"]}
            partner_106.save()

        partner_81 = Partner.objects.filter(pk=81, company_name="Noormags").first()
        if partner_81:
            partner_81.new_tags = {
                "tags": ["social-sciences_tag", "philosophy-and-religion_tag"]
            }
            partner_81.save()

        partner_17 = Partner.objects.filter(
            pk=17, company_name="Numérique Premium"
        ).first()
        if partner_17:
            partner_17.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_17.save()

        partner_13 = Partner.objects.filter(pk=13, company_name="OpenEdition").first()
        if partner_13:
            partner_13.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_13.save()

        partner_86 = Partner.objects.filter(
            pk=86, company_name="Oxford Art Online"
        ).first()
        if partner_86:
            partner_86.new_tags = {"tags": ["art_tag"]}
            partner_86.save()

        partner_87 = Partner.objects.filter(
            pk=87, company_name="Oxford Bibliographies Online"
        ).first()
        if partner_87:
            partner_87.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_87.save()

        partner_88 = Partner.objects.filter(
            pk=88, company_name="Oxford Dictionary of National Biography"
        ).first()
        if partner_88:
            partner_88.new_tags = {"tags": ["history_tag"]}
            partner_88.save()

        partner_89 = Partner.objects.filter(
            pk=89, company_name="Oxford Handbooks Online"
        ).first()
        if partner_89:
            partner_89.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_89.save()

        partner_93 = Partner.objects.filter(
            pk=93, company_name="Oxford Journals"
        ).first()
        if partner_93:
            partner_93.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_93.save()

        partner_99 = Partner.objects.filter(pk=99, company_name="Oxford Law").first()
        if partner_99:
            partner_99.new_tags = {"tags": ["law_tag"]}
            partner_99.save()

        partner_90 = Partner.objects.filter(
            pk=90, company_name="Oxford Music Online"
        ).first()
        if partner_90:
            partner_90.new_tags = {"tags": ["music_tag"]}
            partner_90.save()

        partner_91 = Partner.objects.filter(
            pk=91, company_name="Oxford Reference Online"
        ).first()
        if partner_91:
            partner_91.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_91.save()

        partner_92 = Partner.objects.filter(
            pk=92, company_name="Oxford Scholarship Online"
        ).first()
        if partner_92:
            partner_92.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_92.save()

        partner_52 = Partner.even_not_available.filter(
            pk=52, company_name="Oxford University Press"
        ).first()
        if partner_52:
            partner_52.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_52.save()

        partner_39 = Partner.objects.filter(pk=39, company_name="Past Masters").first()
        if partner_39:
            partner_39.new_tags = {
                "tags": ["philosophy-and-religion_tag", "languages-and-literature_tag"]
            }
            partner_39.save()

        partner_51 = Partner.even_not_available.filter(
            pk=51, company_name="Pelican Books"
        ).first()
        if partner_51:
            partner_51.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_51.save()

        partner_104 = Partner.objects.filter(pk=104, company_name="PNAS").first()
        if partner_104:
            partner_104.new_tags = {
                "tags": [
                    "physical-sciences_tag",
                    "life-sciences_tag",
                    "social-sciences_tag",
                ]
            }
            partner_104.save()

        partner_38 = Partner.objects.filter(pk=38, company_name="Project MUSE").first()
        if partner_38:
            partner_38.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_38.save()

        partner_82 = Partner.objects.filter(pk=82, company_name="ProQuest").first()
        if partner_82:
            partner_82.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_82.save()

        partner_25 = Partner.even_not_available.filter(
            pk=25, company_name="Questia"
        ).first()
        if partner_25:
            partner_25.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_25.save()

        partner_100 = Partner.objects.filter(
            pk=100,
            company_name="Répertoire International de Littérature Musicale (RILM)",
        ).first()
        if partner_100:
            partner_100.new_tags = {"tags": ["music_tag"]}
            partner_100.save()

        partner_37 = Partner.objects.filter(pk=37, company_name="RIPM").first()
        if partner_37:
            partner_37.new_tags = {"tags": ["music_tag"]}
            partner_37.save()

        partner_69 = Partner.objects.filter(
            pk=69, company_name="Rock's Backpages"
        ).first()
        if partner_69:
            partner_69.new_tags = {"tags": ["music_tag"]}
            partner_69.save()

        partner_30 = Partner.objects.filter(
            pk=30, company_name="Royal Pharmaceutical Society"
        ).first()
        if partner_30:
            partner_30.new_tags = {"tags": ["health-sciences_tag"]}
            partner_30.save()

        partner_20 = Partner.objects.filter(pk=20, company_name="Royal Society").first()
        if partner_20:
            partner_20.new_tags = {
                "tags": ["physical-sciences_tag", "life-sciences_tag"]
            }
            partner_20.save()

        partner_21 = Partner.objects.filter(
            pk=21, company_name="Royal Society of Chemistry (RSC Gold)"
        ).first()
        if partner_21:
            partner_21.new_tags = {"tags": ["physical-sciences_tag"]}
            partner_21.save()

        partner_50 = Partner.objects.filter(pk=50, company_name="Sabinet").first()
        if partner_50:
            partner_50.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_50.save()

        partner_36 = Partner.even_not_available.filter(
            pk=36, company_name="SAGE Stats"
        ).first()
        if partner_36:
            partner_36.new_tags = {"tags": ["social-sciences_tag"]}
            partner_36.save()

        partner_67 = Partner.objects.filter(
            pk=67, company_name="Springer Nature"
        ).first()
        if partner_67:
            partner_67.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_67.save()

        partner_103 = Partner.objects.filter(pk=103, company_name="Taxmann").first()
        if partner_103:
            partner_103.new_tags = {"tags": ["business-and-economics_tag"]}
            partner_103.save()

        partner_10 = Partner.objects.filter(
            pk=10, company_name="Taylor & Francis"
        ).first()
        if partner_10:
            partner_10.new_tags = {"tags": ["multidisciplinary_tag"]}
            partner_10.save()

        partner_70 = Partner.objects.filter(pk=70, company_name="Termsoup").first()
        if partner_70:
            partner_70.new_tags = {"tags": ["languages-and-literature_tag"]}
            partner_70.save()

        partner_12 = Partner.objects.filter(pk=12, company_name="Tilastopaja").first()
        if partner_12:
            partner_12.new_tags = {"tags": ["culture_tag"]}
            partner_12.save()

        partner_75 = Partner.even_not_available.filter(
            pk=75, company_name="Whitaker's"
        ).first()
        if partner_75:
            partner_75.new_tags = {"tags": ["history_tag"]}
            partner_75.save()

        partner_76 = Partner.objects.filter(pk=76, company_name="Who's Who").first()
        if partner_76:
            partner_76.new_tags = {"tags": ["history_tag"]}
            partner_76.save()

        partner_35 = Partner.objects.filter(
            pk=35, company_name="Women Writers Online"
        ).first()
        if partner_35:
            partner_35.new_tags = {"tags": ["languages-and-literature_tag"]}
            partner_35.save()

        partner_34 = Partner.objects.filter(pk=34, company_name="World Bank").first()
        if partner_34:
            partner_34.new_tags = {"tags": ["business-and-economics_tag"]}
            partner_34.save()

        partner_19 = Partner.objects.filter(
            pk=19, company_name="World Scientific"
        ).first()
        if partner_19:
            partner_19.new_tags = {
                "tags": [
                    "life-sciences_tag",
                    "health-sciences_tag",
                    "physical-sciences_tag",
                ]
            }
            partner_19.save()
