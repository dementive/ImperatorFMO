# pdxgui_default.shader with a bunch of different effects
# Use effectname = "x" in the gui to use a different pixel shader for different gui widgets

Includes = {
	"cw/pdxgui.fxh"
	"cw/pdxgui_sprite.fxh"
	"cw/utility.fxh"
	"standardfuncsgfx.fxh" 
	# standardfuncsgfx.fxh imported for GlobalTime
	# If using in Victoria 3 change to "sharedconstants.fxh"
	# If using in CK3 or Imperator keep "standardfuncsgfx.fxh"
}

VertexShader =
{
	MainCode VS_Default
	{
		Input = "VS_INPUT_PDX_GUI"
		Output = "VS_OUTPUT_PDX_GUI"
		Code
		[[
			PDX_MAIN
			{
				return PdxGuiDefaultVertexShader( Input );
			}
		]]
	}
}

PixelShader =
{
	TextureSampler Texture
	{
		Ref = PdxTexture0
		MagFilter = "Point"
		MinFilter = "Point"
		MipFilter = "Point"
		SampleModeU = "Clamp"
		SampleModeV = "Clamp"
	}
	MainCode PS_Default
	{	
		Input = "VS_OUTPUT_PDX_GUI"
		Output = "PDX_COLOR"
		Code
		[[
			PDX_MAIN
			{
				float4 OutColor = SampleImageSprite( Texture, Input.UV0 );
				OutColor *= Input.Color;
				
				#ifdef DISABLED
					OutColor.rgb = DisableColor( OutColor.rgb );
				#endif
				
			    return OutColor;
			}
		]]
	}
	MainCode PS_GuiBloom
	{	
		Input = "VS_OUTPUT_PDX_GUI"
		Output = "PDX_COLOR"
		Code
		[[
			PDX_MAIN
			{
				// https://github.com/dinfinity/mpc-pixel-shaders/blob/master/PS_Bloom.hlsl
				float4 OutColor = SampleImageSprite( Texture, Input.UV0 );
				OutColor *= Input.Color;

				#define angleSteps 12
				#define radiusSteps 10
				#define minRadius (0.0/Input.Position.x)
				#define maxRadius (10.0/Input.Position.x)
				#define ampFactor 1.3
				float correction = 0.6;

				float4 accumulatedColor = float4(0,0,0,0);
				int totalSteps = radiusSteps * angleSteps;
				float angleDelta = (2 * PI) / angleSteps;
				float radiusDelta = (maxRadius - minRadius) / radiusSteps;

				for (int radiusStep = 0; radiusStep < radiusSteps; radiusStep++) {
					float radius = minRadius + radiusStep * radiusDelta;

					for (float angle=0; angle <(2*PI); angle += angleDelta) {
						float2 currentCoord;

						float xDiff = radius * cos(angle);
						float yDiff = radius * sin(angle);
						
						currentCoord = Input.UV0 + float2(xDiff, yDiff);
						float4 currentColor = SampleImageSprite(Texture, currentCoord);
						float currentFraction = ((float)(radiusSteps+1 - radiusStep)) / (radiusSteps+1);

						accumulatedColor +=   currentFraction * currentColor / totalSteps;
					}
				}

				float4 outputPixel = SampleImageSprite(Texture, Input.UV0);
				outputPixel += accumulatedColor * ampFactor;
				outputPixel *= correction;
				OutColor = float4(outputPixel.rgb, OutColor.a);
				#ifdef DISABLED
					OutColor.rgb = DisableColor( OutColor.rgb );
				#endif
			    return OutColor;
			}
		]]
	}
}

BlendState BlendState
{
	BlendEnable = yes
	SourceBlend = "SRC_ALPHA"
	DestBlend = "INV_SRC_ALPHA"
}

BlendState BlendStateNoAlpha
{
	BlendEnable = no
}

BlendState PreMultipliedAlpha
{
	BlendEnable = yes
	SourceBlend = "ONE"
	DestBlend = "INV_SRC_ALPHA"
}

DepthStencilState DepthStencilState
{
	DepthEnable = no
}


Effect PdxGuiDefault
{
	VertexShader = "VS_Default"
	PixelShader = "PS_Default"
}
Effect PdxGuiDefaultDisabled
{
	VertexShader = "VS_Default"
	PixelShader = "PS_Default"
	
	Defines = { "DISABLED" }
}

Effect PdxGuiDefaultNoAlpha
{
	VertexShader = "VS_Default"
	PixelShader = "PS_Default"
	BlendState = BlendStateNoAlpha
}
Effect PdxGuiDefaultNoAlphaDisabled
{
	VertexShader = "VS_Default"
	PixelShader = "PS_Default"
	BlendState = BlendStateNoAlpha
	
	Defines = { "DISABLED" }
}

Effect PdxGuiPreMultipliedAlpha
{
	VertexShader = "VS_Default"
	PixelShader = "PS_Default"
	BlendState = PreMultipliedAlpha
}
Effect PdxGuiPreMultipliedAlphaDisabled
{
	VertexShader = "VS_Default"
	PixelShader = "PS_Default"
	BlendState = PreMultipliedAlpha
	
	Defines = { "DISABLED" }
}

Effect GuiBloom
{
	VertexShader = "VS_Default"
	PixelShader = "PS_GuiBloom"
}
Effect GuiBloomDisabled
{
	VertexShader = "VS_Default"
	PixelShader = "PS_GuiBloom"
	
	Defines = { "DISABLED" }
}
