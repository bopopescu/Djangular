from django.db import models

# Create your models here.

# = models.CharField(max_length=100)
# = models.FloatField(null=True, blank=True)
# = models.IntegerField()
# = models.BooleanField(default=False)



# Documentation:
# http://units.tauniverse.com/tutorials/tadesign/tadesign/tdfdown.htm
class DownloadTDF(models.Model):
    parent_unit = models.ForeignKey(UnitFbiData, on_delete=models.CASCADE,)
    MENUENTRY = models.CharField(max_length=20, default='MENUENTRY1') # [MENUENTRY1] [MENUENTRY2] [MENUENTRY3] etc...
    BUTTON = models.PositiveSmallIntegerField(default=0) # See 'TA Button' below
    MENU = models.PositiveSmallIntegerField(default=2) # first menu in TA is actually '2' for some reason
    UNITMENU = models.CharField(max_length=35) # short name for the construction unit that builds this unit
    UNITNAME = models.CharField(max_length=35) # short name of the unit this button builds
# TA Button:
#######
# 0 1 #
# 2 3 #
# 4 5 #
#######


# SEX = (
#     ('male', 'Male'),
#     ('female', 'Female'),
# )
# sex = models.CharField(choices=SEX, null=True, blank=True, max_length=10)


class FeatureTDF(models.Model):
    animating = models.BooleanField(default=False)
    animtrans = models.BooleanField(default=False, blank=True)
    autoreclaimable = models.BooleanField(default=True)
    burnmax = models.IntegerField(default=18, blank=True)
    burnmin = models.IntegerField(default=15, blank=True)
    burnweapon = models.CharField(blank=True)
    CATEGORIES = (
        ('arm_corpses', 'arm_corpses'),
        ('cor_corpses', 'cor_corpses'),
        ('heaps', 'heaps'),
        ('steamvents', 'steamvents'),
        ('rocks', 'rocks'),
    )
    category = models.CharField(blank=True, choices=CATEGORIES, max_length=40)
    description = models.CharField(max_length=135)
    blocking = models.BooleanField(default=False)
    damage = models.IntegerField(default=1800)
    energy = models.IntegerField(default=250)
    featuredead = models.CharField(max_length=135)
    featurereclamate = models.CharField(max_length=135)
    filename = models.CharField(max_length=135)
    flamable = models.BooleanField(default=False)
    footprintx = models.IntegerField(default=2)
    footprintz = models.IntegerField(default=2)
    geothermal = models.BooleanField(default=False)
    height = models.IntegerField(default=25)
    hitdensity = models.IntegerField(default=25)
    indestructible = models.BooleanField(default=False)
    metal = models.IntegerField(default=250)
    nodisplayinfo = models.BooleanField(default=False)
    _object = models.CharField(max_length=135)
    permanent = models.BooleanField(default=False)
    reclaimable = models.BooleanField(default=True)
    reproduce = models.BooleanField(default=False)
    reproducearea = models.BooleanField(default=False)
    seqname = models.CharField(max_length=135)
    seqnameburn = models.CharField(max_length=135)
    seqnamedie = models.CharField(max_length=135)
    seqnamereclamate = models.CharField(max_length=135)
    seqnameshad = models.CharField(max_length=135)
    shadtrans = models.BooleanField(default=True)
    sparktime = models.IntegerField(default=5)
    spreadchance = models.IntegerField(default=30)
    world = models.CharField(max_length=135)


# Documentation:
# http://units.tauniverse.com/tutorials/tadesign/tadesign/fbidesc.htm
class UnitFbiData(models.Model):
    _raw_json_dump = models.CharField(max_length=100)
    Acceleration = models.FloatField(null=True, blank=True)
    ActiveWhenBuild = models.IntegerField()
    ai_limit = models.CharField(max_length=100)
    ai_weight = models.CharField(max_length=100)
    altfromsealevel = models.IntegerField()
    amphibious = models.BooleanField(default=False)
    antiweapons = models.BooleanField(default=False)
    attackrunlength = models.IntegerField()
    BMcode = models.BooleanField(default=False)
    BadTargetCategory = models.CharField(max_length=100)
    BankScale = models.IntegerField()
    BrakeRate = models.IntegerField()
    BuildAngle = models.IntegerField()
    BuildCostEnergy = models.IntegerField()
    BuildCostMetal = models.IntegerField()
    BuildTime = models.IntegerField()
    Builddistance = models.IntegerField()
    Builder = models.BooleanField(default=False)
    canattack = models.BooleanField(default=False)
    CanCapture = models.BooleanField(default=False)
    CanDgun = models.BooleanField(default=False)
    Canfly = models.BooleanField(default=False)
    canguard = models.BooleanField(default=False)
    canhover = models.BooleanField(default=False)
    canload = models.BooleanField(default=False)
    canmove = models.BooleanField(default=False)
    canpatrol = models.BooleanField(default=False)
    CanReclamate = models.BooleanField(default=False)
    canstop = models.BooleanField(default=False)
    cantbetransported = models.BooleanField(default=False)
    Category = models.CharField(max_length=100)
    CloakCost = models.IntegerField()
    CloakCostMoving = models.IntegerField()
    Commander = models.BooleanField(default=False)
    Copyright = models.CharField(max_length=100)
    #TODO: PK below
    Corpse = models.CharField(max_length=100)
    cruisealt = models.IntegerField()
    DamageModifier = models.FloatField(null=True, blank=True)
    DefaultMissionType = models.CharField(max_length=100)
    Description = models.CharField(max_length=255)
    Designation = models.CharField(max_length=50)
    digger = models.BooleanField(default=False)
    Downloadable = models.BooleanField(default=False)
    EnergyMake = models.IntegerField()
    EnergyStorage = models.IntegerField()
    EnergyUse = models.IntegerField()
    # TODO: Many-To-One
    ExplodeAs = models.CharField(max_length=100)
    ExtractsMetal = models.FloatField(null=True, blank=True)
    firestandorders = models.IntegerField()
    Floater = models.BooleanField(default=False)
    FootprintX = models.IntegerField()
    FootprintZ = models.IntegerField()
    FrenchDescription = models.CharField(max_length=100)
    FrenchName = models.CharField(max_length=100)
    GermanDescription = models.CharField(max_length=100)
    GermanName = models.CharField(max_length=100)
    HealTime = models.IntegerField()
    HideDamage = models.BooleanField(default=False)
    HoverAttack = models.BooleanField(default=False)
    ImmuneToParalyzer = models.BooleanField(default=False)
    init_cloaked = models.BooleanField(default=False)
    IsAirBase = models.BooleanField(default=False)
    IsFeature = models.BooleanField(default=False)
    istargetingupgrade = models.BooleanField(default=False)
    ItalianDescription = models.CharField(max_length=100)
    ItalianName = models.CharField(max_length=100)
    JapanesDescription = models.CharField(max_length=100)
    JapaneseName = models.CharField(max_length=100)
    kamikaze = models.BooleanField(default=False)
    kamikazedistance = models.IntegerField()
    MakesMetal = models.BooleanField(default=False)
    maneuverleashlength = models.IntegerField()
    MaxDamage = models.IntegerField()
    MaxSlope = models.IntegerField()
    MaxVelocity = models.IntegerField()
    MaxWaterDepth = models.IntegerField()
    MetalMake = models.IntegerField()
    MetalStorage = models.IntegerField()
    mincloakdistance = models.IntegerField()
    MinWaterDepth = models.IntegerField()
    MobileStandOrders = models.BooleanField(default=False)
    MoveRate1 = models.IntegerField()
    # TODO: PK below:
    MovementClass = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    NoAutoFire = models.BooleanField(default=False)
    NoChaseCategory = models.CharField(max_length=100)
    norestrict = models.BooleanField(default=False)
    NoShadow = models.BooleanField(default=False)
    # TODO: PK below
    Objectname = models.CharField(max_length=100)
    onoffable = models.BooleanField(default=False)
    Ovradjust = models.BooleanField(default=False)
    PigLatinDescription = models.CharField(max_length=100)
    PigLatinName = models.CharField(max_length=100)
    PitchScale = models.IntegerField(max_length=100)
    RadarDistance = models.IntegerField()
    RadarDistanceJam = models.IntegerField()
    Scale = models.IntegerField()
    # TODO: List of string choices will go below
    SelfDestructAs = models.CharField(max_length=100)
    selfdestructcountdown = models.IntegerField()
    ShootMe = models.BooleanField(default=False)
    ShowPlayerName = models.BooleanField(default=False)
    # TODO: List of string choices will go below
    Side = models.CharField(max_length=100)
    SightDistance = models.IntegerField()
    SonarDistance = models.IntegerField()
    SonarDistanceJam = models.IntegerField()
    sortbias = models.IntegerField()
    # TODO: List of string choices will go below
    SoundCategory = models.CharField(max_length=100)
    SpanishDescription = models.CharField(max_length=100)
    SpanishName = models.CharField(max_length=100)
    StandingFireOrder = models.IntegerField()
    StandingMoveOrder = models.IntegerField()
    Stealth = models.BooleanField(default=False)
    SteeringMode = models.IntegerField()
    # TODO: List of string choices will go below
    TEDClass = models.CharField(max_length=100)
    teleporter = models.BooleanField(default=False)
    ThreeD = models.BooleanField(default=False)
    TidalGenerator = models.BooleanField(default=False)
    TransMaxUnits = models.IntegerField()
    transportcapacity = models.IntegerField()
    transportsize = models.IntegerField()
    TurnRate = models.IntegerField()
    # TODO: unique? ID?
    UnitName = models.CharField(max_length=100)
    # TODO: must be unique, PK?
    UnitNumber = models.IntegerField()
    Upright = models.BooleanField(default=False)
    Version = models.IntegerField()
    WaterLine = models.IntegerField()
    # TODO: PK below
    Weapon1 = models.CharField(max_length=100)
    # TODO: PK below
    Weapon2 = models.CharField(max_length=100)
    # TODO: PK below
    Weapon3 = models.CharField(max_length=100)
    WindGenerator = models.IntegerField()
    WorkerTime = models.IntegerField()
    # TODO: PK below
    wpri_badTargetCategory = models.CharField(max_length=100)
    # TODO: ManyToMany below
    wsec_badTargetCategory = models.CharField(max_length=100)
    YardMap = models.CharField(max_length=100)
    def __str__(self):  # __unicode__ on Python 2
        return self.Objectname



# ONE-TO-ONE SAMPLE:
"""
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the place" % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )

"""

# MANY-TO-MANY SAMPLE:
"""
class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline',)
"""

# MANY-TO-ONE SAMPLE:
"""
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline',)
"""
